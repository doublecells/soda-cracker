
import datetime as dt

class TimeUtils:

    def __init__(self) -> None:
        self._start_time = None
        self._stop_time = None

    def start(self):
        self._start_time = dt.datetime.now()
    
    def stop(self):
        self._stop_time = dt.datetime.now()
    
    @property
    def time_diff(self):
        return self._stop_time - self._start_time
