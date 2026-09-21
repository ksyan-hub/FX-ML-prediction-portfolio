traindata_start_year = 2026
traindata_start_month = 8
traindata_start_day = 11
traindata_end_year = 2026
traindata_end_month = 8
traindata_end_day = 12

class data_setting:
    def __init__(self):
        self.start = (traindata_start_year, traindata_start_month, traindata_start_day)
        self.end = (traindata_end_year, traindata_end_month, traindata_end_day)

    def train_data(self):
        return(rf".\csv_rate_data\traindata_from{self.start}_to{self.end}.csv")
