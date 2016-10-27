#load ProteinPfam into dictionary
pfam = {}
with open('ProteinFiles/ProteinPfam.txt') as f:
    for line in f:
        line = line.strip('\n').split(' ')
        pfam[line[0]] = line[1:-1]

#Load interactingDomainPairs info
interactingDomains = {}
with open('ProteinFiles/interactingDomainPairs.txt') as f:
    for line in f:
        line = line.replace('\n', '').split(' ')

        if(line[0] in interactingDomains):
            interactingDomains[line[0]].append(line[1])
        else:
            interactingDomains[line[0]] = [line[1]]

        if(line[1] in interactingDomains):
            interactingDomains[line[1]].append(line[0])
        else:
            interactingDomains[line[1]] = [line[0]]

#determine interacting domains for protein pair
with open('ProteinFiles/protein_pairs.txt') as f:
    domainMatch = []
    one = open('InteractionLists/one.txt', 'w')
    none = open('InteractionLists/none.txt', 'w')
    multi = open('InteractionLists/multi.txt', 'w')

    for line in f:
        domainMatch.append([])

        line = line.strip('\n').replace(' ', '').split('\t')
        proteinA = pfam[line[0]]
        proteinB = pfam[line[1]]

        #check for interacting domains
        for dA in proteinA:
            if(~(dA in interactingDomains)):    #break if current doamin has no interacting pairs
                continue

            AInteractions = interactingDomains[dA]
            for dB in proteinB:
                if(dB in AInteractions):
                    domainMatch[-1].append([dA, dB])

        #output to file
        if(len(domainMatch[-1])):
            one.write(line[0] + '\t' + line[1] + '\n')
        elif(len(domainMatch[-1]) == 0):
            none.write(line[0] + '\t' + line[1]+ '\n')
        else:
            multi.write(line[0] + '\t' + line[1]+ '\n')
