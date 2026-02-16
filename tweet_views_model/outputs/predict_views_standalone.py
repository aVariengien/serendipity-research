import math

# Auto-generated standalone implementation of the trained model.
# No joblib, pandas, or sklearn needed at inference time.

# Feature order:
# 0: likes_log = log1p(likes)
# 1: retweets_log = log1p(retweets)
# 2: retweets_zero = 1 if retweets == 0 else 0
# 3: like_rt_interaction = likes_log * retweets_log

MEANS = [4.4535295765429606, 2.049629267222271, 0.3494113178883403, 14.696630404232298]
SCALES = [2.602731522352064, 2.3137449818104963, 0.47678406938558, 21.87078063902251]
COEFS = [2.501839884440413, 1.1410513653501317, 0.04492238060723195, -1.031455398213275]
INTERCEPT = 8.338940168890211


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
        print(f"likes={likes:>4}, retweets={retweets:>3} -> pred_views={pred:.0f}")
