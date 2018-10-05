#filename: reply

import time
class BlankMsg(object):
    def __init__(self):
        pass
    def send():
        return "success"

class Msg(object):
    def __init__(self,toUserName,fromUserName,msgType):
        self._dict = dict()
        self._dict['ToUserName'] = toUserName
        self._dict['FromUserName'] = fromUserName
        self._dict['CreateTime'] =  int(time.time())
        self._dict['MsgType'] = msgType
    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self,toUserName,fromUserName,content):
        Msg.__init__(self,toUserName,fromUserName,"text")
        
        self._dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self._dict)

class MediaMsg(Msg):
    def __init__(self,toUserName,fromUserName,mediaId,msgType = 'image'):
        Msg.__init__(self,toUserName,fromUserName,msgType)
        self._dict['MediaId'] = mediaId
    
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[{MsgType}]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self._dict)

class VideoMsg(Msg):
    def __init__(self,toUserName,fromUserName,mediaId,title=None,description=None):
        
        Msg.__init__(self,toUserName,fromUserName,"video")
        self._dict['MediaId'] = mediaId
        self._dict['Title'] = title
        self._dict['Description'] = description
    
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[{MsgType}]]></MsgType>
        <Video>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        <Title><![CDATA[{Title}]]></Title>
        <Description><!{CDATA[{Description'}]]></Description>
        </Video>
        </xml>
        """
        return XmlForm.format(**self._dict)

class MusicMsg(Msg):
    def __init__(self,toUserName,fromUserName,thumbMediaId,title=None,description=None,musicURL=None,hqmusicURL=None):
        Msg.__init__(self,toUserName,fromUserName,"music")
        self._dict['Title'] = title
        self._dict['Description'] = description
        self._dict['MusicURL'] = musicURL
        self._dict['HQMusicURL'] = hqmusicURL
        self._dict['ThumbMediaId'] = thumbMediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[music]]></MsgType>
        <Music>
        <Title><![CDATA[{Title}]]></Title>
        <Description><![CDATA[{Description}]]></Description>
        <MusicUrl><![CDATA[{MusicURL}]]></MusicUrl>
        <HQMusicUrl><![CDATA[{HQMusicURL}]]></HQMusicUrl>
        <ThumbMediaId><![CDATA[{ThumbMediaId}]]></ThumbMediaId>
        </Music>
        </xml>
        """
        return XmlForm.format(**self._dict)

class NewsMsg(Msg):
    def __init__(self,toUserName,fromUserName):#,title,description,picUrl,url):
        Msg.__init__(self,toUserName,fromUserName,"news")
        self._dict['articleCount'] = 0
        #self._dict['Title'] = title
        #self._dict['Description'] = description
        #self._dict['Articles'] = articles
        #self._dict['Picurl'] = picUrl
        #self._dict['Url'] = url

    def addnew(self,title,description,picurl,url):
        self._dict['articleCount'] += 1
        #self._dict['Title'+ str(articleCount)] = title
        #self._dict['Description' + str(articleCount)] = description
        #self._dict['picurl' + str(articleCount)] = picurl
        #self._dict['url' + str(articleCount)] = url
        self._dict['articles'] += """
        <item>
        <Title><![CDATA[{Title}]]></Title> 
        <Description><![CDATA[{Description}]]></Description>
        <PicUrl><![CDATA[{Picurl}]]></PicUrl>
        <Url><![CDATA[{Url}]]></Url>
        </item>
        """.format(Title=title,Description=description,Picurl=picurl,Url=url)

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>{articleCount}</ArticleCount>
        <Articles>
        {articles}
        </Articles>
        </xml>
        """

        return XmlForm.format(**self._dict)

