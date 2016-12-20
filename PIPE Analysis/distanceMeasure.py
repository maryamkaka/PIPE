import pandas
import math

# import dataframes
pipe = pandas.read_table('pipe_results/output/human.out')
prediction = pandas.read_table('InteractionLists/singleDomain.txt')
domainLen = pandas.read_table('ProteinFiles/length.txt')

output = open('ProteinFiles/distanceMeasure.txt', 'w')
output.write('ProteinA\tProteinB\tDM1\tDM2\tDM3\n')

#calculate distance measure
def distanceMeasure(aLab, aPipe, aLen, bLab, bPipe, bLen):
    dA = max(aLab[0] - aPipe[0], aLab[1] - aPipe[1], 0)/aLen
    dB = max(bLab[0] - bPipe[0], bLab[1] - bPipe[1], 0)/bLen
    return math.sqrt(math.pow(dA, 2) + math.pow(dB, 2))/math.sqrt(2)

#walk through prediction and compare with pipe
for index, row in prediction.iterrows():
    aInfo = domainLen[(domainLen.Protein == row.ProteinA) & (domainLen.Domain == row.DomainA)]
    bInfo = domainLen[(domainLen.Protein == row.ProteinB) & (domainLen.Domain == row.DomainB)]
    pipeInfo = pipe[(pipe.protein_a == row.ProteinA) & (pipe.protein_b == row.ProteinB)]

    #extract interaction sites
    aLab = [aInfo.DomainStart.item(), aInfo.DomainEnd.item()]
    bLab = [bInfo.DomainStart.item(), bInfo.DomainEnd.item()]

    aPipe1 = [pipeInfo.site1a_start.item(), pipeInfo.site1a_end.item()]
    bPipe1 = [pipeInfo.site1b_start.item(), pipeInfo.site1b_end.item()]

    aPipe2 = [pipeInfo.site2a_start.item(), pipeInfo.site2a_end.item()]
    bPipe2 = [pipeInfo.site2b_start.item(), pipeInfo.site2b_end.item()]

    aPipe3 = [pipeInfo.site3a_start.item(), pipeInfo.site3a_end.item()]
    bPipe3 = [pipeInfo.site3b_start.item(), pipeInfo.site3b_end.item()]

    #calculate distance measures
    DM1 = distanceMeasure(aLab, aPipe1, aInfo.ProteinLength.item(), bLab, bPipe1, bInfo.ProteinLength.item())
    DM2 = distanceMeasure(aLab, aPipe2, aInfo.ProteinLength.item(), bLab, bPipe2, bInfo.ProteinLength.item())
    DM3 = distanceMeasure(aLab, aPipe3, aInfo.ProteinLength.item(), bLab, bPipe3, bInfo.ProteinLength.item())

    #write to file
    string = row.ProteinA + '\t' + row.ProteinB + '\t' + str(DM1) + '\t' + str(DM2) + '\t' + str(DM3) + '\n'
    print(string)
    output.write(string)
