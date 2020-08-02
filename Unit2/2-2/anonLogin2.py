#!/usr/bin/python
#coding=utf-8
import ftplib

def anonLogin(hostname):
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login('anonymous','what')
		print '\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception,e:
		print '\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.'

def main():
	while True:
		hostname = raw_input("Please enter the hostname: ")
		anonLogin(hostname)
		print

if __name__ == '__main__':
	main()