from datetime import datetime  # 日付や時刻を扱うための標準ライブラリ

import pandas as pd  # 表形式のデータを扱うためのライブラリ

import pytz  # タイムゾーンを扱うためのライブラリ

import MetaTrader5 as mt5

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(2026, 7, 13, tzinfo = timezone)
utc_to = datetime(2026, 7, 20, tzinfo = timezone)
rates = mt5.copy_rates_range("USDJPY.cl", mt5.TIMEFRAME_M5, utc_from, utc_to)
mt5.shutdown()

print("Display obained data 'as is'")
for rate in rates:
    print(rate)

rates_frame = pd.DataFrame(rates)
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

print("\nDisplay dataframe with data")
print(rates_frame)

rates_frame.to_csv(r'C:\Users\bfgtu\OneDrive\デスクトップ\xgboost_練習_1\試作_1\TestDate_USDJPY_5m_20260713_20260720.csv',index=False)