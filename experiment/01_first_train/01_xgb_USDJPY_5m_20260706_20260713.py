import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error

params = {"objective": "reg:squarederror", "learning_rate": 0.1,}
cols = ["open", "low", "close", "tick_volume", "spread"]

train_csv_file = open(r".\TrainData_USDJPY_5m_20260706_20260713.csv", "r")
test_csv_file = open(r".\TestData_USDJPY_5m_20260713_20260720.csv", "r")

train_df_USDJPY_5m =  pd.read_csv(train_csv_file)
test_df_USDJPY_5m = pd.read_csv(test_csv_file)

train_csv_file.close()
test_csv_file.close()

train_deta_x = train_df_USDJPY_5m.drop(columns = ["high", "time", "real_volume"])
print(train_deta_x)

train_deta_y = train_df_USDJPY_5m.loc[:, 'high']
print(train_deta_y)

test_deta_x = test_df_USDJPY_5m.drop(columns = ["high", "time", "real_volume"])
print(test_deta_x)

test_deta_y = test_df_USDJPY_5m.loc[:, 'high']
print(test_deta_y)

dtrain = xgb.DMatrix(train_deta_x, label = train_deta_y, feature_names = cols )
dtest = xgb.DMatrix(test_deta_x, label = test_deta_y, feature_names = cols )
reg = xgb.train(params, dtrain, evals =[(dtrain,"train"), (dtest, "eval")])
pred_y = reg.predict(dtest)
print(mean_squared_error(test_deta_y, pred_y))
