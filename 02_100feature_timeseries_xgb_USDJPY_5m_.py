import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

train_csv_file = open(r".\TrainDate_USDJPY_5m_from2026, 8, 10_to2026, 8, 11.csv")
train_df_USDJPY_5m = pd.read_csv(train_csv_file)
train_csv_file.close()
train_df_USDJPY_5m = train_df_USDJPY_5m.drop(columns="spread")
window = 100
ohlcvr_cols = ["open", "high", "low", "close", "tick_volume", "real_volume"]
feature_name = [f"{col}_{j}" for j in range(window) for col in ohlcvr_cols]
params = {"objective": "reg:squarederror", "learning_rate": 0.1, }
booster = None

for i in range(window, len(train_df_USDJPY_5m)):
    print(i)
    past_deta = train_df_USDJPY_5m.iloc[i-window:i][ohlcvr_cols]
    feature_row = past_deta.values.flatten()
    train_x = pd.DataFrame([feature_row], columns=feature_name)
    train_y = pd.Series([train_df_USDJPY_5m.iloc[i]["high"]])
    dtrain = xgb.DMatrix(train_x, label=train_y)
    predictions = booster.predict(dtrain) if booster is not None else None
    print(predictions, train_y)
    booster = xgb.train(params, dtrain, num_boost_round=1, xgb_model=booster)

    if i % 200 == 0:
        print(f"{i}行目まで学習完了。{booster.num_boosted_rounds()}")
        break