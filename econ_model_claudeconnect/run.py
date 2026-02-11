"""Batch runner for the social matching simulation."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from network import generate_network
from simulation import run_simulation


DEFAULT_SIZES = [5, 10, 20, 40, 80, 160, 320]


def aggregate_runs(runs: list[dict]) -> list[dict]:
    """Aggregate mean event metrics per network size and matchmaking mode."""
    grouped: dict[tuple[int, bool], list[float]] = {}

    for run in runs:
        key = (run["network_size"], run["matchmaking"])
        value = run["summary"]["mean_events_per_user_per_week"]
        grouped.setdefault(key, []).append(value)

    rows: list[dict] = []
    for (network_size, matchmaking), values in sorted(grouped.items()):
        arr = np.array(values, dtype=float)
        rows.append(
            {
                "network_size": network_size,
                "matchmaking": matchmaking,
                "num_seeds": len(values),
                "mean_events_per_user_per_week_mean": float(arr.mean()),
                "mean_events_per_user_per_week_std": float(arr.std()),
                "mean_events_per_user_per_week_min": float(arr.min()),
                "mean_events_per_user_per_week_max": float(arr.max()),
                "critical_mass_reached": bool(arr.mean() >= 1.0),
            }
        )
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run social matching simulations.")
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--problems-per-day", type=int, default=3)
    parser.add_argument("--match-probability", type=float, default=0.01)
    parser.add_argument("--matchmaker-credit", type=float, default=0.5)
    parser.add_argument("--seeds-per-config", type=int, default=10)
    parser.add_argument(
        "--sizes",
        type=int,
        nargs="+",
        default=DEFAULT_SIZES,
        help="Network sizes to run",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="results/simulation_results.json",
        help="Output JSON path",
    )
    parser.add_argument(
        "--base-seed",
        type=int,
        default=42,
        help="Base random seed to generate per-run seeds",
    )
    return parser.parse_args()


def run_batch(
    *,
    days: int = 28,
    problems_per_day: int = 3,
    match_probability: float = 0.01,
    matchmaker_credit: float = 0.5,
    seeds_per_config: int = 10,
    sizes: list[int] | None = None,
    base_seed: int = 42,
) -> dict:
    """Run all configurations and return JSON-ready payload."""
    sizes = sizes or DEFAULT_SIZES
    rng = np.random.default_rng(base_seed)
    runs: list[dict] = []

    for network_size in sizes:
        for matchmaking in (False, True):
            for _ in range(seeds_per_config):
                seed = int(rng.integers(0, 2**31 - 1))
                graph = generate_network(network_size, seed=seed)
                result = run_simulation(
                    graph=graph,
                    days=days,
                    problems_per_day=problems_per_day,
                    match_probability=match_probability,
                    matchmaking=matchmaking,
                    matchmaker_credit=matchmaker_credit,
                    seed=seed,
                )
                run_record = result.to_dict()
                run_record["network_size"] = network_size
                run_record["matchmaking"] = matchmaking
                run_record["seed"] = seed
                runs.append(run_record)

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "config": {
            "days": days,
            "problems_per_day": problems_per_day,
            "match_probability": match_probability,
            "matchmaker_credit": matchmaker_credit,
            "seeds_per_config": seeds_per_config,
            "sizes": sizes,
            "base_seed": base_seed,
        },
        "aggregates": aggregate_runs(runs),
        "runs": runs,
    }


def main() -> None:
    args = parse_args()
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = run_batch(
        days=args.days,
        problems_per_day=args.problems_per_day,
        match_probability=args.match_probability,
        matchmaker_credit=args.matchmaker_credit,
        seeds_per_config=args.seeds_per_config,
        sizes=args.sizes,
        base_seed=args.base_seed,
    )

    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {len(payload['runs'])} runs to {output_path}")


if __name__ == "__main__":
    main()
