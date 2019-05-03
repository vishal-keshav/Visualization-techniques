import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

# Demostrate the basic infra of using pyplot
# Single graph plot only scatter points
def main():
    sns.set()# Sets the seaborn clear plot formatting
    #print(plt.style.available)
    plt.style.use('seaborn-whitegrid') # Sets the plot style
    #plt.xkcd()# for cartoonized plots
    fig = plt.figure() #Container for axes, graphics, etxt, labels etc.
    ax = plt.axes() # Visual boundng box element

    # Else below method can be used for getting both for sublots
    #fig, ax = plt.subplots(2) # here ax is a list of axeses

    # Plot two lines in one axes.
    x = np.linspace(0,10,10)
    y1 = np.sin(x)
    y2 = 1.3*np.cos(x)
    # Scatter plot from plot
    """ax.plot(x, y1, 'X', color = (1.0, 0.0, 0.0),
                markersize=12, markerfacecolor= (0.0,0.0,1.0),
                markeredgecolor = (0.0,1.0,0.0), markeredgewidth = 0.5,
                label = 'sin plot', alpha = 0.7)"""
    #ax.plot(x, y2, color = (0.0,1.0,0.0), linestyle='--X', label = 'cos plot')
    im = ax.scatter(x, y1, c = y1, s = 1000*(y1+1), alpha = 0.7,
                        cmap = 'plasma', label = 'sin')
    # cmap = 'viridis' s also a good choice
    fig.colorbar(im) # Color bar is a property of figure having all axeses

    # Setting other charectestics of the plot
    # X lable and y label should have 5% of emapy space on each side
    x_range_offset = (x.max() - x.min())*(5.0/100.0)
    y_range_offset = max((y1.max()-y1.min()),(y2.max()-y2.min()))*(5.0/100.0)
    xlim = (x.min()-x_range_offset, x.max()+x_range_offset)
    ylim = (min(y1.min(), y2.min())-y_range_offset,
                    max(y1.max(), y2.max()) + y_range_offset)
    ax.set(xlim = xlim, ylim = ylim, xlabel = "x", ylabel="y", title = "sample")
    ax.legend()
    #plt.show()# This should be in the last
    plt.savefig('figure.pdf') # Comment one of the show or savefig

if __name__ == "__main__":
    main()
