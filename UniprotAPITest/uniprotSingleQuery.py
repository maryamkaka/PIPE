import urllib.request
import urllib.parse

url = 'http://www.uniprot.org/uniprot/'

params = {
    'query':'accession:A0AVT1',
    'format':'tab',
    'columns':'database(pfam)'
}

data = urllib.parse.urlencode(params)

print(url + '?' + data)
request = urllib.request.Request(url + '?' + data)
contact = "maryam.kaka@carleton.ca"
request.add_header('User-Agent', 'Python %s' % contact)

response = urllib.request.urlopen(request)
protein = response.read()

print(protein)
