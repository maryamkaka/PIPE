import untangle
import collections

def pfamConnect(protein):
    url = 'http://pfam.xfam.org/protein/'

    xml = untangle.parse(url + protein + '?output=xml').pfam.entry

    proteinLength = int(xml.sequence['length'])
    domainLength = {}

    #extract data
    try:
        for i in range(0, len(xml.matches.match)):
            current = xml.matches.match
            domainLength[current[i]['accession']] = int(current[i].location['end']) - int(current[i].location['start'])
    except TypeError:
        domainLength[xml.matches.match['accession']] = int(xml.matches.match.location['end']) - int(xml.matches.match.location['start'])

    return [proteinLength, domainLength]

# Import data
proteinA = []
proteinB = []
domainA = []
domainB = []
with open('InteractionLists/singleDomain.txt') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        proteinA.append(line[0])
        proteinB.append(line[1])
        domainA.append(line[2])
        domainB.append(line[3])
    # remove heading
    proteinA.pop(0)
    proteinB.pop(0)
    domainA.pop(0)
    domainB.pop(0)

# find number of unique proteins and domains
proteins = dict(collections.Counter(proteinA + proteinB))
domains = dict(collections.Counter(domainA + domainB))

# find length of proteins and domains
proteinLength = {}
domainLength = {}

proteinLengthOutput = open('ProteinFiles/proteinLength.txt', 'w')
domainLengthOutput = open('ProteinFiles/DomainLength.txt', 'w')

for p in proteins:
    [pLen, domLen] = pfamConnect(p)

    proteinLength[p] = pLen
    print(p + '\t' + str(pLen))
    proteinLengthOutput.write(p + '\t' + str(pLen) + '\n')

    for d in domLen:
        if(not(d in domainLength) and (d in domains)):
            domainLength[d] = domLen[d]
            print(d + '\t' + str(domLen[d]))
            domainLengthOutput.write(d + '\t' + str(domLen[d]) + '\n')
