

def uploadFile(fileName):
	print "[+] Uploading file to VirSCAN..."
	fileContents = open(fileName,'rb').read()

	header = {
		'Host': 'up.virscan.org',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://www.virscan.org/',
		'Content-Type': 'multipart/form-data; boundary=---------------------------20121180416870',
		'Upgrade-Insecure-Requests': '1'
	}
	        
	params = "-----------------------------20121180416870"
	params += "\r\nContent-Disposition: form-data; name=\"UPLOAD_IDENTIFIER\""
	params += "\r\nContent-Type: application/octet stream\r\n\r\n"
	params += fileContents
	params += "\r\n------WebKitFormBoundaryF17rwCZdGuPNPT9U"
	params += "\r\nContent-Disposition: form-data; name=\"submitfile\"\r\n"
	params += "\r\nSubmit File\r\n"
	params += "------WebKitFormBoundaryF17rwCZdGuPNPT9U--\r\n"
	conn = httplib.HTTPConnection('vscan.novirusthanks.org')
	conn.request("POST", "/", params, header)
	response = conn.getresponse()
	location = response.getheader('location')
	conn.close()
	return location