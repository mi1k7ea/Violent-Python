#!/usr/bin/python
#coding=utf-8
import optparse
from PIL import Image
from PIL.ExifTags import TAGS
import urllib2
from bs4 import BeautifulSoup as BS
from os.path import basename
from urlparse import urlsplit

# 通过BeautifulSoup查找URL中所有的img标签
def findImages(url):
	print '[+] Finding images on ' + url
	urlContent = urllib2.urlopen(url).read()
	soup = BS(urlContent, 'lxml')
	imgTags = soup.findAll('img')
	return imgTags

# 通过img标签的src属性的值来获取图片URL下载图片
def downloadImage(imgTag):
	try:
		print '[+] Dowloading image...'
		imgSrc = imgTag['src']
		imgContent = urllib2.urlopen(imgSrc).read()
		imgFileName = basename(urlsplit(imgSrc)[2])
		imgFile = open(imgFileName, 'wb')
		imgFile.write(imgContent)
		imgFile.close()
		return imgFileName
	except:
		return ' '

# 获取图像文件的元数据，并寻找是否存在Exif标签“GPSInfo”
def testForExif(imgFileName):
	try:
		exifData = {}
		imgFile = Image.open(imgFileName)
		info = imgFile._getexif()
		if info:
			for (tag, value) in info.items():
				decoded = TAGS.get(tag, tag)
				exifData[decoded] = value
			exifGPS = exifData['GPSInfo']
			if exifGPS:
				print '[*] ' + imgFileName + ' contains GPS MetaData'
	except:
		pass

def main():
	parser = optparse.OptionParser('[*]Usage: python Exif.py -u <target url>')
	parser.add_option('-u', dest='url', type='string', help='specify url address')
	(options, args) = parser.parse_args()
	url = options.url
	if url == None:
		print parser.usage
		exit(0)
	else:
		imgTags = findImages(url)
		for imgTag in imgTags:
			imgFileName = downloadImage(imgTag)
			testForExif(imgFileName)

if __name__ == '__main__':
	main()