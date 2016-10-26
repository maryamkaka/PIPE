inputFile = open('Accessing_3did/3did_flat', 'r')
outputFile = open('ProteinFiles/interactingDomainPairs.txt', 'w')

for line in inputFile:
    line = line.replace(' ', '').split('\t')

    if(line[0] == '#=ID'):
        domain1 = line[3].split('.')[0].replace('(', '')
        domain2 = line[4].split('.')[0]

        print(domain1 + ' ' + domain2)
        outputFile.write(domain1 + ' ' + domain2 + '\n')

inputFile.close()
outputFile.close()
