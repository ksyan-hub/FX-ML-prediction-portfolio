from datetime import datetime  # 日付や時刻を扱うための標準ライブラリ

import pandas as pd  # 表形式のデータを扱うためのライブラリ

import pytz  # タイムゾーンを扱うためのライブラリ

import MetaTrader5 as mt5

from setting_traindata import data_setting

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

date = data_setting()

print(f"{date.start}から{date.end}のデータを取得")

timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(*date.start, tzinfo = timezone)
utc_to = datetime(*date.end, tzinfo = timezone)
rates = mt5.copy_rates_range("USDJPY.cl", mt5.TIMEFRAME_M5, utc_from, utc_to)
mt5.shutdown()

rates_frame = pd.DataFrame(rates)
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

print("\nDisplay dataframe with data")
print(rates_frame)

map(str, date.start)
map(str, date.end)

rates_frame.to_csv(rf".\csv_rate_data\traindata_from{date.start}_to{date.end}.csv",index=False)