"""
JSON utility class
"""
import json

class JSONUtils:
    """Class JSONUtils - JSON data process utility class"""
    def __init__(self, arg):
        self._data = dict()

        if arg.endswith('.json'):
            with open(arg, mode='r', encoding='utf-8') as f:
                self._data = json.load(f)
        else:
            self._data = json.loads(arg)

    def read(self):
        """Function - Return JSON data read result"""
        return self._data
