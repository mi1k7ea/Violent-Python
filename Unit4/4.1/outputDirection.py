#!/usr/bin/python
#coding=utf-8
import dpkt
import socket

def printPcap(pcap):
	# 遍历[timestamp, packet]记录的数组
	for (ts, buf) in pcap:
		try:
			# 获取以太网层数据
			eth = dpkt.ethernet.Ethernet(buf)
			# 获取IP层数据
			ip = eth.data
			# 把存储在inet_ntoa中的IP地址转换成一个字符串
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print '[+] Src: ' + src + ' --> Dst: ' + dst
		except:
			pass

def main():
	f = open('geotest.pcap')
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)

if __name__ == '__main__':
	main()