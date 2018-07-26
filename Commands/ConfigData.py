import xml.dom.minidom as minidom


def getNodeStr(nodes):
    return nodes.childNodes[0].data


def getFirstChild(node, title):
    return node.getElementsByTagName(title)[0].childNodes[0].data


def issetNode(node, tag):
    return not (not node.getElementsByTagName(tag))


class ConfigData:
    __siteCode = ''
    __siteName = ''
    __siteMode = ''
    __username = ''
    __servers = []
    __password = None
    __rsaKeyPath = None

    __type = None
    __arguments = {}

    def __init__(self, siteCode: str, siteMode: str, url='conf.xml'):
        servers = minidom.parse(url).getElementsByTagName("server")
        for server in servers:
            code = getFirstChild(server, "site-code")
            siteName = getFirstChild(server, "site-title")
            mode = getFirstChild(server, "site-mode")
            username = getFirstChild(server, "username")
            if code == siteCode and mode == siteMode:
                self.__siteCode = code
                self.__siteName = siteName
                self.__siteMode = mode
                self.__username = username
                for ip in server.getElementsByTagName("ip"):
                    self.__servers.append(getNodeStr(ip))
                if issetNode(server, 'pwd'):
                    self.__password = getFirstChild(server, "pwd")
                if issetNode(server, 'ssh-key'):
                    self.__rsaKeyPath = getFirstChild(server, "ssh-key")

    def getSiteCode(self):
        return self.__siteCode

    def getSiteName(self):
        return self.__siteName

    def getSiteMode(self):
        return self.__siteMode

    def getUsername(self):
        return self.__username

    def getServers(self):
        return self.__servers

    def getPassword(self):
        return self.__password

    def getKeyPath(self):
        return self.__rsaKeyPath

    def getArguments(self):
        return self.__arguments

    def addArgument(self, key: str, cmd: str) -> None:
        self.__arguments[key] = cmd

    def getType(self):
        return self.__type

    def setType(self, newType: int) -> None:
        self.__type = newType

    def toDict(self) -> dict:
        result = {
            'siteCode': self.getSiteCode(),
            'siteName': self.getSiteName(),
            'siteMode': self.getSiteMode(),
            'username': self.getUsername(),
            'servers': self.getServers()
        }

        if self.getPassword():
            result['pwd'] = self.getPassword()
        if self.getKeyPath():
            result['keyPath'] = self.getKeyPath()
        return result
