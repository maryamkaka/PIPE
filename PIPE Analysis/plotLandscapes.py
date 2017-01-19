from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy

landscapeLocation = 'pipe_results/landscapes/'
outputLocation = 'ProteinFiles/landscapes/'
landscapeList = os.listdir(landscapeLocation)

for landscape in landscapeList:
    print(landscape)

    data = pd.read_csv(landscapeLocation + landscape, sep=' ', header=None)
    data.as_matrix()

    plt.figure()
    plt.imshow(data, cmap='gray_r')
    plt.savefig(outputLocation+ landscape[0:-4] + '.png', bbox_inches='tight')
    plt.close()

    ny, nx = data.shape
    hf = plt.figure()
    ha = hf.add_subplot(111, projection='3d')
    X, Y = numpy.meshgrid(range(nx), range(ny))
    ha.plot_surface(X, Y, data, cmap='cool')
    plt.savefig(outputLocation + landscape[0:-4] + '-3D.png', bbox_inches='tight')
    plt.close()
