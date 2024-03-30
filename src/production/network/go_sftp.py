"""
Class - Secure FTP process class
"""
import os
from datetime import datetime
import paramiko as miko

class GoSFTP:
    """
    Class: connect to secure FTP server and download, upload files
    """

    def __init__(self, entity) -> None:
        self._entity = entity
        self._client = None
        self._trans = None
        self._is_connected = False
        self._root_path = entity.path

    @property
    def is_connected(self):
        """
        Property - Is connecting to SFTP server
        """        
        return self._is_connected

    @property
    def root_path(self):
        return self._root_path

    @is_connected.setter
    def is_connected(self, value):
        self._is_connected = value

    def connect(self):
        """
        Method - Connect to SFTP server
        """        
        try:
            self._trans = miko.Transport((self._entity.host, self._entity.port))
            self._trans.connect(username=self._entity.username, password=self._entity.password)
            self._client = miko.SFTPClient.from_transport(self._trans)
            self._is_connected = True
        except:
            self._is_connected = False

    def disconnect(self):
        """
        Method - Disconnect from SFTP server
        """        
        self._client.close()
        self._trans.close()

    def get_directories(self, source):
        """
        Method - Get directories from SFTP server
        """
        return [dir for dir in self._client.listdir(source) \
                if 'd' in str(self._client.lstat(self._sftp_dir_path(source, dir))).split()[0]]

        # for dir in self._client.listdir(source):
        #     if 'd' in str(self._client.lstat(self._sftp_dir_path(source, dir))).split()[0]:
        #         print(dir)

    def get_all_directories(self, source):
        """
        Method - Get all directories from SFTP server
        """
        folders = []

        flie_list = self._client.listdir(source)

        for item in flie_list:
            if source == "/":
                _path = f"{source}{item}"
            else: _path = f"{source}/{item}"

            if 'd' in str(self._client.lstat(_path)).split()[0]:
                folders.append(_path)

                subfolders = self.get_all_directories(_path)
                folders += subfolders

        return folders

    def get_files(self, source, extension = ''):
        """
        Method - Get files from SFTP server
        """        
        if extension.__len__() == 0:                            
            return [f for f in self._client.listdir(source) \
                    if 'd' not in str(self._client.lstat(self._sftp_dir_path(source, f))).split()[0]]
        else:
            return [f for f in self._client.listdir(source) if (extension in f)]

    def get_file_attribues(self, source, extension=""):
        """
        """
        _result = []
        # print(self._client.chdir(source))
        print(source)
        self._client.listdir(source)
        if extension.__len__() > 0:
            for f in self._client.listdir(source):
                # print(self._client.lstat(self._sftp_dir_path(source, f)))
                # _result.append(str(self._client.lstat(self._sftp_dir_path(source, f))))
                _item = [
                    f,
                    datetime.fromtimestamp(self._client.stat(self._sftp_dir_path(source, f)).st_mtime)
                ]
                _result.append(_item)
                # if 'd' not in str(self._client.lstat(self._sftp_dir_path(source, f))).split()[0]:
        else:
            for f in self._client.listdir(source):
                # print(f)
                # print(self._sftp_dir_path(source, f))
                _item = [
                    f,
                    datetime.fromtimestamp(self._client.stat(self._sftp_dir_path(source, f)).st_mtime)
                ]
                _result.append(_item)
        return _result

    def download(self, src, dst):
        """
        Method - download file
        """
        self._client.get(src, dst)

    def remove(self, arg):
        """
        Method - delete file
        """
        self._client.remove(arg)

    def _sftp_dir_path(self, src, dir):
        return os.path.join(src, dir).replace("\\", "/")