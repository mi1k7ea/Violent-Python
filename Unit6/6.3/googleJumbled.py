#!/usr/bin/python
#coding=utf-8
import urllib
from anonBrowser import *

def google(search_term):
	ab = anonBrowser()
	# URL编码
	search_term = urllib.quote_plus(search_term)
	response = ab.open('https://www.googleapis.com/customsearch/v1?key=AIzaSyCn_IE6NM_ATjZ0j5vfXIFlyW-EpGs5gsU&cx=006431901905483214390:i3yxhoqkzo0&num=1&alt=json&q=' + search_term)
	print response.read()

google('Boundock Saint')