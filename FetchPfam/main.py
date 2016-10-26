from retrievePfam import retrievePfam

outputFile = open('ProteinFiles/ProteinPfam.txt', 'w')
inputFile = open('ProteinFiles/protein_list.txt', 'r')

for line in inputFile:
    protein = line.strip()
    pfam = retrievePfam(protein)

    print(protein + ' ' + pfam + '\n')
    outputFile.write(protein + ' ' + pfam + '\n')
