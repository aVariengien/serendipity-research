import math
import joblib
import pandas as pd

_model = joblib.load("outputs/views_model.joblib")

def predict_views(likes: float, retweets: float) -> float:
    likes = max(0.0, float(likes))
    retweets = max(0.0, float(retweets))
    row = pd.DataFrame([{
        "likes_log": math.log1p(likes),
        "retweets_log": math.log1p(retweets),
        "retweets_zero": 1 if retweets == 0 else 0,
        "like_rt_interaction": math.log1p(likes) * math.log1p(retweets),
    }])
    pred_log = float(_model.predict(row)[0])
    return max(0.0, math.expm1(pred_log))

if __name__ == "__main__":
    examples = [(8, 0), (26, 1), (87, 2), (949, 34)]
    for l, r in examples:
        print(f"likes={l:>4}, retweets={r:>3} -> pred_views={predict_views(l, r):.0f}")
