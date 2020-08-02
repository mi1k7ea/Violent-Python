#!/usr/bin/python
#coding=utf-8
import mechanize
import cookielib
import random

class anonBrowser(mechanize.Browser):
	def __init__(self, proxies = [], user_agents = []):
		mechanize.Browser.__init__(self)
		self.set_handle_robots(False)
		# 可供用户使用的代理服务器列表
		self.proxies = proxies
		# user_agent列表
		self.user_agents = user_agents + ['Mozilla/4.0 ', 'FireFox/6.01','ExactSearch', 'Nokia7110/1.0'] 
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
		self.anonymize()

	# 清空cookie
	def clear_cookies(self):
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)

	# 从user_agent列表中随机设置一个user_agent
	def change_user_agent(self):
		index = random.randrange(0, len(self.user_agents) )
		self.addheaders = [('User-agent',  ( self.user_agents[index] ))]         
	        
	# 从代理列表中随机设置一个代理
	def change_proxy(self):
		if self.proxies:
			index = random.randrange(0, len(self.proxies))
			self.set_proxies( {'http': self.proxies[index]} )
	
	# 调用上述三个函数改变UA、代理以及清空cookie以提高匿名性，其中sleep参数可让进程休眠以进一步提高匿名效果
	def anonymize(self, sleep = False):
		self.clear_cookies()
		self.change_user_agent()
		self.change_proxy()

		if sleep:
			time.sleep(60)