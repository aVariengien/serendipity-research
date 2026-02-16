from __future__ import annotations

import json
import math
import random
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


SEED = 42
random.seed(SEED)
np.random.seed(SEED)


@dataclass
class Config:
    base_url: str = (
        "https://fabxmporizzqflnftavs.supabase.co/storage/v1/object/public"
        "/firehose/mapped_data"
    )
    start_date: date = date(2025, 8, 1)
    end_date: date = date(2025, 8, 12)
    part_range: range = range(0, 12)
    timeout: int = 25
    max_downloads: int = 40
    sample_for_scatter: int = 25000
    splits: int = 6
    test_size: float = 0.2


def safe_int(x: Any) -> float:
    if x is None:
        return np.nan
    if isinstance(x, bool):
        return int(x)
    if isinstance(x, (int, np.integer)):
        return float(x)
    if isinstance(x, float):
        if math.isnan(x):
            return np.nan
        return float(x)
    if isinstance(x, str):
        s = x.strip().replace(",", "")
        if not s:
            return np.nan
        try:
            return float(s)
        except ValueError:
            return np.nan
    return np.nan


def date_range(start: date, end: date) -> list[date]:
    d = start
    out: list[date] = []
    while d <= end:
        out.append(d)
        d += timedelta(days=1)
    return out


def build_candidate_urls(cfg: Config) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    for d in date_range(cfg.start_date, cfg.end_date):
        dstr = d.isoformat()
        for part in cfg.part_range:
            fn = f"{dstr}_mapped_part_{part:06d}.parquet"
            rel = f"{dstr}/{fn}"
            candidates.append((f"{cfg.base_url}/{rel}", rel))
    return candidates


