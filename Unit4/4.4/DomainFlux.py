#!/usr/bin/python
#coding=utf-8
from scapy.all import *

def dnsQRTest(pkt):
	# 判断是否含有DNSRR且存在UDP端口53
	if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
		rcode = pkt.getlayer(DNS).rcode
		qname = pkt.getlayer(DNSQR).qname
		# 若rcode为3，则表示该域名不存在
		if rcode == 3:
			print '[!] Name request lookup failed: ' + qname
			return True
		else:
			return False

def main():
	unAnsReqs = 0
	pkts = rdpcap('domainFlux.pcap')
	for pkt in pkts:
		if dnsQRTest(pkt):
			unAnsReqs = unAnsReqs + 1
	print '[!] ' + str(unAnsReqs) + ' Total Unanswered Name Requests'

if __name__ == '__main__':
	main()