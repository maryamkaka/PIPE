import untangle

def pfamConnect(protein):
    url = 'http://pfam.xfam.org/protein/'

    xml = untangle.parse(url + protein + '?output=xml')
    pfam = []

    #extract data
    try:
        for i in range(0, len(xml.pfam.entry.matches.match)):
            pfam.append(xml.pfam.entry.matches.match[i]['accession'])
    except TypeError:
        pfam.append(xml.pfam.entry.matches.match['accession'])
    except IndexError:
        pfam.append(' ')

    return pfam
