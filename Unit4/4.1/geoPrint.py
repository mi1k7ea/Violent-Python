#!/usr/bin/python
#coding=utf-8
import dpkt
import socket
import pygeoip
import optparse

gi = pygeoip.GeoIP('GeoLiteCity.dat')

# 查询数据库相关的城市信息并输出
def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	# 原来的代码为 region = rec['region_name']，已弃用'region_name'
	region = rec['region_code']
	country = rec['country_name']
	long = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' + tgt + ' Geo-located. '
	print '[+] '+str(city)+', '+str(region)+', '+str(country)
	print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)

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
			print '[+] Src: ' + retGeoStr(src) + '--> Dst: ' + retGeoStr(dst)
		except:
			pass

# 返回指定IP地址对应的物理位置
def retGeoStr(ip):
	try:
		rec = gi.record_by_name(ip)
		city = rec['city']
		country = rec['country_code3']
		if city != '':
			geoLoc = city + ', ' + country
		else:
			geoLoc = country
		return geoLoc
	except Exception, e:
		return 'Unregistered'

def main():
	parser = optparse.OptionParser('[*]Usage: python geoPrint.py -p <pcap file>')
	parser.add_option('-p', dest='pcapFile', type='string', help='specify pcap filename')
	(options, args) = parser.parse_args()
	if options.pcapFile == None:
		print parser.usage
		exit(0)
	pcapFile = options.pcapFile
	f = open(pcapFile)
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)

if __name__ == '__main__':
	main()