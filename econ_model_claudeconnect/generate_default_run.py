"""Generate a default simulation run and save it as JSON.

This produces a pre-computed result file that the Streamlit app uses as
its landing page, so visitors see charts immediately without having to
run the simulation themselves.

The parameters here mirror the sidebar defaults in app.py.
"""

from __future__ import annotations

import json
from pathlib import Path

from run import run_batch

DEFAULT_OUTPUT = Path(__file__).parent / "default_run.json"

# These match the sidebar defaults in app.py exactly.
DEFAULT_PARAMS = dict(
    days=28,
    problems_per_day=0.7,
    match_probability=0.000051,
    matchmaker_credit=0.5,
    seeds_per_config=1,
    sizes=[5, 10, 20, 40, 80, 160, 320, 640, 1280],
    base_seed=42,
    small_network_degree_fraction=0.20,
    max_target_avg_degree=20.0,
    enable_triadic_closure=True,
)


def main() -> None:
    print("Running default simulation with app sidebar defaults...")
    payload = run_batch(**DEFAULT_PARAMS)
    payload["simulation_name"] = "Top 50 CA users Twitter base rate"

    DEFAULT_OUTPUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    n_runs = len(payload.get("runs", []))
    print(f"Wrote {n_runs} runs to {DEFAULT_OUTPUT}")


if __name__ == "__main__":
    main()
