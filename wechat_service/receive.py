#filename:receive.py
from lxml import etree

def parse_xml(web_data):
    print(web_data)
    if len(web_data) == 0:
        return 'success'

    xmlData = etree.fromstring(web_data)
    return distinguish(xmlData)

def distinguish(xmlData):
    msg_type = xmlData.find("MsgType").text

    if msg_type == "text":
        return TextMsg(xmlData)
    elif msg_type == "voice":
        return VoiceMsg(xmlData)
    elif msg_type == "video":
        return VideoMsg(xmlData)
    elif msg_type == "image":
        return ImageMsg(xmlData)
    elif msg_type == "location":
        return LocationMsg(xmlData)
    elif msg_type == "event":
        return EventMsg(xmlData)
    elif msg_type == "link":
        return LinkMsg(xmlData)

class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text

class TextMsg(Msg):

    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.Content = xmlData.find('Content').text.encode("utf-8")

class ImageMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.MsgId = xmlData.find('MsgId').text
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text

class EventMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.Event = xmlData.find("Event").text
        eventkey = ["subscribe","unsubscribe","CLICK","VIEW"]

        if self.Event in eventkey:
            self.EventKey = xmlData.find("EventKey").text
        elif event == "SCAN":
            self.Ticket = xmlData.find("Ticket").text
        elif event == "LOCATION":
            self.Latitude = xmlData.find("Latitude").text
            self.Longitude = xmlData.find("Longitude").text
            self.Precision = xmlData.find("Precision").text

class VoiceMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.MediaId = xmlData.find("MediaId").text
        self.Format = xmlData.find("Format").text
        if self.Format == "amr":
            self.Recognition = xmlData.find("Recognition").text

class VideoMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.MediaId = xmlData.find("MediaId").text
        self.ThumbMediaId = xmlData.find("ThumbMediaId").text

class LocationMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self,xmlData)
        self.Location_X = xmlData.find("Location_X").text
        self.Location_Y = xmlData.find("Location_Y").text
        self.Scale = xmlData.find("Scale").text
        self.Label = xmlData.find("Label").text

class LinkMsg(Msg):
    def __init__(self,xmlData):

        Msg.__init__(self,xmlData)
        self.Title = xmlData.find("Title").text
        self.Description = xmlData.find("Description").text
        self.Url = xmlData.find("Url").text
