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
import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network

from run import DEFAULT_SIZES, run_batch


DEFAULT_RESULTS_PATH = Path("results/simulation_results.json")


@st.cache_data
def load_results(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Results file not found: {path}")
    return json.loads(p.read_text(encoding="utf-8"))


def build_run_dataframe(payload: dict) -> pd.DataFrame:
    rows = []
    for run in payload.get("runs", []):
        summary = run.get("summary", {})
        rows.append(
            {
                "network_size": run["network_size"],
                "matchmaking": run["matchmaking"],
                "seed": run["seed"],
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


def main() -> None:
    st.set_page_config(page_title="Social Matching Simulation", layout="wide")
    st.title("Social Network Problem-Opportunity Matching")

    st.sidebar.header("Data")
    path = st.sidebar.text_input("Results JSON path", value=str(DEFAULT_RESULTS_PATH))
    output_path = Path(path)

    st.sidebar.header("Simulation Controls")
    sim_name = st.sidebar.text_input("Simulation name", value="baseline")
    sim_problems_per_day_text = st.sidebar.text_input(
        "Problems per user per day (pb/day, mean)", value="3"
    )
    sim_match_probability_text = st.sidebar.text_input(
        "Solve probability per candidate", value="0.01"
    )
    with st.sidebar.expander("Advanced run settings"):
        sim_days_text = st.text_input("Days", value="28")
        sim_seeds_per_config = st.number_input(
            "Seeds per configuration",
            min_value=1,
            max_value=100,
            value=10,
            step=1,
        )
        sim_sizes_text = st.text_input(
            "Network sizes (comma-separated, max 2000)",
            value=", ".join(str(x) for x in DEFAULT_SIZES),
        )
        sim_base_seed = st.number_input(
            "Base seed", min_value=0, max_value=2**31 - 1, value=42, step=1
        )

    run_clicked = st.sidebar.button("Run simulation from app", type="primary")
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
            with st.spinner("Running simulations..."):
                payload = run_batch(
                    days=int(sim_days),
                    problems_per_day=float(sim_problems_per_day),
                    match_probability=float(sim_match_probability),
                    matchmaker_credit=0.5,
                    seeds_per_config=int(sim_seeds_per_config),
                    sizes=[int(x) for x in sim_sizes],
                    base_seed=int(sim_base_seed),
                )
                payload["simulation_name"] = sim_name_clean
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            load_results.clear()
            st.sidebar.success(f"'{sim_name_clean}' written to {output_path}")
            st.rerun()

    try:
        payload = load_results(str(output_path))
    except FileNotFoundError as exc:
        st.error(str(exc))
        st.info(
            "Use the sidebar button 'Run simulation from app' or run "
            "`uv run python run.py`."
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
    selected_size = st.sidebar.selectbox("Network size", options=sizes, index=0)
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
