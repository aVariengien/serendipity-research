"""Streamlit app for visualizing simulation output."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any, cast

import networkx as nx
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network

from run import run_batch


APP_DEFAULT_SIZES = [5, 10, 20, 40, 80, 160, 320, 640, 1280]
DEFAULT_RUN_PATH = Path(__file__).parent / "default_run.json"


def build_run_dataframe(payload: dict) -> pd.DataFrame:
    rows = []
    for run in payload.get("runs", []):
        summary = run.get("summary", {})
        degree_values = [float(v) for v in run.get("network", {}).get("degrees", {}).values()]
        mean_degree = float(np.mean(degree_values)) if degree_values else 0.0
        rows.append(
            {
                "network_size": run["network_size"],
                "matchmaking": run["matchmaking"],
                "seed": run["seed"],
                "mean_degree": mean_degree,
                "mean_events_per_user_per_week": summary.get(
                    "mean_events_per_user_per_week", 0.0
                ),
                "solve_rate": summary.get("solve_rate", 0.0),
                "total_problems": summary.get("total_problems", 0),
                "total_solved": summary.get("total_solved", 0),
            }
        )
    return pd.DataFrame(rows)


def render_pyvis_graph(run: dict) -> None:
    network_data = run["network"]
    edges = [tuple(edge) for edge in network_data["edges"]]
    degrees = {int(k): int(v) for k, v in network_data["degrees"].items()}

    per_user_events = {}
    for user_id, event_data in run["user_events"].items():
        per_user_events[int(user_id)] = event_data["total"]

    days = run["parameters"]["days"]
    weeks = max(days / 7.0, 1e-9)

    graph = nx.Graph()
    graph.add_edges_from(edges)
    for node in degrees:
        if node not in graph:
            graph.add_node(node)

    values = np.array(list(per_user_events.values()), dtype=float)
    v_min = float(values.min()) if len(values) else 0.0
    v_max = float(values.max()) if len(values) else 1.0

    net = Network(height="700px", width="100%", notebook=False)
    net.from_nx(graph)

    for node in net.nodes:
        node_dict = cast(dict[str, Any], node)
        node_id = int(node_dict["id"])
        event_total = per_user_events.get(node_id, 0.0)
        event_rate = event_total / weeks
        deg = degrees.get(node_id, 0)

        norm = 0.0 if v_max == v_min else (event_total - v_min) / (v_max - v_min)
        red = int(255 * norm)
        blue = int(255 * (1 - norm))
        color = f"rgb({red},60,{blue})"

        node_dict["value"] = max(5, deg + 3)
        node_dict["color"] = color
        node_dict["title"] = (
            f"User {node_id}<br>"
            f"Degree: {deg}<br>"
            f"Total events: {event_total:.2f}<br>"
            f"Events/week: {event_rate:.2f}"
        )

    net.force_atlas_2based(gravity=-50)

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as temp_html:
        net.save_graph(temp_html.name)
        html = Path(temp_html.name).read_text(encoding="utf-8")

    components.html(html, height=720, scrolling=True)


def build_user_table(run: dict) -> pd.DataFrame:
    days = run["parameters"]["days"]
    weeks = max(days / 7.0, 1e-9)
    degrees = {int(k): int(v) for k, v in run["network"]["degrees"].items()}
    rows = []
    for user_id, events in run["user_events"].items():
        uid = int(user_id)
        total = float(events["total"])
        rows.append(
            {
                "user": uid,
                "degree": degrees.get(uid, 0),
                "as_holder": float(events["as_holder"]),
                "as_solver": float(events["as_solver"]),
                "as_matchmaker": float(events["as_matchmaker"]),
                "total_events": total,
                "events_per_week": total / weeks,
            }
        )
    return pd.DataFrame(rows).sort_values("events_per_week", ascending=False)


def build_degree_rank_table(run: dict) -> pd.DataFrame:
    """Return degree rank table for plotting log(degree) vs node order."""
    degrees = [int(v) for v in run.get("network", {}).get("degrees", {}).values()]
    if not degrees:
        return pd.DataFrame(columns=["order", "degree", "log10_degree"])

    degrees_sorted = sorted(degrees, reverse=True)
    rows = []
    for idx, degree in enumerate(degrees_sorted, start=1):
        rows.append(
            {
                "order": idx,
                "degree": degree,
                "log10_degree": float(np.log10(max(degree, 1))),
            }
        )
    return pd.DataFrame(rows)


def build_resolve_rate_by_degree(run: dict, n_buckets: int = 8) -> pd.DataFrame:
    """Bucket users by degree and compute resolve rate per bucket.

    Uses actual per-user ``problems_generated`` when available (new runs),
    falls back to the expected value ``problems_per_day * days`` for older
    result files that lack this field.
    """
    degrees = {int(k): int(v) for k, v in run["network"]["degrees"].items()}
    days = run["parameters"]["days"]
    problems_per_day = run["parameters"]["problems_per_day"]
    fallback_problems = days * problems_per_day

    rows = []
    for uid_str, events in run["user_events"].items():
        uid = int(uid_str)
        problems = events.get("problems_generated")
        if problems is None:
            problems = fallback_problems
        rows.append(
            {
                "degree": degrees.get(uid, 0),
                "as_holder": float(events["as_holder"]),
                "problems_generated": float(problems),
            }
        )
    if not rows:
        return pd.DataFrame(
            columns=["degree_bucket", "node_count", "resolve_rate"]
        )

    df = pd.DataFrame(rows)
    deg_min = int(df["degree"].min())
    deg_max = int(df["degree"].max())

    if deg_max == deg_min:
        boundaries = [deg_min, deg_max + 1]
    else:
        boundaries = np.linspace(deg_min, deg_max + 1, n_buckets + 1).astype(int)
        boundaries = sorted(set(boundaries))

    labels = []
    for i in range(len(boundaries) - 1):
        lo = boundaries[i]
        hi = boundaries[i + 1] - 1
        labels.append(f"{lo}-{hi}" if lo != hi else str(lo))

    df["bucket"] = pd.cut(
        df["degree"],
        bins=[float(b) for b in boundaries],
        labels=labels,
        include_lowest=True,
        right=False,
    )

    agg = df.groupby("bucket", observed=False).agg(
        node_count=("degree", "size"),
        solved_sum=("as_holder", "sum"),
        problems_sum=("problems_generated", "sum"),
    )
    agg["resolve_rate"] = np.where(
        agg["problems_sum"] > 0, agg["solved_sum"] / agg["problems_sum"], 0.0
    )
    agg = agg.reset_index().rename(columns={"bucket": "degree_bucket"})
    return agg


def main() -> None:
    st.set_page_config(page_title="Social Matching Simulation", layout="wide")
    st.title("Social Network Problem-Opportunity Matching")

    st.sidebar.header("Simulation Controls")
    sim_name = st.sidebar.text_input("Simulation name", value="Top 50 CA users Twitter base rate")
    sim_problems_per_day_text = st.sidebar.text_input(
        "Problems per user per day (pb/day, mean)", value="0.7"
    )
    sim_match_probability_text = st.sidebar.text_input(
        "Solve probability per candidate", value="0.000051"
    )
    sim_small_network_degree_percent = st.sidebar.slider(
        "Small-network degree percent (P)",
        min_value=1,
        max_value=100,
        value=20,
        step=1,
        help="Target average degree starts as int(n * P/100).",
    )
    sim_large_network_degree_cap = st.sidebar.slider(
        "Large-network avg degree cap (K)",
        min_value=5,
        max_value=100,
        value=20,
        step=1,
        help="When int(n * P/100) exceeds K, target degree is capped at K.",
    )
    st.sidebar.caption(
        "Per network size n: target average degree = min(int(n * P/100), K)."
    )
    with st.sidebar.expander("Advanced run settings"):
        sim_days_text = st.text_input("Days", value="28")
        sim_seeds_per_config = st.number_input(
            "Seeds per configuration",
            min_value=1,
            max_value=100,
            value=1,
            step=1,
        )
        sim_sizes_text = st.text_input(
            "Network sizes (comma-separated, max 2000)",
            value=", ".join(str(x) for x in APP_DEFAULT_SIZES),
        )
        sim_base_seed = st.number_input(
            "Base seed", min_value=0, max_value=2**31 - 1, value=42, step=1
        )
        sim_disable_triadic_closure = st.checkbox(
            "Disable triadic closure",
            value=False,
            help="If enabled, skips friend-of-friend edge additions in large-network generation.",
        )

    st.markdown(
        "Run a simulation and explore the network and outcome charts."
    )
    run_clicked = st.button("Run simulation", type="primary")
    if run_clicked:
        errors: list[str] = []
        sim_name_clean = sim_name.strip() or "unnamed_simulation"

        try:
            sim_problems_per_day = float(sim_problems_per_day_text.strip())
            if sim_problems_per_day < 0:
                errors.append("Problems per user per day must be >= 0.")
        except ValueError:
            errors.append("Problems per user per day must be a number.")

        try:
            sim_days = int(sim_days_text.strip())
            if sim_days < 1:
                errors.append("Days must be >= 1.")
        except ValueError:
            errors.append("Days must be an integer.")

        try:
            sim_match_probability = float(sim_match_probability_text.strip())
            if not 0.0 <= sim_match_probability <= 1.0:
                errors.append("Solve probability per candidate must be between 0 and 1.")
        except ValueError:
            errors.append("Solve probability per candidate must be a number.")

        sim_sizes: list[int] = []
        raw_sizes = [token.strip() for token in sim_sizes_text.split(",") if token.strip()]
        if not raw_sizes:
            errors.append("Provide at least one network size.")
        else:
            for token in raw_sizes:
                try:
                    size = int(token)
                except ValueError:
                    errors.append(f"Invalid network size '{token}' (must be an integer).")
                    continue

                if size < 2 or size > 2000:
                    errors.append(f"Network size {size} is out of range (2..2000).")
                    continue

                sim_sizes.append(size)

            if sim_sizes:
                sim_sizes = sorted(set(sim_sizes))

        if errors:
            for error in errors:
                st.sidebar.error(error)
        else:
            progress_bar = st.progress(0, text="Running simulations...")

            def _update_progress(completed: int, total: int, size: int) -> None:
                frac = completed / max(total, 1)
                progress_bar.progress(
                    frac, text=f"Running simulations... n={size}  ({completed}/{total})"
                )

            payload = run_batch(
                days=int(sim_days),
                problems_per_day=float(sim_problems_per_day),
                match_probability=float(sim_match_probability),
                matchmaker_credit=0.5,
                seeds_per_config=int(sim_seeds_per_config),
                sizes=[int(x) for x in sim_sizes],
                base_seed=int(sim_base_seed),
                small_network_degree_fraction=(
                    float(sim_small_network_degree_percent) / 100.0
                ),
                max_target_avg_degree=float(sim_large_network_degree_cap),
                enable_triadic_closure=not sim_disable_triadic_closure,
                progress_callback=_update_progress,
            )
            progress_bar.empty()
            payload["simulation_name"] = sim_name_clean
            st.session_state["simulation_payload"] = payload
            st.sidebar.success(f"Simulation '{sim_name_clean}' complete!")
            st.rerun()

    payload = st.session_state.get("simulation_payload")
    if payload is None:
        if DEFAULT_RUN_PATH.exists():
            payload = json.loads(DEFAULT_RUN_PATH.read_text(encoding="utf-8"))
            st.session_state["simulation_payload"] = payload
            st.info(
                "Showing pre-computed default results. "
                "Adjust settings in the sidebar and click **Run simulation** to run your own."
            )
        else:
            st.info(
                "Welcome! "
                "Configure your settings in the sidebar and click 'Run simulation' to begin."
            )
            return

    runs_df = build_run_dataframe(payload)
    if runs_df.empty:
        st.warning("No runs found in the results file.")
        return

    sim_header = payload.get("simulation_name", "Unnamed simulation")
    st.header(f"Simulation: {sim_header}")

    st.sidebar.header("Filters")
    sizes = sorted(runs_df["network_size"].unique().tolist())
    match_modes = [False, True]
    selected_size = st.sidebar.selectbox(
        "Network size", options=sizes, index=max(len(sizes) - 1, 0)
    )
    selected_matchmaking = st.sidebar.selectbox(
        "Matchmaking",
        options=match_modes,
        format_func=lambda x: "Enabled" if x else "Disabled",
        index=0,
    )
    eligible_seeds = sorted(
        runs_df[
            (runs_df["network_size"] == selected_size)
            & (runs_df["matchmaking"] == selected_matchmaking)
        ]["seed"].unique()
    )
    selected_seed = st.sidebar.selectbox("Seed", options=eligible_seeds, index=0)

    selected_run = None
    for run in payload["runs"]:
        if (
            run["network_size"] == selected_size
            and run["matchmaking"] == selected_matchmaking
            and run["seed"] == selected_seed
        ):
            selected_run = run
            break

    st.subheader("Critical Mass Analysis")
    mode_labels = {False: "No matchmaking", True: "With matchmaking"}
    mode_order = ["No matchmaking", "With matchmaking"]
    mode_colors = {
        "No matchmaking": "#8EC5FF",  # light blue
        "With matchmaking": "#0B3D91",  # dark blue
    }
    grouped = (
        runs_df.groupby(["network_size", "matchmaking"])["mean_events_per_user_per_week"]
        .agg(["mean", "std"])
        .reset_index()
    )
    grouped["mode"] = grouped["matchmaking"].map(mode_labels)
    runs_df["mode"] = runs_df["matchmaking"].map(mode_labels)

    fig = px.line(
        grouped,
        x="network_size",
        y="mean",
        color="mode",
        markers=True,
        category_orders={"mode": mode_order},
        color_discrete_map=mode_colors,
        labels={
            "network_size": "Network size",
            "mean": "Mean events/user/week",
            "mode": "Mode",
        },
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Observed Mean Degree by Network Size")
    degree_grouped = (
        runs_df.groupby("network_size")["mean_degree"].agg(["mean", "std"]).reset_index()
    )
    degree_fig = px.line(
        degree_grouped,
        x="network_size",
        y="mean",
        error_y="std",
        markers=True,
        labels={
            "network_size": "Network size",
            "mean": "Observed mean degree",
            "std": "Std dev across runs",
        },
    )
    st.plotly_chart(degree_fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        hist = px.histogram(
            runs_df,
            x="mean_events_per_user_per_week",
            color="mode",
            barmode="overlay",
            category_orders={"mode": mode_order},
            color_discrete_map=mode_colors,
            labels={"color": "Mode"},
            title="Distribution of run-level event outcomes",
        )
        st.plotly_chart(hist, use_container_width=True)
    with col2:
        box = px.box(
            runs_df,
            x="mode",
            y="mean_events_per_user_per_week",
            color="mode",
            category_orders={"mode": mode_order},
            color_discrete_map=mode_colors,
            labels={"x": "Mode", "y": "Mean events/user/week", "color": "Mode"},
            title="Run-level outcome spread by mode",
        )
        st.plotly_chart(box, use_container_width=True)

    if selected_run is None:
        st.error("Could not locate selected run in payload.")
        return

    st.subheader("Selected Run Graph Heatmap")
    n_edges = len(selected_run.get("network", {}).get("edges", []))
    if n_edges > 5000:
        st.info(f"Network too large ({n_edges:,} edges). Network visualisation not shown.")
    else:
        render_pyvis_graph(selected_run)

    user_df = build_user_table(selected_run)

    st.subheader("User-Level Outcomes")
    scatter = px.scatter(
        user_df,
        x="degree",
        y="events_per_week",
        hover_data=["user", "total_events", "as_holder", "as_solver", "as_matchmaker"],
        title="Degree vs events per week",
    )
    st.plotly_chart(scatter, use_container_width=True)

    st.subheader("Resolve Rate & Node Count by Degree Bucket")
    resolve_df = build_resolve_rate_by_degree(selected_run)
    resolve_fig = make_subplots(specs=[[{"secondary_y": True}]])
    resolve_fig.add_trace(
        go.Bar(
            x=resolve_df["degree_bucket"],
            y=resolve_df["node_count"],
            name="Node count",
            marker_color="#8EC5FF",
            opacity=0.8,
        ),
        secondary_y=False,
    )
    resolve_fig.add_trace(
        go.Scatter(
            x=resolve_df["degree_bucket"],
            y=resolve_df["resolve_rate"],
            name="Resolve rate",
            mode="lines+markers",
            marker=dict(color="#2ca02c", size=8),
            line=dict(color="#2ca02c", width=2),
        ),
        secondary_y=True,
    )
    resolve_fig.update_layout(
        xaxis_title="Degree bucket",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    resolve_fig.update_yaxes(
        title_text="Number of nodes", showgrid=False, secondary_y=False
    )
    resolve_fig.update_yaxes(
        title_text="Resolve rate",
        tickformat=".4%",
        showgrid=False,
        secondary_y=True,
    )
    st.plotly_chart(resolve_fig, use_container_width=True)

    st.subheader("Degree Distribution (log-log)")
    degree_rank_df = build_degree_rank_table(selected_run)
    degree_rank_fig = px.scatter(
        degree_rank_df,
        x="order",
        y="degree",
        hover_data=["degree"],
        log_x=True,
        log_y=True,
        labels={
            "order": "Rank (log scale)",
            "degree": "Degree (log scale)",
        },
    )
    st.plotly_chart(degree_rank_fig, use_container_width=True)

    st.dataframe(user_df, use_container_width=True)

    st.subheader("Selected Run Summary")
    summary = selected_run["summary"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total problems", summary.get("total_problems", 0))
    c2.metric("Total solved", summary.get("total_solved", 0))
    c3.metric("Solve rate", f"{100 * summary.get('solve_rate', 0.0):.2f}%")
    c4.metric(
        "Mean events/user/week",
        f"{summary.get('mean_events_per_user_per_week', 0.0):.3f}",
    )

    # Explicit critical-mass crossing table
    crossing_rows = []
    for mode in (False, True):
        mode_label = "With matchmaking" if mode else "No matchmaking"
        mode_df = grouped[grouped["matchmaking"] == mode].sort_values("network_size")
        crossing = mode_df[mode_df["mean"] >= 1.0]
        crossing_size = int(crossing.iloc[0]["network_size"]) if not crossing.empty else None
        crossing_rows.append({"mode": mode_label, "critical_mass_size": crossing_size})

    st.subheader("Estimated Critical Mass")
    st.table(pd.DataFrame(crossing_rows))


if __name__ == "__main__":
    main()
