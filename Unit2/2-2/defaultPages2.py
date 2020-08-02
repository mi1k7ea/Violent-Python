#!/usr/bin/python
#coding=utf-8
import ftplib

def returnDefault(ftp):
	try:
		#nlst()方法获取目录下的文件
		dirList = ftp.nlst()
	except:
		dirList = []
		print '[-] Could not list directory contents.'
		print '[-] Skipping To Next Target.'
		return

	retList=[]
	for fileName in dirList:
		#lower()方法将文件名都转换为小写的形式
		fn = fileName.lower()
		if '.php' in fn or '.htm' in fn or '.asp' in fn:
			print '[+] Found default page: ' + fileName
			retList.append(fileName)

	if len(retList) == 0:
		print '[-] Could not list directory contents.'
		print '[-] Skipping To Next Target.'
		
	return retList

def main():

	while True:
		host = raw_input('[*]Host >>> ')
		username = raw_input('[*]Username >>> ')
		password = raw_input('[*]Password >>> ')

		try:
			ftp = ftplib.FTP(host)
			ftp.login(username,password)
			returnDefault(ftp)
		except:
			print '[-] Logon failed.'

		print

if __name__ == '__main__':
	main()