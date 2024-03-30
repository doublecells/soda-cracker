
import logging

class LogUtils:

    def __init__(self, entity) -> None:
        self._entity = entity
        logging.basicConfig(filename='app.log', filemode='w',  format='%(asctime)s - %(message)s')
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)

    def log(self, arg):                
        self._logger.info(msg=arg)
