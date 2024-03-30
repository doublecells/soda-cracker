
import re

class RegexUtils:
    def __init__(self, pattern, value) -> None:
        self._pattern = pattern
        self._value = value
    
    def get_group(self):
        _result = re.search(r'{}'.format(self._pattern), self._value)
        return _result.group()
    
    def get_groups(self) -> None:
        _result = re.search(r'{}'.format(self._pattern), self._value)
        return _result.groups()
