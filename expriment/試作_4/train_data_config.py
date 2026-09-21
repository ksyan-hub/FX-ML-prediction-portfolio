import MetaTrader5 as mt5

traindata_start_year = 2026
traindata_start_month = 8
traindata_start_day = 11
traindata_end_year = 2026
traindata_end_month = 8
traindata_end_day = 12
time_frame_data: int =  mt5.TIMEFRAME_M5

class train_data_config:
    def __init__(self):
        self.start = (traindata_start_year, traindata_start_month, traindata_start_day)
        self.end = (traindata_end_year, traindata_end_month, traindata_end_day)
        self.time_frame = (time_frame_data)
        self.file_path = rf".\csv_rate_data\traindata_from{self.start}_to{self.end}.csv"
        self.pred_file = rf".\predict_csv\試作_4_predicted_high_from{self.start}_to{self.end}.csv"