def download_files(cfg: Config, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    downloaded: list[Path] = []
    for url, rel in build_candidate_urls(cfg):
        local = out_dir / rel.replace("/", "__")
        if local.exists() and local.stat().st_size > 0:
            downloaded.append(local)
            continue
        try:
            resp = requests.get(url, stream=True, timeout=cfg.timeout)
            if resp.status_code != 200:
                continue
            with local.open("wb") as f:
                for chunk in resp.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            downloaded.append(local)
            print(f"Downloaded: {rel} ({local.stat().st_size / 1e6:.2f} MB)")
            if len(downloaded) >= cfg.max_downloads:
                break
        except requests.RequestException:
            continue
    print(f"Total parquet files available locally: {len(downloaded)}")
    return downloaded


def pick_col(columns: list[str], options: list[str]) -> str | None:
    lowered = {c.lower(): c for c in columns}
    for opt in options:
        if opt.lower() in lowered:
            return lowered[opt.lower()]
    return None


def from_json_payload(payload: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    if payload is None:
        return out

    obj = None
    if isinstance(payload, str):
        try:
            parsed = json.loads(payload)
            if isinstance(parsed, list) and parsed:
                obj = parsed[0]
            elif isinstance(parsed, dict):
                obj = parsed
        except Exception:
            return out
    elif isinstance(payload, list) and payload:
        obj = payload[0]
    elif isinstance(payload, dict):
        obj = payload

    if not isinstance(obj, dict):
        return out

    tweet = obj.get("tweet", {}) if isinstance(obj.get("tweet"), dict) else {}
    account = obj.get("account", {}) if isinstance(obj.get("account"), dict) else {}

    out["tweet_id"] = tweet.get("tweet_id") or tweet.get("id")
    out["created_at"] = tweet.get("created_at")
    out["retweet_count"] = safe_int(tweet.get("retweet_count"))
    out["favorite_count"] = safe_int(tweet.get("favorite_count"))
    out["reply_count"] = safe_int(tweet.get("reply_count"))
    out["quote_count"] = safe_int(tweet.get("quote_count"))
    out["bookmark_count"] = safe_int(tweet.get("bookmark_count"))
    out["view_count"] = safe_int(
        tweet.get("view_count")
        or tweet.get("views")
        or tweet.get("impression_count")
        or tweet.get("impressions")
    )
    out["followers"] = safe_int(account.get("followers"))
    out["following"] = safe_int(account.get("following"))
    out["num_tweets"] = safe_int(account.get("num_tweets"))
    out["account_likes"] = safe_int(account.get("likes"))
    out["created_via"] = account.get("created_via")
    return out


def extract_records(df: pd.DataFrame) -> pd.DataFrame:
    cols = list(df.columns)
    payload_col = pick_col(cols, ["data", "payload", "tweet_json", "json"])

    target_col = pick_col(
        cols, ["view_count", "views", "impression_count", "impressions", "viewcount"]
    )
    likes_col = pick_col(cols, ["favorite_count", "likes", "like_count"])
    rts_col = pick_col(cols, ["retweet_count", "retweets", "retweet"])
    replies_col = pick_col(cols, ["reply_count", "replies"])
    quotes_col = pick_col(cols, ["quote_count", "quotes"])
    followers_col = pick_col(cols, ["followers", "follower_count"])
    following_col = pick_col(cols, ["following", "following_count"])

    records: list[dict[str, Any]] = []
    if payload_col is not None:
        for payload in df[payload_col].tolist():
            rec = from_json_payload(payload)
            if rec:
                records.append(rec)
    else:
        rec = pd.DataFrame(
            {
                "view_count": df[target_col] if target_col else np.nan,
                "favorite_count": df[likes_col] if likes_col else np.nan,
                "retweet_count": df[rts_col] if rts_col else np.nan,
                "reply_count": df[replies_col] if replies_col else np.nan,
                "quote_count": df[quotes_col] if quotes_col else np.nan,
                "followers": df[followers_col] if followers_col else np.nan,
                "following": df[following_col] if following_col else np.nan,
            }
        )
        records = rec.to_dict(orient="records")

    out = pd.DataFrame.from_records(records)
    if out.empty:
        return out

    numeric_cols = [
        "view_count",
        "favorite_count",
        "retweet_count",
        "reply_count",
        "quote_count",
        "bookmark_count",
        "followers",
        "following",
        "num_tweets",
        "account_likes",
    ]
    for c in numeric_cols:
        if c in out.columns:
            out[c] = out[c].apply(safe_int)
        else:
            out[c] = np.nan

    if "created_at" in out.columns:
        out["created_at"] = pd.to_datetime(out["created_at"], errors="coerce", utc=True)
        out["hour"] = out["created_at"].dt.hour
        out["dow"] = out["created_at"].dt.dayofweek
    else:
        out["hour"] = np.nan
        out["dow"] = np.nan

    out = out[out["view_count"].notna()]
    out = out[out["view_count"] > 0]
    return out


def build_model(name: str) -> Pipeline:
    num_cols = [
        "favorite_count",
        "retweet_count",
        "reply_count",
        "quote_count",
        "bookmark_count",
        "followers",
        "following",
        "num_tweets",
        "account_likes",
        "hour",
        "dow",
        "engagement_total",
        "engagement_rate_proxy",
        "favorite_to_retweet_ratio",
        "log_favorite_count",
        "log_retweet_count",
        "log_followers",
    ]
    cat_cols = ["created_via"]

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
                num_cols,
            ),
            (
                "cat",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                cat_cols,
            ),
        ],
        remainder="drop",
    )

    if name == "linear":
        reg = LinearRegression()
    elif name == "ridge":
        reg = Ridge(alpha=2.0, random_state=SEED)
    elif name == "random_forest":
        reg = RandomForestRegressor(
            n_estimators=220, max_depth=20, n_jobs=-1, random_state=SEED
        )
    elif name == "gradient_boosting":
        reg = GradientBoostingRegressor(random_state=SEED)
    else:
        raise ValueError(f"Unknown model: {name}")

    return Pipeline(steps=[("preprocess", pre), ("regressor", reg)])


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    x = df.copy()
    x["engagement_total"] = (
        x["favorite_count"].fillna(0)
        + x["retweet_count"].fillna(0)
        + x["reply_count"].fillna(0)
        + x["quote_count"].fillna(0)
        + x["bookmark_count"].fillna(0)
    )
    x["engagement_rate_proxy"] = x["engagement_total"] / x["view_count"].clip(lower=1)
    x["favorite_to_retweet_ratio"] = x["favorite_count"] / x["retweet_count"].replace(
        {0: np.nan}
    )
    x["favorite_to_retweet_ratio"] = x["favorite_to_retweet_ratio"].replace(
        [np.inf, -np.inf], np.nan
    )
    x["log_favorite_count"] = np.log1p(x["favorite_count"].clip(lower=0))
    x["log_retweet_count"] = np.log1p(x["retweet_count"].clip(lower=0))
    x["log_followers"] = np.log1p(x["followers"].clip(lower=0))
    x["log_view_count"] = np.log1p(x["view_count"].clip(lower=0))
    return x


