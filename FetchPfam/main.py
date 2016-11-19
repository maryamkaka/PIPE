from getPfam import pfamConnect as getPfam

outputFile = open('ProteinFiles/ProteinPfam.txt', 'w')
inputFile = open('ProteinFiles/protein_list.txt', 'r')

for line in inputFile:
    protein = line.strip()
    pfam = getPfam(protein)

    print(protein + ' ' + ' '.join(pfam) + '\n')
    outputFile.write(protein + ' ' + ' '.join(pfam) + '\n')
