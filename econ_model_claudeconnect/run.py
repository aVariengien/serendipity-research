"""Batch runner for the social matching simulation."""

from __future__ import annotations

import argparse
import json
from collections.abc import Callable
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
    parser.add_argument("--problems-per-day", type=float, default=3.0)
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
    parser.add_argument(
        "--target-avg-degree",
        type=float,
        default=None,
        help="Optional global target average degree for generated networks",
    )
    parser.add_argument(
        "--small-network-degree-fraction",
        type=float,
        default=None,
        help="If set with --max-target-avg-degree, use target=min(int(n*fraction), max)",
    )
    parser.add_argument(
        "--max-target-avg-degree",
        type=float,
        default=None,
        help="Cap K used with --small-network-degree-fraction",
    )
    parser.add_argument(
        "--disable-triadic-closure",
        action="store_true",
        help="Disable friend-of-friend closure links during graph generation",
    )
    return parser.parse_args()


def run_batch(
    *,
    days: int = 28,
    problems_per_day: float = 3.0,
    match_probability: float = 0.01,
    matchmaker_credit: float = 0.5,
    seeds_per_config: int = 10,
    sizes: list[int] | None = None,
    base_seed: int = 42,
    target_avg_degree: float | None = None,
    small_network_degree_fraction: float | None = None,
    max_target_avg_degree: float | None = None,
    enable_triadic_closure: bool = True,
    progress_callback: Callable[[int, int, int], None] | None = None,
) -> dict:
    """Run all configurations and return JSON-ready payload.

    Parameters
    ----------
    progress_callback : callable or None
        If provided, called after each individual run with
        ``(completed, total, network_size)``.
    """
    sizes = sizes or DEFAULT_SIZES
    rng = np.random.default_rng(base_seed)
    runs: list[dict] = []

    run_sizes_desc = sorted(sizes, reverse=True)
    total_runs = len(sizes) * 2 * seeds_per_config
    completed = 0

    for network_size in run_sizes_desc:
        for matchmaking in (False, True):
            for _ in range(seeds_per_config):
                seed = int(rng.integers(0, 2**31 - 1))
                per_size_target_avg_degree: float | None
                if (
                    small_network_degree_fraction is not None
                    and max_target_avg_degree is not None
                ):
                    per_size_target_avg_degree = float(
                        min(
                            int(network_size * small_network_degree_fraction),
                            max_target_avg_degree,
                        )
                    )
                    per_size_target_avg_degree = max(2.0, per_size_target_avg_degree)
                else:
                    per_size_target_avg_degree = target_avg_degree

                graph = generate_network(
                    network_size,
                    seed=seed,
                    target_avg_degree=per_size_target_avg_degree,
                    enable_triadic_closure=enable_triadic_closure,
                )
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

                completed += 1
                if progress_callback is not None:
                    progress_callback(completed, total_runs, network_size)

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "config": {
            "days": days,
            "problems_per_day": problems_per_day,
            "problems_per_day_sampling": "stochastic_rounding_floor_ceil",
            "match_probability": match_probability,
            "matchmaker_credit": matchmaker_credit,
            "seeds_per_config": seeds_per_config,
            "sizes": sizes,
            "base_seed": base_seed,
            "target_avg_degree": target_avg_degree,
            "small_network_degree_fraction": small_network_degree_fraction,
            "max_target_avg_degree": max_target_avg_degree,
            "enable_triadic_closure": enable_triadic_closure,
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
        target_avg_degree=args.target_avg_degree,
        small_network_degree_fraction=args.small_network_degree_fraction,
        max_target_avg_degree=args.max_target_avg_degree,
        enable_triadic_closure=not args.disable_triadic_closure,
    )

    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {len(payload['runs'])} runs to {output_path}")


if __name__ == "__main__":
    main()