def evaluate_models(df: pd.DataFrame) -> tuple[pd.DataFrame, str, pd.DataFrame]:
    model_names = ["linear", "ridge", "gradient_boosting", "random_forest"]
    splitter = ShuffleSplit(
        n_splits=Config().splits, test_size=Config().test_size, random_state=SEED
    )

    results: list[dict[str, Any]] = []
    preds_for_best: list[pd.DataFrame] = []
    best_name = None
    best_rmse = float("inf")

    for name in model_names:
        fold_metrics: list[dict[str, float]] = []
        fold_pred_frames: list[pd.DataFrame] = []
        for fold_i, (train_idx, test_idx) in enumerate(splitter.split(df), start=1):
            train_df = df.iloc[train_idx].copy()
            test_df = df.iloc[test_idx].copy()

            y_train = train_df["log_view_count"]
            y_test = test_df["log_view_count"]
            x_train = train_df.drop(columns=["view_count", "log_view_count"])
            x_test = test_df.drop(columns=["view_count", "log_view_count"])

            model = build_model(name)
            model.fit(x_train, y_train)
            pred_log = model.predict(x_test)

            rmse_log = math.sqrt(mean_squared_error(y_test, pred_log))
            mae_log = mean_absolute_error(y_test, pred_log)
            r2_log = r2_score(y_test, pred_log)

            y_test_raw = np.expm1(y_test)
            pred_raw = np.expm1(pred_log)
            rmse_raw = math.sqrt(mean_squared_error(y_test_raw, pred_raw))
            mae_raw = mean_absolute_error(y_test_raw, pred_raw)
            r2_raw = r2_score(y_test_raw, pred_raw)

            fold_metrics.append(
                {
                    "model": name,
                    "fold": fold_i,
                    "rmse_log": rmse_log,
                    "mae_log": mae_log,
                    "r2_log": r2_log,
                    "rmse_raw": rmse_raw,
                    "mae_raw": mae_raw,
                    "r2_raw": r2_raw,
                }
            )

            fold_pred_frames.append(
                pd.DataFrame(
                    {
                        "actual_views": y_test_raw,
                        "pred_views": pred_raw,
                        "model": name,
                        "fold": fold_i,
                    }
                )
            )

        fold_df = pd.DataFrame(fold_metrics)
        summary = {
            "model": name,
            "rmse_log_mean": fold_df["rmse_log"].mean(),
            "rmse_log_std": fold_df["rmse_log"].std(ddof=1),
            "mae_log_mean": fold_df["mae_log"].mean(),
            "r2_log_mean": fold_df["r2_log"].mean(),
            "rmse_raw_mean": fold_df["rmse_raw"].mean(),
            "mae_raw_mean": fold_df["mae_raw"].mean(),
            "r2_raw_mean": fold_df["r2_raw"].mean(),
        }
        results.append(summary)

        if summary["rmse_log_mean"] < best_rmse:
            best_rmse = summary["rmse_log_mean"]
            best_name = name
            preds_for_best = fold_pred_frames

    res_df = pd.DataFrame(results).sort_values("rmse_log_mean").reset_index(drop=True)
    preds_df = pd.concat(preds_for_best, ignore_index=True) if preds_for_best else pd.DataFrame()
    return res_df, best_name or "linear", preds_df


