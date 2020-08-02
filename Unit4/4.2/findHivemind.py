#!/usr/bin/python
#coding=utf-8
import dpkt
import socket

def findHivemind(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			sport = tcp.sport
			# 若目标端口为6667且含有“!lazor”指令，则确定是某个成员提交一个攻击指令
			if dport == 6667:
				if '!lazor' in tcp.data.lower():
					print '[!] DDoS Hivemind issued by: '+src
					print '[+] Target CMD: ' + tcp.data
			# 若源端口为6667且含有“!lazor”指令，则确定是服务器在向HIVE中的成员发布攻击的消息
			if sport == 6667:
				if '!lazor' in tcp.data.lower():
					print '[!] DDoS Hivemind issued to: '+src
					print '[+] Target CMD: ' + tcp.data
		except:
			pass

f = open('hivemind.pcap')
pcap = dpkt.pcap.Reader(f)
findHivemind(pcap)