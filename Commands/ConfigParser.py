import xml.dom.minidom as minidom


def getNodeStr(nodes):
    return nodes.childNodes[0].data


class ConfigParser:
    doc = None

    def __init__(self, url='conf.xml'):
        self.doc = minidom.parse(url)

    def getServersByCode(self, siteCode, siteMode):
        servers = self.doc.getElementsByTagName("server")
        for server in servers:
            code = getNodeStr(server.getElementsByTagName("site-code")[0])
            sitename = getNodeStr(server.getElementsByTagName("site-title")[0])
            mode = getNodeStr(server.getElementsByTagName("site-mode")[0])
            username = getNodeStr(server.getElementsByTagName("username")[0])
            pwd = server.getElementsByTagName("pwd")
            keyPath = server.getElementsByTagName("ssh-key")
            if code == siteCode and mode == siteMode:
                ips = []
                for ip in server.getElementsByTagName("ip"):
                    ips.append(getNodeStr(ip))
                result = {
                    'code': code,
                    'sitename': sitename,
                    'mode': mode,
                    'username': username,
                    'servers': ips
                }
                if pwd:
                    result['pwd'] = getNodeStr(pwd[0])
                if keyPath:
                    result['keyPath'] = getNodeStr(keyPath[0])
                return result
        return {}
