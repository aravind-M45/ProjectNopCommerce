
import configparser
config = configparser.RawConfigParser()
config.read('.\\configuration\\config.ini')

class ReadProperties:
    @staticmethod
    def readPageURL():
        url=config.get("common info","page_url")
        return url
    @staticmethod
    def readUsername():
        username=config.get("common info","username")
        return username

    @staticmethod
    def readPassword():
        password=config.get("common info","password")
        return password