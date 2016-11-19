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
proteinLen = {}
domainLen = {}

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
proteins = (proteinA + proteinB)
domains = (domainA + domainB)

proteinLengthOutput = open('ProteinFiles/proteinLength.txt', 'w')
domainLengthOutput = open('ProteinFiles/DomainLength.txt', 'w')

for i in range(0, len(proteins)):
    key = proteins[i] + '-' + domains[i]

    if(key in domainLen):
        continue

    [pLen, dLen] = pfamConnect(proteins[i])

    if(not(proteins[i] in proteinLen)):
        proteinLen[proteins[i]] = pLen
        print(proteins[i] + '\t' + str(pLen))
        proteinLengthOutput.write(proteins[i] + '\t' + str(pLen) + '\n')

    domainLen[key] = dLen
    print(proteins[i] + '-' + domains[i] + '\t' + str(dLen[domains[i]]))
    domainLengthOutput.write(key + '\t' + str(dLen[domains[i]]) + '\n')
