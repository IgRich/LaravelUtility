import paramiko
import time
import os


class SshClient:
    __username = None
    __hostname = None
    __key = None

    def __init__(self, config: dict):
        self.__key = paramiko.RSAKey.from_private_key_file(config["key_path"])
        self.__username = config["username"]
        self.__hostname = config["host"]
        self.__remoteConn = paramiko.SSHClient()

        # connect
        self.__remoteConn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__remoteConn.connect(hostname=self.__hostname, username=self.__username, pkey=self.__key)
        print("SSH connection established to " + config["host"])
        __remote = self.__remoteConn.invoke_shell()
        time.sleep(5)
        bytes = __remote.recv(500)
        print(bytes.decode(encoding='utf-8'))

    def RunCommand(self, commands):
        if type(commands) is list:
            if commands[0] == "SFTP":
                del commands[0]
                return self.get_remote_file(commands[0], commands[1])
            commands = self.pipeCommand(commands)
        stdin, stdout, stderr = self.__remoteConn.exec_command(commands)
        stdin.close()
        out = SshClient.formatCommand(commands)
        with stdout, stderr:
            out = out + stdout.read().decode(encoding='utf-8')
            out = out + stderr.read().decode(encoding='utf-8')
        return out

    @staticmethod
    def formatCommand(commands: str) -> str:
        result = "\nЗапущенная команды:\n"
        for cmd in commands.split(";"):
            result = result + "\t" + cmd + " ;\n"
        return result

    @staticmethod
    def pipeCommand(commands: list) -> str:
        result = ""
        for command in commands:
            result = result + str(command) + " ; "
        return result[:-3]

    def get_remote_file(self, remotePath, localPath):
        hostkeytype, hostkey = self.get_host_key(self.__hostname)

        try:
            t = paramiko.Transport(self.__hostname, 22)
            t.connect(hostkey=hostkey, username=self.__username, pkey=self.__key)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.get(remotePath, os.path.basename(localPath))
            t.close()
        except FileNotFoundError:
            return "Файл '" + remotePath + "' не найден!"
        return "Файл " + remotePath + " успешно сохранен как " + localPath

    def get_host_key(self, host):
        hostkeytype = hostkey = None
        try:
            host_keys = paramiko.util.load_host_keys(os.path.expanduser("~/.ssh/known_hosts"))
        except IOError:
            host_keys = {}
        if host in host_keys:
            hostkeytype = host_keys[host].keys()[0]
            hostkey = host_keys[host][hostkeytype]
        return hostkeytype, hostkey
