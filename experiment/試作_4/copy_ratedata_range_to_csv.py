from datetime import datetime  # 日付や時刻を扱うための標準ライブラリ

import pandas as pd  # 表形式のデータを扱うためのライブラリ

import pytz  # タイムゾーンを扱うためのライブラリ

import MetaTrader5 as mt5

from train_data_config import train_data_config

data = train_data_config()

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

print(f"{data.start}から{data.end}のデータ取得を実行")

timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(*data.start, tzinfo = timezone)
utc_to = datetime(*data.end, tzinfo = timezone)
rates = mt5.copy_rates_range("USDJPY.cl", data.time_frame, utc_from, utc_to) 

if rates is not None:
    print("データ取得に成功")
mt5.shutdown()

rates_frame = pd.DataFrame(rates)
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

print(f"{data.time_frame}\n{rates_frame}")

rates_frame.to_csv(data.file_path,index=False)