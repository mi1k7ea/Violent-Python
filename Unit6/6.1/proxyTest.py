#!/usr/bin/python
#coding=utf-8
import mechanize

def testProxy(url, proxy):
	browser = mechanize.Browser()
	browser.set_proxies(proxy)
	page = browser.open(url)
	source_code = page.read()
	print source_code

url = 'http://2017.ip138.com/ic.asp'
hideMeProxy = {'http': '139.196.202.164:9001'}
testProxy(url, hideMeProxy)