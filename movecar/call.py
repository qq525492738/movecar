import urllib.parse, urllib.request
import hashlib
import time
import datetime
import json
from wechat_service import message as ms


class Phone:
    def __init__(self, appkey='dongsheng', secretkey='ydxs99rjz6oed1aftyr3m2ly0yj05v29'):
        self.appkey = appkey
        self.secretkey = secretkey
        self.url = '114.55.179.220:8080/safenumber/'

    def __generate_msgdgt(self, ts, data):
        d = data.copy()
        d['appkey'] = self.appkey
        d['ts'] = ts
        sort = sorted(d)
        string = self.secretkey
        for each in sort:
            string += each + d[each]

        m = hashlib.md5()
        m.update(string.encode('utf-8'))
        
        return m.hexdigest().upper()

    def bind(self, tela='', telx='', telb='', requestid='1'):
        if isinstance(tela, int):
            tela=str(tela)
        elif isinstance(telb, int):
            tela=str(telb)
        elif isinstance(telx, int):
            telx= str(telx)
        elif isinstance(requestid, int):
            requestid= str(requestid)
        ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

        data = {
            'requestId': '1',#requestid,
            'telA': tela,
            'telX': telx,
            'telB': telb,
            'subts': ts[:-3],
            'expiration': '600',
        }
        #urldata = urllib.parse.urlencode(data).encode()
        msgdgt = self.__generate_msgdgt(ts=ts, data=data)
        
        headers = {
            'Accept': "application/json;charset=utf-8",
            'Content-Type': "application/json;charset=utf-8",
            'appkey': self.appkey,
            'ts': ts,
            'msgdgt': msgdgt,
        }

        req = urllib.request.Request(url='http://114.55.179.220:8080/safenumber/v2/axb/bound',\
                                     data=json.dumps(data).encode(), headers=headers)
        
        with urllib.request.urlopen(req) as resd:
            
            return json.loads(resd.read().decode())['data']['telX']


if __name__ == '__main__':
    p = Phone()
    print(p.bind(tela='15877752003', telb='15877752003', requestid='2'))


