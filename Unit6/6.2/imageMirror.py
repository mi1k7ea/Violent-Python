#!/usr/bin/python
#coding=utf-8
from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os
import optparse

def mirrorImages(url, dir):
	ab = anonBrowser()
	ab.anonymize()
	html = ab.open(url)
	soup = BeautifulSoup(html)
	image_tags = soup.findAll('img')

	for image in image_tags:
		# lstrip() 方法用于截掉字符串左边的空格或指定字符
		filename = image['src'].lstrip('http://')
		filename = os.path.join(dir, filename.replace('/', '_'))
		print '[+] Saving ' + str(filename)
		data = ab.open(image['src']).read()
		# 回退
		ab.back()
		save = open(filename, 'wb')
		save.write(data)
		save.close()

def main():
	parser = optparse.OptionParser('[*]Usage: python imageMirror.py -u <target url> -d <destination directory>')
	parser.add_option('-u', dest='tgtURL', type='string', help='specify target url')
	parser.add_option('-d', dest='dir', type='string', help='specify destination directory')
	(options, args) = parser.parse_args()
	url = options.tgtURL
	dir = options.dir
	if url == None or dir == None:
		print parser.usage
		exit(0)
	else:
		try:
			mirrorImages(url, dir)
		except Exception, e:
			print '[-] Error Mirroring Images.'
			print '[-] ' + str(e)

if __name__ == '__main__':
	main()