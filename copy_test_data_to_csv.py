from datetime import datetime  # 日付や時刻を扱うための標準ライブラリ

import pandas as pd  # 表形式のデータを扱うためのライブラリ

import pytz  # タイムゾーンを扱うためのライブラリ

import MetaTrader5 as mt5

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

start_day = (2026, 8, 11) # 取得開始日

end_day = (2026, 8, 12) # 取得終了日

timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(*start_day, tzinfo = timezone)
utc_to = datetime(*end_day, tzinfo = timezone)
rates = mt5.copy_rates_range("USDJPY.cl", mt5.TIMEFRAME_M5, utc_from, utc_to)
mt5.shutdown()

print("Display obained data")
for rate in rates:
    print(rate)

rates_frame = pd.DataFrame(rates)
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

print("\nDisplay dataframe with data")
print(rates_frame)

rates_frame.to_csv(r'.\TestDate_USDJPY_5m_from2026, 8, 11_to2026, 8, 12.csv',index=False)