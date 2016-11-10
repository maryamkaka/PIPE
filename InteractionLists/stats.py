import collections
import matplotlib.pyplot as plt
import numpy as np

#variables
displayCharts = 0

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

print('Number of unique proteins: ' + str(len(proteins)))
print('Number of unique domains: ' + str(len(domains)))

#import pdb; pdb.set_trace()

# plots
plt.figure(0)
plt.hist(list(proteins.values()), bins=50)
plt.title('Histogram of Interacting Proteins')
plt.xlabel('Number of Interactions')
plt.ylabel('Number of Proteins')
plt.grid(True)
plt.savefig('InteractionLists/Figures/Proteins.png', bbox_inches='tight')
if(displayCharts): plt.show();

plt.figure(1)
plt.hist(list(domains.values()), bins=50)
plt.title('Histogram of Interacting Domains')
plt.xlabel('Number of Interactions')
plt.ylabel('Number of Domains')
plt.grid(True)
plt.savefig('InteractionLists/Figures/Domains.png', bbox_inches='tight')
if(displayCharts): plt.show();
