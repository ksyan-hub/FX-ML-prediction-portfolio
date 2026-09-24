import pandas as pd
import numpy as np
import xgboost as xgb
import csv
from setting_traindata import data_setting

train_data = data_setting()
with open(train_data.train_data(), "r") as data:
    train_df_USDJPY_5m =  pd.read_csv(data)

window = 12
ohlcts_cols = [ "open", "high", "low", "close", "tick_volume", "spread"]
params = {"objective": "reg:squarederror", "learning_rate": 0.1,}
booster = None
predict_csv_file_path = rf".\predict_csv\03_predicted_high.csv"
se_buffer = []

with open(predict_csv_file_path, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["0","predicted","actual","se","mse"])

with open(predict_csv_file_path, "a", newline ="") as file:
    writer = csv.writer(file)

    for i in range(window, len(train_df_USDJPY_5m)):
        window_data= train_df_USDJPY_5m.iloc[i - window: i][ohlcts_cols] 
        window_data_shape = window_data.shape[0]
        feature_row = window_data.values.flatten()#一次元配列に変換 

        feature_columns = []
        for j in range(window_data_shape):
            for col in ohlcts_cols:
                feature_columns.append(f"{col}_{j}")

        train_x = pd.DataFrame([feature_row], columns = feature_columns)
        train_y = pd.Series([train_df_USDJPY_5m.iloc[i]["high"]])
        dtrain = xgb.DMatrix(train_x, label = train_y)#xgb.DMatrix(train_x, label=train_y)は特徴量とlabelの行数を一致させる必要がある

        mse = None
        if booster is not None:
            predictions_data = booster.predict(dtrain)
            predictions = float(predictions_data[0]) #スカラー値に変換
            se = ((predictions - train_df_USDJPY_5m.iloc[i]["high"]))**2 #誤差を2乗
            se_buffer.append(se)

            if i % 12 == 0: #60分/5分＝12
                sum_se = 0
                count_se = len(se_buffer)

                for val in se_buffer:
                    sum_se = sum_se + val

                mse= sum_se /  count_se
                se_buffer = [] #bufferをリセット

            else:mse = None

            writer.writerow([ i, predictions, train_df_USDJPY_5m.iloc[i]["high"],se,mse])

        booster = xgb.train(params, dtrain, num_boost_round = 1, xgb_model = booster)        

        if i + 1 == len(train_df_USDJPY_5m):
            print(f"{i}行目まで学習完了。{booster.num_boosted_rounds()}")
            break