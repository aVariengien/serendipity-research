# Social Network Problem-Opportunity Simulation

This project simulates a social app where users generate problems daily and potentially match with solvers through:

- direct friends
- optional friend-of-friend matchmaking (warm intros)

The main metric is **events per user per week**. An event is credited to:

- problem holder: `+1`
- solver: `+1`
- matchmaker (if matchmaking flow is used): `+0.5`

## Model Summary

- Network sizes: `5, 10, 20, 40, 80, 160, 320`
- Problems per user per day: default `3`
- Match probability per candidate: default `0.01`
- Simulation duration: default `28` days
- Static social graph: each problem is evaluated once at creation and either solved or lost.

## Project Files

- `network.py`: heterogeneous social graph generation
- `simulation.py`: core simulation logic
- `run.py`: batch runner that writes `results/simulation_results.json`
- `app.py`: Streamlit dashboard and graph heatmap

## Setup (uv)

Install dependencies:

```bash
uv sync
```

## Run Simulation

Generate results for all sizes, both modes, multiple seeds:

```bash
uv run python run.py
```

Optional custom config:

```bash
uv run python run.py \
  --days 28 \
  --problems-per-day 3 \
  --match-probability 0.01 \
  --matchmaker-credit 0.5 \
  --seeds-per-config 10 \
  --sizes 5 10 20 40 80 160 320 \
  --output results/simulation_results.json
```

## Launch Web App

```bash
uv run streamlit run app.py
```

The app provides:

- network-size comparison with/without matchmaking
- critical-mass line at `1 event/user/week`
- selected-run graph heatmap (node color by events)
- user-level degree vs event scatter
- in-app simulation runner (adjust problems/day and solve probability, then regenerate results)

## Notes

- The runner auto-creates the `results/` directory if missing.
- If you change model logic, regenerate results before opening the app.
