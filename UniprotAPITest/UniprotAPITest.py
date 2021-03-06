import urllib.request
import urllib.parse

url = 'http://www.uniprot.org/'

params = {
	'from':'ACC', 
	'to':'P_REFSEQ_AC', 
	'format':'tab', 
	'columns':'domains', 
	'query':'P13368 P20806',
}

data = urllib.parse.urlencode(params)
data = data.encode('ascii')

request = urllib.request.Request(url, data)
contact = "maryam.kaka@carleton.ca"
request.add_header('User-Agent', 'Python %s' % contact)

response = urllib.request.urlopen(request)
protein = response.read()

#write to file
f = open('recievedData', 'wb')
f.write(protein)
f.close()
print('Successfully written to file')
