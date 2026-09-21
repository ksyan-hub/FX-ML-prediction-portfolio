import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import csv
from train_data_config import train_data_config

params = {"objective": "reg:squarederror", "learning_rate": 0.1,}
booster = None

x_buffer = []
y_buffer = []
se_buffer = []
feature_columns = []

window = 12
tree_batch_size = 12
reduce_float= 1000

config = train_data_config()

with open(config.file_path, "r") as data:
    train_df_USDJPY_5m =  pd.read_csv(data)

ohlcts_cols = [ "open", "high", "low", "close", "tick_volume", "spread"]

for j in range(window):
        for col in ohlcts_cols:
            feature_columns.append(f"{col}_{j}")

with open(config.pred_file, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["0","predicted","actual","se","mse"])

with open(config.pred_file, "a", newline ="") as file:
    writer = csv.writer(file)

    for i in range(window, len(train_df_USDJPY_5m)):
        window_data= train_df_USDJPY_5m.iloc[i - window: i][ohlcts_cols] 

        if i % window == 0:
            print("window_data")
            print(window_data)

        feature_row = window_data.values.flatten()#一次元配列に変換 

        if i % window == 0:
            print("feature_row")
            print(feature_row)

        x_buffer.append(feature_row)
        y_buffer.append(train_df_USDJPY_5m.iloc[i]["high"])

        if booster is not None:
            pred_x = pd.DataFrame([feature_row], columns = feature_columns)
            pred_dmatrix = xgb.DMatrix(pred_x)
            predictions_data = booster.predict(pred_dmatrix)
            predictions = float(predictions_data[0]) #スカラー値に変換
            se = int(((predictions - train_df_USDJPY_5m.iloc[i]["high"])**2)*reduce_float)/reduce_float #誤差を2乗
            se_buffer.append(se)
            writed_predictions = int(float(predictions)*reduce_float)/reduce_float

            if i % 12 == 0: #60分/5分＝12
                sum_se = 0
                count_se = len(se_buffer)

                for val in se_buffer:
                    sum_se = sum_se + val

                mse = int((sum_se /  count_se)*reduce_float)/reduce_float
                print(mse)
                se_buffer = []
            else: mse = None

        else:
            writed_predictions = se = mse = None

        writer.writerow([ i - (window - 1), writed_predictions, train_df_USDJPY_5m.iloc[i]["high"],se,mse])
        
        if len(x_buffer) >= tree_batch_size:
             train_x = pd.DataFrame(x_buffer, columns = feature_columns)
             train_y = pd.Series(y_buffer)
             dtrain = xgb.DMatrix(train_x, label = train_y)#xgb.DMatrix(train_x, label=train_y)は特徴量とlabelの行数を一致させる必要がある
             booster = xgb.train(params, dtrain, num_boost_round = 1, xgb_model = booster)
             x_buffer = []
             y_buffer = []     

        if i + 1 == len(train_df_USDJPY_5m):
            print(f"{i}行目まで学習完了。{booster.num_boosted_rounds()}")
            break