""" Invoker entrance. """

from utils.time_utils import TimeUtils


class Invoker:

    def __init__(self, path = "") -> None:
        self._path = path
        self._ctls = []

    def run(self):
        _time_utils = TimeUtils()
        _time_utils.start()
        
        # -- snip --

        _time_utils.stop()
        print(_time_utils.time_diff)
