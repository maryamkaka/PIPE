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
            start = int(current[i].location['start'])
            end = int(current[i].location['end'])
            domainLength[current[i]['accession']] =  [start, end, end - start]
    except TypeError:
        start = int(xml.matches.match.location['start'])
        end = int(xml.matches.match.location['end'])
        domainLength[xml.matches.match['accession']] =  [start, end, end - start]

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
proteins = (proteinA + proteinB)
domains = (domainA + domainB)

length = open('ProteinFiles/length.txt', 'w')
length.write('Protein\tDomain\tProteinLength\tDomainLength\tDomainStart\tDomainEnd\n')
done = []

for i in range(0, len(proteins)):
    key = proteins[i] + '-' + domains[i]

    if(key in done):
        continue
    done.append(key)

    [pLen, dLen] = pfamConnect(proteins[i])

    print(proteins[i] + '\t' + domains[i] + '\t' + str(pLen) + '\t' + str(dLen[domains[i]][2]) + '\t' + str(dLen[domains[i]][0]) + '\t' + str(dLen[domains[i]][1]) + '\n')
    length.write(proteins[i] + '\t' + domains[i] + '\t' + str(pLen) + '\t' + str(dLen[domains[i]][2]) + '\t' + str(dLen[domains[i]][0]) + '\t' + str(dLen[domains[i]][1]) + '\n')
