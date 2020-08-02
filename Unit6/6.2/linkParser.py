#!/usr/bin/python
#coding=utf-8
from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os
import optparse
import re

def printLinks(url):
	ab = anonBrowser()
	ab.anonymize()
	page = ab.open(url)
	html = page.read()
	# 使用re模块解析href链接
	try:
		print '[+] Printing Links From  Regex.'
		link_finder = re.compile('href="(.*?)"')
		links = link_finder.findall(html)
		for link in links:
			print link
	except:
		pass
	# 使用bs4模块解析href链接
	try:
		print '\n[+] Printing Links From BeautifulSoup.'
		soup = BeautifulSoup(html)
		links = soup.findAll(name='a')
		for link in links:
			if link.has_key('href'):
				print link['href']
	except:
		pass

def main():
	parser = optparse.OptionParser('[*]Usage: python linkParser.py -u <target url>')
	parser.add_option('-u', dest='tgtURL', type='string', help='specify target url')
	(options, args) = parser.parse_args()
	url = options.tgtURL

	if url == None:
		print parser.usage
		exit(0)
	else:
		printLinks(url)

if __name__ == '__main__':
	main()