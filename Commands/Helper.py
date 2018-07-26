sites = {
    "dt": "domotekhnika.ru",
    "cm": "cybermall.ru"
}


def isCm(addr) -> bool:
    if type(addr) is str and (addr == "cybermall.ru" or addr == "cm.ru"):
        return True
    else:
        return False


def isDt(addr) -> bool:
    if (type(addr) is str and addr == "dt.ru") or \
            (type(addr) is dict and addr.get("node2") is not None):
        return True
    else:
        return False


def getSiteBase(siteName: str) -> str:
    return "/var/www/" + siteName + "/"


def getBuildPath(siteName: str, build: str) -> str:
    return Helper.getSiteBase(siteName) + "releases/" + build + "/"


def cacheClear(siteName: str) -> list:
    return [
        "cd " + Helper.getSiteBase(siteName) + "current",
        "php artisan cache:clear",
        "php artisan views:clear"
    ]


def phpRestart() -> list:
    return ["sudo service php-fpm restart"]


class Helper:
    @staticmethod
    def getSiteBase(siteName: str) -> str:
        return "/var/www/" + siteName + "/"
