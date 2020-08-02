#!/usr/bin/python
#coding=utf-8
from scapy.all import *

# 触发DDoS警报
def ddosTest(src, dst, iface, count):
	pkt = IP(src=src, dst=dst) / ICMP(type=8, id=678) / Raw(load='1234')
	send(pkt, iface=iface, count=count)

	pkt = IP(src=src, dst=dst) / ICMP(type=0) / Raw(load='AAAAAAAAAA')
	send(pkt, iface=iface, count=count)

	pkt = IP(src=src, dst=dst) / UDP(dport=31335) / Raw(load='PONG')
	send(pkt, iface=iface, count=count)

	pkt = IP(src=src, dst=dst) / ICMP(type=0, id=456)
	send(pkt, iface=iface, count=count)

src = "192.168.220.132"
dst = "192.168.220.129"
iface = "eth0"
count = 1
ddosTest(src, dst, iface, count)