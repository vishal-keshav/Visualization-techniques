import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns

import numpy as np

# Demostrate the basic infra of using pyplot
# Single graph plot only contour plots in 3D
def main():
    sns.set()# Sets the seaborn clear plot formatting
    print(plt.style.available)
    #plt.style.use('seaborn-white') # Sets the plot style
    #plt.xkcd()# for cartoonized plots
    fig = plt.figure() #Container for axes, graphics, etxt, labels etc.
    ax = plt.axes(projection='3d') # Visual boundng box element

    # Else below method can be used for getting both for sublots
    #fig, ax = plt.subplots(2) # here ax is a list of axeses

    # Plot two lines in one axes.
    x = np.linspace(0,10,1000)
    y = np.linspace(0,10,1000)
    x,y = np.meshgrid(x,y)
    z = x*np.sin(x) + y*np.cos(y)

    im = ax.plot_surface(x,y,z, cmap = 'viridis', edgecolor='black')
    fig.colorbar(im)

    # Setting other charectestics of the plot
    # X lable and y label should have 5% of emapy space on each side
    x_range_offset = (x.max() - x.min())*(5.0/100.0)
    y_range_offset = (y.max()-y.min())*(5.0/100.0)
    xlim = (x.min()-x_range_offset, x.max()+x_range_offset)
    ylim = (y.min() - y_range_offset, y.max() + y_range_offset)
    ax.set(xlim = xlim, ylim = ylim, xlabel = "x", ylabel="y", title = "sample")
    #ax.legend()
    plt.show()# This should be in the last
    #plt.savefig('figure.pdf') # Comment one of the show or savefig

if __name__ == "__main__":
    main()
