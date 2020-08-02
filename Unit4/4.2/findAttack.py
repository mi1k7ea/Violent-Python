#!/usr/bin/python
#coding=utf-8
import dpkt
import socket

# 默认设置检测不正常数据包的数量的阈值为1000
THRESH = 1000

def findAttack(pcap):
	pktCount = {}
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			# 累计各个src地址对目标地址80端口访问的次数
			if dport == 80:
				stream = src + ':' + dst
				if pktCount.has_key(stream):
					pktCount[stream] = pktCount[stream] + 1
				else:
					pktCount[stream] = 1
		except:
			pass

	for stream in pktCount:
		pktsSent = pktCount[stream]
		# 若超过设置检测的阈值，则判断为进行DDoS攻击
		if pktsSent > THRESH:
			src = stream.split(':')[0]
			dst = stream.split(':')[1]
			print '[+] ' + src + ' attacked ' + dst + ' with ' + str(pktsSent) + ' pkts.'

f = open('attack.pcap')
pcap = dpkt.pcap.Reader(f)
findAttack(pcap)