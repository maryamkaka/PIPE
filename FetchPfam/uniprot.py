import urllib.request
import urllib.parse

def uniprot(protein):
    url = 'http://www.uniprot.org/uniprot/'

    params = {
        'query':'accession:'+protein,
        'format':'tab',
        'columns':'database(pfam)'
    }

    data = urllib.parse.urlencode(params)
    request = urllib.request.Request(url + '?' + data)
    response = urllib.request.urlopen(request)

    pfam = response.read()
    pfam = pfam.decode().split('\n')[1].replace(';', '\t')
    return pfam 
