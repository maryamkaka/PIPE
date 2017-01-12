from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy

landscapeLocation = '../pipe_results/landscapes/'
outputLocation = '../ProteinFiles/landscapes/'
landscapeList = os.listdir(landscapeLocation)

#for landscape in landscapeList:
    #plt.figure(0)
    #plt.hist(list(proteins.values()), bins=50)
    #plt.title(landscape)
    #plt.xlabel()
    #plt.ylabel()
    #plt.grid(True)
    #plt.savefig('.png', bbox_inches='tight')

data = pd.read_csv(landscapeLocation + "A5YKK6-O75175.mat", sep=' ', header=None)
data.as_matrix()

# Set up grid and test data
nx, ny = 735,2357
x = range(nx)
y = range(ny)

hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')

X, Y = numpy.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D
ha.plot_surface(X, Y, data, cmap=cm.coolwarm)

plt.show()