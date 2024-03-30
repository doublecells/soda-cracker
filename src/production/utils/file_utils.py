"""
General file process utility
"""
import os
import enum

class SortedType(enum.Enum):
    NAME = "name"
    TIME = "time"


class FileUtils:

    def __init__(self) -> None:
        pass

    def read_all_lines(self, arg) -> None:
        with open(arg, mode='r', encoding='utf-8') as f:
            return f.readlines()

    def read_all_lines(self, arg, start = 0) -> None:
        with open(arg, mode='r', encoding='utf-8') as f:
            return f.readlines()[start:]

    def is_exists(self, arg):
        return os.path.exists(arg)
    
    def create_dir(self, arg):
        os.mkdir(arg)

    def delete_from(self, arg):
        os.remove(arg)

    def move_to(self, src, dst):
        if self.is_exists(dst):
            os.remove(dst)
        os.rename(src, dst)

    def get_path(self, arg):
        return os.path.dirname(arg)

    def get_file(self, arg):
        return os.path.basename(arg)

    def get_file_list(self, arg, type = SortedType.NAME):
        if type == SortedType.TIME:
            return self._get_file_list_with_time(arg)
        return self._get_file_list_with_name(arg)

    def _get_file_list_with_name(self, arg):
        return [f for f in os.listdir(arg) if os.path.isfile(os.path.join(arg, f))]

    def _get_file_list_with_time(self, arg):
        return [(f, os.stat(os.path.join(arg, f)).st_mtime) for f in os.listdir(arg) if os.path.isfile(os.path.join(arg, f))]

    def sorted_file_list(self, arg, reverse = True):
        return sorted(arg, key=lambda x: x[1], reverse = reverse)