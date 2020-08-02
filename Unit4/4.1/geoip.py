#!/usr/bin/python
#coding=utf-8
import pygeoip

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

gi = pygeoip.GeoIP('GeoLiteCity.dat')
tgt = '173.255.226.98'
printRecord(tgt)