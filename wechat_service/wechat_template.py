import urllib, json

class Templates_message:

    def post(access_token, openid, template_id, template_data, url='', miniprogram='' ):
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + access_token
        data={
            "touser": openid,
            "template_id": template_id,
            "url": url,
            "miniprogram": {
                "appid":self.appid,
                "pagepath": pagepath
            },
            "data": template_data,
        }

        req_data = urllib.parse.urlencode(data)

        res = urllib.request.urlopen(url=url, data=req_data)

        res_dict = json.loads(res.read().decode())

        if res_dict["errcode"] ==0:
            return res_dict
        else:
            return None



