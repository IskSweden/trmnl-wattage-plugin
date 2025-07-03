import config


class WattageDataManager:
    def __init__(self):
        self.buffer_size = config.DATA_BUFFER_SIZE
        self._set_latest_raw_wattage = None

    def _set_latest_raw_wattage(wattage, timestamp):
        print(f"{wattage} recieved at {timestamp}")
