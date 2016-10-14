import urllib, urllib2

url = 'http://www.uniprot.org/uploadlists/'

params = {
	'from':'ACC', 
	'to':'P_REFSEQ_AC', 
	'format':'tab', 
	'query':'P13368 P20806'
}

data = urllib.urlencode(params)
request = urllib2.request.Request(url, data)
contact = "maryam.kaka@carleton.ca"
request.add_header('User-Agent', 'Python %s' % contact)
response = urllib2.urlopen(request)
page = response.read(200000)

