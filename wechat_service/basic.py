#file name: basic
from urllib.request import urlopen
import time,json

class Basic:
    def __init__(self):
        self.__accessToken = ""
        self.__leftTime = 0
    def __real_get_access_token(self):
        appId= "wx1daf30a5ae26e09e"
        appSecret = "771f1f04b90cbefa7a10c297bfc6046c"
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urlopen(url=postUrl)
        urlResp = json.loads(urlResp.read().decode("utf-8"))

        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken
    
    def run():
        while(True):
            if self.__leftTime >10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()
