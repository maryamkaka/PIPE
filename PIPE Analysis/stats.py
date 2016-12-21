import pandas

distanceMeasure = pandas.read_table('ProteinFiles/distanceMeasure.txt')

#statistical summary
print(distanceMeasure.describe())

#create box plot
ax = distanceMeasure.boxplot()
fig = ax.get_figure()
# fig.title('Box Plot of Distance Measure Comparison of Binding Site Pridictors')
# fig.xlabel('PIPE Binding Site')
# fig.ylabel('Distance Measure')
fig.savefig('PIPE Analysis/distanceMeasure-BoxPlot.png', bbox_inches='tight')
