from Commands.ConfigData import ConfigData
from Commands.Simple.BaseCommand import BaseCommand
from time import gmtime, strftime
from Commands.Helper import Helper
from Connector.SshTypes import SshTypes


class GetLastLog(BaseCommand):
    def run(self, data: ConfigData) -> ConfigData:
        curDate = strftime("%Y-%m-%d", gmtime())
        pathForProject = Helper.getSiteBase(data.getSiteName())
        remoteFilePath = pathForProject + "current/storage/logs/" + curDate + '-error.log'
        localFileName = strftime("logs/" + data.getSiteCode() + "_" + data.getSiteMode() + "_%Y-%m-%d_H-%M-%S.log",
                                 gmtime())
        data.setType(SshTypes.DOWNLOAD_FILE)
        data.addArgument('remote_file', remoteFilePath)
        data.addArgument('local_file', localFileName)
        return data
