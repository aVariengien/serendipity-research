from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import HuberRegressor, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

SEED = 42
PROBLEM_LIKES_P90 = 87
PROBLEM_RTS_P90 = 2


def read_scrapes(data_dir: Path) -> pd.DataFrame:
    files = sorted(data_dir.glob("*.json"))
    if not files:
        raise RuntimeError(f"No scrape JSON files found in {data_dir}")

    rows: list[dict[str, Any]] = []
    for fp in files:
        with fp.open("r", encoding="utf-8") as f:
            payload = json.load(f)
        for r in payload.get("rows", []):
            rows.append(
                {
                    "source_file": fp.name,
                    "tweetId": r.get("tweetId"),
                    "createdAt": r.get("createdAt"),
                    "scrapedAt": r.get("scrapedAt"),
                    "likes": r.get("likes"),
                    "retweets": r.get("retweets"),
                    "views": r.get("views"),
                }
            )

    df = pd.DataFrame(rows)
    if df.empty:
        raise RuntimeError("Scrape files loaded but no rows found.")
    return df


def to_num(v: Any) -> float:
    if v is None:
        return np.nan
    if isinstance(v, (int, float, np.integer, np.floating)):
        return float(v)
    s = str(v).strip().replace(",", "").upper()
    if not s:
        return np.nan
    mult = 1.0
    if s.endswith("K"):
        mult = 1e3
        s = s[:-1]
    elif s.endswith("M"):
        mult = 1e6
        s = s[:-1]
    elif s.endswith("B"):
        mult = 1e9
        s = s[:-1]
    try:
        return float(s) * mult
    except ValueError:
        return np.nan


def dedupe_latest(df: pd.DataFrame) -> pd.DataFrame:
    x = df.copy()
    x["likes"] = x["likes"].map(to_num)
    x["retweets"] = x["retweets"].map(to_num)
    x["views"] = x["views"].map(to_num)
    x["scrapedAt"] = pd.to_datetime(x["scrapedAt"], errors="coerce", utc=True)
    x = x.dropna(subset=["tweetId"])

    # Keep latest scrape per tweet, but also guard against partial updates by taking max counters.
    g = x.sort_values("scrapedAt").groupby("tweetId", as_index=False)
    out = g.agg(
        {
            "source_file": "last",
            "createdAt": "last",
            "scrapedAt": "last",
            "likes": "max",
            "retweets": "max",
            "views": "max",
        }
    )
    out = out.dropna(subset=["likes", "retweets", "views"])
    out = out[(out["views"] > 0) & (out["likes"] >= 0) & (out["retweets"] >= 0)]
    return out.reset_index(drop=True)


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    x = df.copy()
    x["likes_log"] = np.log1p(x["likes"])
    x["retweets_log"] = np.log1p(x["retweets"])
    x["retweets_zero"] = (x["retweets"] == 0).astype(int)
    x["like_rt_interaction"] = x["likes_log"] * x["retweets_log"]
    x["views_log"] = np.log1p(x["views"])
    return x


def make_model(name: str) -> Pipeline:
    feats = ["likes_log", "retweets_log", "retweets_zero", "like_rt_interaction"]
    pre = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                feats,
            )
        ],
        remainder="drop",
    )

    if name == "ridge":
        reg = Ridge(alpha=1.0, random_state=SEED)
    elif name == "huber":
        reg = HuberRegressor(epsilon=1.35, alpha=0.0001)
    elif name == "gbr":
        reg = GradientBoostingRegressor(
            random_state=SEED, n_estimators=300, learning_rate=0.05, max_depth=2
        )
    elif name == "rf":
        reg = RandomForestRegressor(
            random_state=SEED, n_estimators=250, max_depth=12, min_samples_leaf=4, n_jobs=-1
        )
    else:
        raise ValueError(name)

    return Pipeline(steps=[("pre", pre), ("reg", reg)])