def make_plots(df: pd.DataFrame, preds_df: pd.DataFrame, out_dir: Path, cfg: Config) -> list[str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    files: list[str] = []
    sns.set_theme(style="whitegrid")

    # 1) Views distribution
    fig, ax = plt.subplots(figsize=(8.5, 5))
    sns.histplot(np.log1p(df["view_count"]), bins=60, ax=ax, color="#3b82f6")
    ax.set_title("Distribution of log(1 + view_count)")
    ax.set_xlabel("log(1 + view_count)")
    ax.set_ylabel("Count")
    p1 = out_dir / "plot_01_view_distribution.png"
    fig.tight_layout()
    fig.savefig(p1, dpi=150)
    plt.close(fig)
    files.append(str(p1.name))

    # 2) Likes vs Views
    plot_df = df.sample(min(cfg.sample_for_scatter, len(df)), random_state=SEED)
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    sns.scatterplot(
        data=plot_df,
        x="favorite_count",
        y="view_count",
        alpha=0.15,
        s=10,
        ax=ax,
        color="#0ea5e9",
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Views vs Likes (log-log)")
    ax.set_xlabel("favorite_count")
    ax.set_ylabel("view_count")
    p2 = out_dir / "plot_02_views_vs_likes.png"
    fig.tight_layout()
    fig.savefig(p2, dpi=150)
    plt.close(fig)
    files.append(str(p2.name))

    # 3) Retweets vs Views
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    sns.scatterplot(
        data=plot_df,
        x="retweet_count",
        y="view_count",
        alpha=0.15,
        s=10,
        ax=ax,
        color="#14b8a6",
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Views vs Retweets (log-log)")
    ax.set_xlabel("retweet_count")
    ax.set_ylabel("view_count")
    p3 = out_dir / "plot_03_views_vs_retweets.png"
    fig.tight_layout()
    fig.savefig(p3, dpi=150)
    plt.close(fig)
    files.append(str(p3.name))

    # 4) Correlation heatmap
    corr_cols = [
        "view_count",
        "favorite_count",
        "retweet_count",
        "reply_count",
        "quote_count",
        "bookmark_count",
        "followers",
        "engagement_total",
        "favorite_to_retweet_ratio",
    ]
    corr_df = df[corr_cols].copy()
    corr = corr_df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, cmap="coolwarm", center=0, annot=True, fmt=".2f", ax=ax)
    ax.set_title("Correlation matrix")
    p4 = out_dir / "plot_04_correlation_heatmap.png"
    fig.tight_layout()
    fig.savefig(p4, dpi=150)
    plt.close(fig)
    files.append(str(p4.name))

    # 5) Prediction vs actual
    if not preds_df.empty:
        pred_plot_df = preds_df.sample(min(20000, len(preds_df)), random_state=SEED)
        fig, ax = plt.subplots(figsize=(8.5, 5.5))
        sns.scatterplot(
            data=pred_plot_df,
            x="actual_views",
            y="pred_views",
            alpha=0.2,
            s=10,
            ax=ax,
            color="#f97316",
        )
        both = pd.concat([pred_plot_df["actual_views"], pred_plot_df["pred_views"]])
        min_v, max_v = float(both.min()), float(both.max())
        ax.plot([min_v, max_v], [min_v, max_v], linestyle="--", color="black", linewidth=1)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title("Predicted vs Actual Views (best model)")
        ax.set_xlabel("Actual views")
        ax.set_ylabel("Predicted views")
        p5 = out_dir / "plot_05_pred_vs_actual.png"
        fig.tight_layout()
        fig.savefig(p5, dpi=150)
        plt.close(fig)
        files.append(str(p5.name))

    return files


def write_report(
    out_path: Path,
    df: pd.DataFrame,
    files_downloaded: list[Path],
    model_results: pd.DataFrame,
    best_model: str,
    plot_files: list[str],
) -> None:
    n_rows = len(df)
    n_files = len(files_downloaded)
    dates = sorted({f.name.split("__")[0] for f in files_downloaded})
    date_span = f"{dates[0]} to {dates[-1]}" if dates else "N/A"

    desc = df[
        [
            "view_count",
            "favorite_count",
            "retweet_count",
            "reply_count",
            "quote_count",
            "followers",
            "engagement_total",
        ]
    ].describe(percentiles=[0.5, 0.9, 0.95, 0.99]).T

    model_table = model_results.copy()
    model_table = model_table[
        [
            "model",
            "rmse_log_mean",
            "rmse_log_std",
            "mae_log_mean",
            "r2_log_mean",
            "rmse_raw_mean",
            "mae_raw_mean",
            "r2_raw_mean",
        ]
    ]

    lines: list[str] = []
    lines.append("# Tweet Views Modeling Report")
    lines.append("")
    lines.append("## 1) Goal")
    lines.append("")
    lines.append(
        "Estimate tweet view count from engagement features (likes, retweets, replies, "
        "quotes, bookmarks) plus a few account/context features."
    )
    lines.append("")
    lines.append("## 2) Data Collected")
    lines.append("")
    lines.append(f"- Parquet files downloaded/used: **{n_files}**")
    lines.append(f"- Date span covered: **{date_span}**")
    lines.append(f"- Rows with usable target (`view_count > 0`): **{n_rows:,}**")
    lines.append("- Input source: Supabase public storage (`firehose/mapped_data/...`).")
    lines.append("")
    lines.append("## 3) Feature Set")
    lines.append("")
    lines.append("- Core engagement: `favorite_count`, `retweet_count`, `reply_count`, `quote_count`, `bookmark_count`")
    lines.append("- Account/context: `followers`, `following`, `num_tweets`, `account_likes`, `created_via`, `hour`, `dow`")
    lines.append("- Engineered: `engagement_total`, `engagement_rate_proxy`, `favorite_to_retweet_ratio`, plus log transforms")
    lines.append("- Target: `view_count` (modeled in log-space as `log1p(view_count)`).")
    lines.append("")
    lines.append("## 4) Data Snapshot")
    lines.append("")
    lines.append(desc.to_markdown(floatfmt=".4f"))
    lines.append("")
    lines.append("## 5) EDA Plots")
    lines.append("")
    for pf in plot_files:
        lines.append(f"![{pf}](plots/{pf})")
        lines.append("")
    lines.append("## 6) Modeling Approach")
    lines.append("")
    lines.append("- Train/test strategy: **ShuffleSplit** (random shuffling), 6 splits, 80/20 each.")
    lines.append("- Models trained:")
    lines.append("  - Linear Regression")
    lines.append("  - Ridge Regression")
    lines.append("  - Gradient Boosting Regressor")
    lines.append("  - Random Forest Regressor")
    lines.append("- Preprocessing:")
    lines.append("  - Numeric: median imputation + scaling")
    lines.append("  - Categorical: one-hot encoding (`created_via`)")
    lines.append("- Primary selection metric: mean RMSE in log-space (`rmse_log_mean`).")
    lines.append("")
    lines.append("## 7) Model Results")
    lines.append("")
    lines.append(model_table.to_markdown(index=False, floatfmt=".5f"))
    lines.append("")
    lines.append("## 8) Selected Model")
    lines.append("")
    lines.append(f"**Best model: `{best_model}`** (lowest average log-space RMSE across shuffled splits).")
    lines.append("")
    lines.append("### Practical Notes")
    lines.append("")
    lines.append("- Engagement counts (especially likes and retweets) are strongly associated with views.")
    lines.append("- Relationship is heavy-tailed; log-space modeling stabilizes training and evaluation.")
    lines.append("- Even simple models work reasonably; tree models generally improve non-linear fit.")
    lines.append("- Prediction error in raw view units remains large on viral outliers, which is expected.")
    lines.append("")
    lines.append("## 9) What I’d Do Next (If Needed)")
    lines.append("")
    lines.append("- Add more days/parts for broader coverage and less drift sensitivity.")
    lines.append("- Calibrate separate models by account-size bucket (small/medium/large follower counts).")
    lines.append("- Add robust interval predictions (quantile regression) for uncertainty bands.")
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cfg = Config()
    base_dir = Path(__file__).resolve().parent
    raw_dir = base_dir / "data" / "raw"
    out_dir = base_dir / "outputs"
    plot_dir = out_dir / "plots"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("1) Downloading parquet files...")
    files = download_files(cfg, raw_dir)
    if not files:
        raise RuntimeError("No parquet files found/downloaded. Check URL access.")

    print("2) Reading and extracting usable rows...")
    all_rows: list[pd.DataFrame] = []
    for fp in files:
        try:
            part = pd.read_parquet(fp)
            rec = extract_records(part)
            if not rec.empty:
                all_rows.append(rec)
        except Exception:
            continue
    if not all_rows:
        raise RuntimeError("Could not extract usable rows with view_count from downloaded data.")

    df = pd.concat(all_rows, ignore_index=True)
    df = df.drop_duplicates(subset=["tweet_id"], keep="first") if "tweet_id" in df.columns else df
    df = add_features(df)
    df = df[df["view_count"].notna() & (df["view_count"] > 0)].copy()
    if len(df) < 300:
        raise RuntimeError(f"Too few training rows after filtering: {len(df)}")

    print(f"Usable rows: {len(df):,}")

    print("3) Training/evaluating models...")
    model_results, best_model, preds_df = evaluate_models(df)
    model_results.to_csv(out_dir / "model_results.csv", index=False)

    print("4) Creating plots...")
    plots = make_plots(df, preds_df, plot_dir, cfg)

    print("5) Writing markdown report...")
    write_report(
        out_path=out_dir / "tweet_views_model_report.md",
        df=df,
        files_downloaded=files,
        model_results=model_results,
        best_model=best_model,
        plot_files=plots,
    )

    print("Done.")
    print(f"- Report: {out_dir / 'tweet_views_model_report.md'}")
    print(f"- Metrics: {out_dir / 'model_results.csv'}")
    print(f"- Plots:   {plot_dir}")


if __name__ == "__main__":
    main()
