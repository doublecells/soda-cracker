""" Access the shared folder via account. """

import os
import shutil

from datetime import datetime

class GoSharedFolder:
    """
    Class - Shared folder access class
    """

    def __init__(self, entity) -> None:
        self._entity = entity
        self._is_connected = False
        self._path = "\\\\" + os.path.join(self._entity.host, self._entity.path)

    @property
    def path(self):
        return self._path

    @property
    def is_connected(self):
        """
        Property - Is connecting to shared folder
        """        
        return self._is_connected

    def connect(self):
        try:
            _access_command = "net use {} /user:{} {}".format(
                self._path,
                self._entity.username,
                self._entity.password
            )

            os.system(_access_command)

            self._is_connected = True
        except Exception as e:
            print(e)

    def disconnect(self):
        _left_command = "net use {} /delete".format(self._entity.path)
        os.system(_left_command)

    def get_all_directories(self, source):
        """
        Method - Get all directories from SFTP server
        """
        folders = []

        flie_list = os.listdir(source)

        for item in flie_list:
            _full_path = os.path.join(source, item)
            if os.path.isdir(_full_path):
                folders.append(_full_path)

                subfolders = self.get_all_directories(_full_path)
                folders += subfolders

        return folders

    def get_file_attributes(self, source, extension = ""):
        """
        """
        print(source)
        if extension.__len__() > 0:
            return [(f, datetime.fromtimestamp(os.path.getctime(os.path.join(source, f))).strftime("%Y-%m-%d %H:%M:%S")) 
                    for f in os.listdir(source) if os.path.isfile(os.path.join(source, f)) and (extension in f)]
        else:
            return [(f, datetime.fromtimestamp(os.path.getctime(os.path.join(source, f))).strftime("%Y-%m-%d %H:%M:%S")) 
                    for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]

    def download(self, src, dst):
        shutil.copyfile(src, dst)