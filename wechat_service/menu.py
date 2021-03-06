#filename: menu

import urllib
from basic import Basic

class Menu(object):
    def __init__(self):
        pass
    def create(self,postData,accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        postData = postData.encode("utf-8")
        urlResp = urllib.request.urlopen(url=postUrl,data=postData)
        print(urlResp.read())
    def query(self,accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu.get?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url = postUrl)

    def delete(self,accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url = postUrl)
		
    def get_current_selfmenu_info(self,accessToken):
        postUrl = "http://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url = postUrl)

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [

            {
                "type": "view",
                "name": "钉钉挪车",
                "url": "https://yqzql.cn/wechat_service?path=index"
            },
            {
                "type": "view",
                "name": "test-center",
                "url": "https://yqzql.cn/wechat_service?path=center"
            },
        ]
    }
    """

    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(postJson,accessToken)
