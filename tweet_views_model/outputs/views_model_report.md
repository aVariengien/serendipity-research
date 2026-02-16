# Views prediction model (scraped timeline)

## Data
- Tweets used (deduplicated): **2633**
- Likes zero rate: **2.1%**
- Retweets zero rate: **34.9%**

### Likes distribution
- median: 51
- mean: 2976.3
- p75: 483
- p90: 4056
- p99: 58103
- max: 316720

### Retweets distribution
- median: 2
- mean: 291.7
- p75: 30
- p90: 254
- p99: 6283
- max: 41166

## Modeling choices suited for this distribution
- Predict in **log-space**: target = `log1p(views)` to stabilize heavy tails.
- Use **log features**: `log1p(likes)`, `log1p(retweets)`.
- Add **zero-retweet indicator** for the 0-inflated retweet mass.
- Add interaction term to capture non-linear coupling.
- Reweight training data toward problem-like tweets (`likes<=87`, `retweets<=2`).
- Evaluate with shuffled train/test splits (8 repeats).
- Select best model by **problem-regime MAE (log)**, not only global average.

## Model comparison
```
model  mae_log_mean  rmse_log_mean  r2_log_mean  mae_log_problem_mean  rmse_log_problem_mean  r2_log_problem_mean
huber        0.6409         0.8162       0.9096                0.6120                 0.7864               0.6547
ridge        0.6432         0.8154       0.9098                0.6120                 0.7866               0.6546
  gbr        0.6521         0.8318       0.9061                0.6144                 0.7901               0.6516
   rf        0.6680         0.8484       0.9023                0.6301                 0.8029               0.6401
```

## Selected model: `huber`
- Selection criterion: lowest **problem-regime MAE (log)**.
- Interpretation: typical multiplicative error in the focus regime is about `exp(0.6120) ~= 1.84x`.

## Outputs
Artifact files:
- `outputs/views_model_results.csv`
- `outputs/views_model.joblib`
- `outputs/predict_views.py`
- `outputs/predict_views_standalone.py`
- `outputs/pred_vs_actual_views.png`
- `outputs/model_vs_likes_with_actual.png`
- `outputs/model_vs_retweets_with_actual.png`

## Inference
- Joblib-based: `predict_views(likes, retweets)` in `outputs/predict_views.py`.
- Standalone (no sklearn/joblib): `predict_views(likes, retweets)` in `outputs/predict_views_standalone.py`.