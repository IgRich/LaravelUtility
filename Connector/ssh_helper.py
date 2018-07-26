import sys

from Connector.SshTypes import SshTypes


class SshTypeNotFound(Exception):
    """ SshTypeNotFound """


class SshDispatcher:
    @staticmethod
    def dispatchCommand(type: int, args: dict):
        if type == SshTypes.EXECUTE:
            """ EXECUTE """
        elif type == SshTypes.DOWNLOAD_FILE:
            """ DOWNLOAD_FILE """
        elif type == SshTypes.UPLOAD_FILE:
            """ UPLOAD_FILE """
        else:
            raise SshTypeNotFound()
