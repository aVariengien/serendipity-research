"""Core simulation engine for problem-opportunity matching."""

from dataclasses import dataclass, field

import networkx as nx
import numpy as np


@dataclass
class UserEvents:
    """Tracks events for one user across all roles."""

    as_holder: float = 0.0
    as_solver: float = 0.0
    as_matchmaker: float = 0.0

    @property
    def total(self) -> float:
        return self.as_holder + self.as_solver + self.as_matchmaker


@dataclass
class SimulationResult:
    """Serializable simulation output."""

    n_users: int
    days: int
    problems_per_day: int
    match_probability: float
    matchmaking: bool
    matchmaker_credit: float
    seed: int | None
    edges: list[tuple[int, int]]
    degrees: dict[int, int]
    user_events: dict[int, UserEvents] = field(default_factory=dict)
    total_problems: int = 0
    total_solved: int = 0

    @property
    def weeks(self) -> float:
        return self.days / 7.0

    @property
    def solve_rate(self) -> float:
        if self.total_problems == 0:
            return 0.0
        return self.total_solved / self.total_problems

    @property
    def mean_events_per_user_per_week(self) -> float:
        if self.n_users == 0 or self.weeks == 0:
            return 0.0
        total = sum(ue.total for ue in self.user_events.values())
        return total / self.n_users / self.weeks

    def to_dict(self) -> dict:
        """Return JSON-friendly dictionary."""
        user_events = {}
        for uid, ue in self.user_events.items():
            user_events[str(uid)] = {
                "as_holder": ue.as_holder,
                "as_solver": ue.as_solver,
                "as_matchmaker": ue.as_matchmaker,
                "total": ue.total,
            }

        per_week = []
        if self.weeks > 0:
            per_week = [ue.total / self.weeks for ue in self.user_events.values()]

        summary = {
            "total_problems": self.total_problems,
            "total_solved": self.total_solved,
            "solve_rate": round(self.solve_rate, 6),
            "mean_events_per_user_per_week": round(
                self.mean_events_per_user_per_week, 6
            ),
        }
        if per_week:
            summary.update(
                {
                    "median_events_per_user_per_week": round(float(np.median(per_week)), 6),
                    "min_events_per_user_per_week": round(float(min(per_week)), 6),
                    "max_events_per_user_per_week": round(float(max(per_week)), 6),
                }
            )

        return {
            "parameters": {
                "n_users": self.n_users,
                "days": self.days,
                "problems_per_day": self.problems_per_day,
                "match_probability": self.match_probability,
                "matchmaking": self.matchmaking,
                "matchmaker_credit": self.matchmaker_credit,
                "seed": self.seed,
            },
            "network": {
                "edges": [list(edge) for edge in self.edges],
                "degrees": {str(uid): degree for uid, degree in self.degrees.items()},
            },
            "user_events": user_events,
            "summary": summary,
        }


def run_simulation(
    graph: nx.Graph,
    days: int = 28,
    problems_per_day: int = 3,
    match_probability: float = 0.01,
    matchmaking: bool = False,
    matchmaker_credit: float = 0.5,
    seed: int | None = None,
) -> SimulationResult:
    """Run simulation on a static social graph.

    Each problem is evaluated once at creation time:
    1) direct friend matching
    2) optional friend-of-friend matchmaking if still unsolved
    """
    rng = np.random.default_rng(seed)
    nodes = list(graph.nodes())

    friends = {u: list(graph.neighbors(u)) for u in nodes}
    friends_set = {u: set(friends[u]) for u in nodes}

    user_events = {u: UserEvents() for u in nodes}
    total_problems = 0
    total_solved = 0

    for _day in range(days):
        for user_a in nodes:
            for _problem in range(problems_per_day):
                total_problems += 1
                solved = False

                direct_candidates = friends[user_a].copy()
                rng.shuffle(direct_candidates)

                for user_b in direct_candidates:
                    if rng.random() < match_probability:
                        user_events[user_a].as_holder += 1.0
                        user_events[user_b].as_solver += 1.0
                        total_solved += 1
                        solved = True
                        break

                if matchmaking and not solved:
                    candidate_to_matchmaker: dict[int, int] = {}
                    matchmaker_order = friends[user_a].copy()
                    rng.shuffle(matchmaker_order)

                    for friend_c in matchmaker_order:
                        for candidate_d in friends[friend_c]:
                            if (
                                candidate_d != user_a
                                and candidate_d not in friends_set[user_a]
                                and candidate_d not in candidate_to_matchmaker
                            ):
                                candidate_to_matchmaker[candidate_d] = friend_c

                    fof_candidates = list(candidate_to_matchmaker.keys())
                    rng.shuffle(fof_candidates)

                    for user_d in fof_candidates:
                        if rng.random() < match_probability:
                            matchmaker_c = candidate_to_matchmaker[user_d]
                            user_events[user_a].as_holder += 1.0
                            user_events[user_d].as_solver += 1.0
                            user_events[matchmaker_c].as_matchmaker += matchmaker_credit
                            total_solved += 1
                            solved = True
                            break

    return SimulationResult(
        n_users=len(nodes),
        days=days,
        problems_per_day=problems_per_day,
        match_probability=match_probability,
        matchmaking=matchmaking,
        matchmaker_credit=matchmaker_credit,
        seed=seed,
        edges=list(graph.edges()),
        degrees=dict(graph.degree()),
        user_events=user_events,
        total_problems=total_problems,
        total_solved=total_solved,
    )
