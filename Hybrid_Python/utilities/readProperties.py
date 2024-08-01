import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class Read_config:
    @staticmethod
    def getApplication_Url():
        url = config.get("common info", "base_url")
        return url

    @staticmethod
    def api_url():
        response_url = config.get("common info", "api_url")
        return response_url
