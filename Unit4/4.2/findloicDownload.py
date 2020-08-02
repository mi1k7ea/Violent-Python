#!/usr/bin/python
#coding=utf-8
import dpkt
import socket

def findDownload(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			# 获取TCP数据
			tcp = ip.data
			# 解析TCP中的上层协议HTTP的请求
			http = dpkt.http.Request(tcp.data)
			# 若是GET方法，且请求行中包含“.zip”和“loic”字样则判断为下载LOIC
			if http.method == 'GET':
				uri = http.uri.lower()
				if '.zip' in uri and 'loic' in uri:
					print "[!] " + src + " Downloaded LOIC."
		except:
			pass

f = open('download.pcap')
pcap = dpkt.pcap.Reader(f)
findDownload(pcap)