def evaluate_models(df: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    model_names = ["ridge", "huber", "gbr", "rf"]
    splitter = ShuffleSplit(n_splits=8, test_size=0.2, random_state=SEED)

    X = df[["likes_log", "retweets_log", "retweets_zero", "like_rt_interaction"]]
    y = df["views_log"].values

    rows = []
    for name in model_names:
        fold_mae = []
        fold_rmse = []
        fold_r2 = []
        fold_mae_problem = []
        fold_rmse_problem = []
        fold_r2_problem = []
        for tr, te in splitter.split(X):
            model = make_model(name)
            tr_df = df.iloc[tr]
            tr_weights = np.where(
                (tr_df["likes"] <= PROBLEM_LIKES_P90) & (tr_df["retweets"] <= PROBLEM_RTS_P90),
                3.5,
                1.0,
            )
            model.fit(X.iloc[tr], y[tr], reg__sample_weight=tr_weights)
            pred = model.predict(X.iloc[te])
            fold_mae.append(mean_absolute_error(y[te], pred))
            fold_rmse.append(math.sqrt(mean_squared_error(y[te], pred)))
            fold_r2.append(r2_score(y[te], pred))

            te_df = df.iloc[te]
            problem_mask = (te_df["likes"] <= PROBLEM_LIKES_P90) & (
                te_df["retweets"] <= PROBLEM_RTS_P90
            )
            if problem_mask.any():
                y_prob = y[te][problem_mask.to_numpy()]
                p_prob = pred[problem_mask.to_numpy()]
                fold_mae_problem.append(mean_absolute_error(y_prob, p_prob))
                fold_rmse_problem.append(math.sqrt(mean_squared_error(y_prob, p_prob)))
                fold_r2_problem.append(r2_score(y_prob, p_prob))
        rows.append(
            {
                "model": name,
                "mae_log_mean": float(np.mean(fold_mae)),
                "rmse_log_mean": float(np.mean(fold_rmse)),
                "r2_log_mean": float(np.mean(fold_r2)),
                "mae_log_problem_mean": float(np.mean(fold_mae_problem)),
                "rmse_log_problem_mean": float(np.mean(fold_rmse_problem)),
                "r2_log_problem_mean": float(np.mean(fold_r2_problem)),
            }
        )

    # Choose model by performance on the target low-like/low-retweet regime.
    res = pd.DataFrame(rows).sort_values("mae_log_problem_mean").reset_index(drop=True)
    return res, str(res.iloc[0]["model"])


def fit_final(df: pd.DataFrame, best_model: str) -> Pipeline:
    X = df[["likes_log", "retweets_log", "retweets_zero", "like_rt_interaction"]]
    y = df["views_log"].values
    model = make_model(best_model)
    weights = np.where(
        (df["likes"] <= PROBLEM_LIKES_P90) & (df["retweets"] <= PROBLEM_RTS_P90),
        3.5,
        1.0,
    )
    model.fit(X, y, reg__sample_weight=weights)
    return model


def diagnostic_plot(df: pd.DataFrame, model: Pipeline, out_path: Path) -> None:
    X = df[["likes_log", "retweets_log", "retweets_zero", "like_rt_interaction"]]
    pred_log = model.predict(X)
    pred = np.expm1(pred_log)

    # Sample for legibility
    n = min(5000, len(df))
    plot_df = df.sample(n, random_state=SEED).copy()
    plot_df["pred_views"] = pred[plot_df.index]

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    sns.scatterplot(
        data=plot_df,
        x="views",
        y="pred_views",
        alpha=0.25,
        s=14,
        ax=ax,
        color="#2563eb",
    )
    vmin = float(min(plot_df["views"].min(), plot_df["pred_views"].min()))
    vmax = float(max(plot_df["views"].max(), plot_df["pred_views"].max()))
    ax.plot([vmin, vmax], [vmin, vmax], "--", color="black", linewidth=1)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Actual views")
    ax.set_ylabel("Predicted views")
    ax.set_title("Predicted vs Actual views (log-log)")
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def feature_overlay_plots(df: pd.DataFrame, model: Pipeline, out_dir: Path) -> None:
    X = df[["likes_log", "retweets_log", "retweets_zero", "like_rt_interaction"]]
    pred_log = model.predict(X)

    plot_df = df.copy()
    plot_df["pred_views"] = np.expm1(pred_log)

    # Keep plots readable on very large datasets.
    if len(plot_df) > 7000:
        plot_df = plot_df.sample(7000, random_state=SEED)

    sns.set_theme(style="whitegrid")
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1) Views vs likes with actual + model points.
    fig, ax = plt.subplots(figsize=(9, 5.8))
    sns.scatterplot(
        data=plot_df,
        x="likes",
        y="views",
        alpha=0.22,
        s=14,
        color="#2563eb",
        label="Actual",
        ax=ax,
    )
    sns.scatterplot(
        data=plot_df,
        x="likes",
        y="pred_views",
        alpha=0.18,
        s=14,
        color="#f97316",
        label="Model prediction",
        ax=ax,
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Likes")
    ax.set_ylabel("Views")
    ax.set_title("Model vs Actual: Views by Likes")
    fig.tight_layout()
    fig.savefig(out_dir / "model_vs_likes_with_actual.png", dpi=150)
    plt.close(fig)

    # 2) Views vs retweets with actual + model points.
    fig, ax = plt.subplots(figsize=(9, 5.8))
    sns.scatterplot(
        data=plot_df,
        x="retweets",
        y="views",
        alpha=0.22,
        s=14,
        color="#2563eb",
        label="Actual",
        ax=ax,
    )
    sns.scatterplot(
        data=plot_df,
        x="retweets",
        y="pred_views",
        alpha=0.18,
        s=14,
        color="#f97316",
        label="Model prediction",
        ax=ax,
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Retweets")
    ax.set_ylabel("Views")
    ax.set_title("Model vs Actual: Views by Retweets")
    fig.tight_layout()
    fig.savefig(out_dir / "model_vs_retweets_with_actual.png", dpi=150)
    plt.close(fig)


def write_report(
    df: pd.DataFrame, model_results: pd.DataFrame, best_model: str, report_path: Path
) -> None:
    likes = df["likes"]
    rts = df["retweets"]

    def pct(a: pd.Series, q: float) -> float:
        return float(np.percentile(a, q))

    lines = []
    lines.append("# Views prediction model (scraped timeline)")
    lines.append("")
    lines.append("## Data")
    lines.append(f"- Tweets used (deduplicated): **{len(df)}**")
    lines.append(f"- Likes zero rate: **{(likes.eq(0).mean()*100):.1f}%**")
    lines.append(f"- Retweets zero rate: **{(rts.eq(0).mean()*100):.1f}%**")
    lines.append("")
    lines.append("### Likes distribution")
    lines.append(f"- median: {likes.median():.0f}")
    lines.append(f"- mean: {likes.mean():.1f}")
    lines.append(f"- p75: {pct(likes, 75):.0f}")
    lines.append(f"- p90: {pct(likes, 90):.0f}")
    lines.append(f"- p99: {pct(likes, 99):.0f}")
    lines.append(f"- max: {likes.max():.0f}")
    lines.append("")
    lines.append("### Retweets distribution")
    lines.append(f"- median: {rts.median():.0f}")
    lines.append(f"- mean: {rts.mean():.1f}")
    lines.append(f"- p75: {pct(rts, 75):.0f}")
    lines.append(f"- p90: {pct(rts, 90):.0f}")
    lines.append(f"- p99: {pct(rts, 99):.0f}")
    lines.append(f"- max: {rts.max():.0f}")
    lines.append("")
    lines.append("## Modeling choices suited for this distribution")
    lines.append("- Predict in **log-space**: target = `log1p(views)` to stabilize heavy tails.")
    lines.append("- Use **log features**: `log1p(likes)`, `log1p(retweets)`.")
    lines.append("- Add **zero-retweet indicator** for the 0-inflated retweet mass.")
    lines.append("- Add interaction term to capture non-linear coupling.")
    lines.append("- Reweight training data toward problem-like tweets (`likes<=87`, `retweets<=2`).")
    lines.append("- Evaluate with shuffled train/test splits (8 repeats).")
    lines.append("- Select best model by **problem-regime MAE (log)**, not only global average.")
    lines.append("")
    lines.append("## Model comparison")
    lines.append("```")
    lines.append(model_results.to_string(index=False, float_format=lambda v: f"{v:.4f}"))
    lines.append("```")
    lines.append("")
    lines.append(f"## Selected model: `{best_model}`")
    lines.append("- Selection criterion: lowest **problem-regime MAE (log)**.")
    lines.append(
        "- Interpretation: typical multiplicative error in the focus regime is about "
        f"`exp({model_results.iloc[0]['mae_log_problem_mean']:.4f}) ~= "
        f"{math.exp(float(model_results.iloc[0]['mae_log_problem_mean'])):.2f}x`."
    )
    lines.append("")
    lines.append("## Outputs")
    lines.append("Artifact files:")
    lines.append("- `outputs/views_model_results.csv`")
    lines.append("- `outputs/views_model.joblib`")
    lines.append("- `outputs/predict_views.py`")
    lines.append("- `outputs/predict_views_standalone.py`")
    lines.append("- `outputs/pred_vs_actual_views.png`")
    lines.append("- `outputs/model_vs_likes_with_actual.png`")
    lines.append("- `outputs/model_vs_retweets_with_actual.png`")
    lines.append("")
    lines.append("## Inference")
    lines.append("- Joblib-based: `predict_views(likes, retweets)` in `outputs/predict_views.py`.")
    lines.append(
        "- Standalone (no sklearn/joblib): `predict_views(likes, retweets)` in "
        "`outputs/predict_views_standalone.py`."
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def write_predictor_script(path: Path) -> None:
    content = """import math
import joblib
import pandas as pd

_model = joblib.load("outputs/views_model.joblib")

def predict_views(likes: float, retweets: float) -> float:
    likes = max(0.0, float(likes))
    retweets = max(0.0, float(retweets))
    row = pd.DataFrame([{
        "likes_log": math.log1p(likes),
        "retweets_log": math.log1p(retweets),
        "retweets_zero": 1 if retweets == 0 else 0,
        "like_rt_interaction": math.log1p(likes) * math.log1p(retweets),
    }])
    pred_log = float(_model.predict(row)[0])
    return max(0.0, math.expm1(pred_log))

if __name__ == "__main__":
    examples = [(8, 0), (26, 1), (87, 2), (949, 34)]
    for l, r in examples:
        print(f"likes={l:>4}, retweets={r:>3} -> pred_views={predict_views(l, r):.0f}")
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_standalone_predictor_script(model: Pipeline, path: Path) -> None:
    pre = model.named_steps["pre"]
    num_pipe = pre.named_transformers_["num"]
    scaler = num_pipe.named_steps["scaler"]
    reg = model.named_steps["reg"]

    if not hasattr(reg, "coef_") or not hasattr(reg, "intercept_"):
        raise RuntimeError(
            "Standalone export requires a linear regressor with coef_/intercept_. "
            f"Got: {type(reg).__name__}"
        )

    means = [float(x) for x in scaler.mean_.tolist()]
    scales = [float(x) for x in scaler.scale_.tolist()]
    coefs = [float(x) for x in reg.coef_.tolist()]
    intercept = float(reg.intercept_)

    content = f"""import math

# Auto-generated standalone implementation of the trained model.
# No joblib, pandas, or sklearn needed at inference time.

# Feature order:
# 0: likes_log = log1p(likes)
# 1: retweets_log = log1p(retweets)
# 2: retweets_zero = 1 if retweets == 0 else 0
# 3: like_rt_interaction = likes_log * retweets_log

MEANS = {means}
SCALES = {scales}
COEFS = {coefs}
INTERCEPT = {intercept}


def _build_features(likes: float, retweets: float) -> list[float]:
    likes = max(0.0, float(likes))
    retweets = max(0.0, float(retweets))
    likes_log = math.log1p(likes)
    retweets_log = math.log1p(retweets)
    retweets_zero = 1.0 if retweets == 0 else 0.0
    like_rt_interaction = likes_log * retweets_log
    return [likes_log, retweets_log, retweets_zero, like_rt_interaction]


def predict_views(likes: float, retweets: float) -> float:
    x = _build_features(likes, retweets)
    z = [(x[i] - MEANS[i]) / SCALES[i] for i in range(4)]
    y_log = INTERCEPT + sum(COEFS[i] * z[i] for i in range(4))
    return max(0.0, math.expm1(y_log))


if __name__ == "__main__":
    examples = [(8, 0), (26, 1), (87, 2), (949, 34)]
    for likes, retweets in examples:
        pred = predict_views(likes, retweets)
        print(f"likes={{likes:>4}}, retweets={{retweets:>3}} -> pred_views={{pred:.0f}}")
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    data_dir = root / "data" / "twitter_scraps"
    out_dir = root / "outputs"

    raw = read_scrapes(data_dir)
    df = dedupe_latest(raw)
    df = add_features(df)

    results, best = evaluate_models(df)
    final_model = fit_final(df, best)

    out_dir.mkdir(parents=True, exist_ok=True)
    results.to_csv(out_dir / "views_model_results.csv", index=False)
    joblib.dump(final_model, out_dir / "views_model.joblib")
    diagnostic_plot(df, final_model, out_dir / "pred_vs_actual_views.png")
    feature_overlay_plots(df, final_model, out_dir)
    write_report(df, results, best, out_dir / "views_model_report.md")
    write_predictor_script(out_dir / "predict_views.py")
    write_standalone_predictor_script(final_model, out_dir / "predict_views_standalone.py")

    print(f"Rows used: {len(df)}")
    print("Model ranking:")
    print(results.to_string(index=False))
    print(f"Best model: {best}")
    print("Wrote:")
    print(f"- {out_dir / 'views_model_results.csv'}")
    print(f"- {out_dir / 'views_model.joblib'}")
    print(f"- {out_dir / 'pred_vs_actual_views.png'}")
    print(f"- {out_dir / 'model_vs_likes_with_actual.png'}")
    print(f"- {out_dir / 'model_vs_retweets_with_actual.png'}")
    print(f"- {out_dir / 'views_model_report.md'}")
    print(f"- {out_dir / 'predict_views.py'}")
    print(f"- {out_dir / 'predict_views_standalone.py'}")


if __name__ == "__main__":
    main()

