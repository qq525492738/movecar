from urllib import request
from . import reply

class intelligent:
	def __init__(self,recMsg):
		print(recMsg.FromUserName)
		print(recMsg.MsgType)
		self.__toUser = recMsg.FromUserName
		self.__fromUser = recMsg.ToUserName
		self.recMsg = recMsg
		self.content = '感谢你的关注'


	def send(self):
		if self.recMsg.MsgType == 'text':
			Features = self.recMsg.Content.decode()
			return self.process(Features)

	def process(self, Features):
		return reply.TextMsg(self.__toUser, self.__fromUser, 'sccessfully').send()

