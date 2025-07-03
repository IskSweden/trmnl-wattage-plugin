import config
import collections
import datetime

class WattageDataManager:
    def __init__(self):
        self._set_latest_raw_wattage = None

        self.wattage_data_buffer = collections.deque(maxlen=config.DATA_BUFFER_SIZE)

        self.buffer_size = config.DATA_BUFFER_SIZE

        current_time = datetime.datetime.now()
        interval_minutes = 60 // 5

        for i in range(5, -1, -1):
            timestamp = current_time - datetime.timedelta(minutes=i * interval_minutes)
            self.wattage_data_buffer.append((timestamp, 0))





    def _set_latest_raw_wattage(self, wattage, timestamp):
        print(f"{wattage} recieved at {timestamp}")
        i = 0


        

