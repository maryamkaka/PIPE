import collections
import matplotlib.pyplot as plt
import numpy as np

#variables
displayCharts = 0
verbose = 0

def printDict(d):
    for i in d:
        print(i + ': ' + str(d[i]))

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

with open('ProteinFiles/proteinLength.txt') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        proteinLen[line[0]] = int(line[1])

with open('ProteinFiles/DomainLength.txt') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        domainLen[line[0]] = int(line[1])

# find number of unique proteins and domains
proteins = dict(collections.Counter(proteinA + proteinB))
domains = dict(collections.Counter(domainA + domainB))

print('Number of unique proteins: ' + str(len(proteins)))
print('Number of unique domains: ' + str(len(domains)))

#find proteins/domains with 10+ Interactions
if(verbose):
    temp = {k:v for (k,v) in proteins.items() if v > 15}
    print('Proteins with 15+ interactions (' + str(len(temp)) + '):')
    printDict(temp)

    temp = {k:v for (k,v) in domains.items() if v > 15}
    print('Domains with 15+ interactions ('  + str(len(temp)) + '):')
    printDict(temp)

#import pdb; pdb.set_trace()

# plots
plt.figure(0)
plt.hist(list(proteins.values()), bins=50)
plt.title('Histogram of Interacting Proteins')
plt.xlabel('Number of Interactions')
plt.ylabel('Number of Proteins')
plt.grid(True)
plt.savefig('InteractionLists/stats/Proteins.png', bbox_inches='tight')
if(displayCharts): plt.show();

plt.figure(1)
plt.hist(list(domains.values()), bins=50)
plt.title('Histogram of Interacting Domains')
plt.xlabel('Number of Interactions')
plt.ylabel('Number of Domains')
plt.grid(True)
plt.savefig('InteractionLists/stats/Domains.png', bbox_inches='tight')
if(displayCharts): plt.show();

plt.figure(2)
plt.hist(list(domainLen.values()), bins=100)
plt.title('Domain Length')
plt.xlabel('Domain Length')
plt.ylabel('Number of Domains')
plt.grid(True)
plt.savefig('InteractionLists/stats/DomainLength.png', bbox_inches='tight')
if(displayCharts): plt.show();
