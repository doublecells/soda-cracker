
import zipfile

class CompressUtils:

    def __init__(self, entity) -> None:
        self._entity = entity

    def compress(self):
        pass

    def decompress(self):
        if self._entity.destination is None:
            self._decompress()
        else:
            self._decompress_with_destination(
                self._entity.path,
                self._entity.destination)
    
    def _decompress(self):
        pass

    def _decompress_with_destination(self, path, dest):
        """
        Decompress file to destination location
        """
        if self._entity.path is not None:
            with zipfile.ZipFile(path, 'r') as zf:
                zf.extractall(dest)
