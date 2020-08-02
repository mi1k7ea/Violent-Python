#!/usr/bin/python
#coding=utf-8
import optparse
import socket
from socket import *
from threading import *

#定义一个信号量
screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
	try:
		connSkt = socket(AF_INET,SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		connSkt.send('ViolentPython\r\n')
		result = connSkt.recv(100)

		#执行一个加锁操作
		screenLock.acquire()

		print '[+] %d/tcp open'%tgtPort
		print '[+] ' + str(result)
	except:
		#执行一个加锁操作
		screenLock.acquire()
		print '[-] %d/tcp closed'%tgtPort
	finally:
		#执行释放锁的操作，同时将socket的连接在其后关闭
		screenLock.release()
		connSkt.close()

def portScan(tgtHost,tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s' : Unknown host"%tgtHost
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP

	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
		t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser("[*] Usage : ./portscanner.py -H <target host> -p <target port>")
	parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
	parser.add_option('-p',dest='tgtPort',type='string',help='specify target port[s]')
	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
	main()