#!/usr/bin/python
#coding=utf-8
from scapy.all import *

# 检查数据包的IP层，提取出源IP和TTL字段的值
def testTTL(pkt):
	try:
		if pkt.haslayer(IP):
			ipsrc = pkt.getlayer(IP).src
			ttl = str(pkt.ttl)
			print "[+] Pkt Received From: " + ipsrc + " with TTL: " + ttl
	except:
		pass

def main():
	sniff(prn=testTTL, store=0)

if __name__ == '__main__':
	main()