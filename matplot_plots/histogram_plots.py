import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

# Demostrate the basic infra of using pyplot
# Single graph plot only contour plots
def main():
    sns.set()# Sets the seaborn clear plot formatting
    #print(plt.style.available)
    plt.style.use('seaborn-white') # Sets the plot style
    #plt.xkcd()# for cartoonized plots
    fig = plt.figure() #Container for axes, graphics, etxt, labels etc.
    ax = plt.axes() # Visual boundng box element

    # Else below method can be used for getting both for sublots
    #fig, ax = plt.subplots(2) # here ax is a list of axeses

    # Plot two lines in one axes.
    x1 = np.random.normal(0,4,10000)
    x2 = np.random.normal(-2,1,10000)
    x3 = np.random.normal(4,4,10000)

    ax.hist(x1, histtype = 'stepfilled', alpha = 0.4, bins = 100)
    ax.hist(x2, histtype = 'stepfilled', alpha = 0.4, bins = 100)
    ax.hist(x3, histtype = 'stepfilled', alpha = 0.4, bins = 100)

    # Setting other charectestics of the plot
    # X lable and y label should have 5% of emapy space on each side
    #x_range_offset = (x.max() - x.min())*(5.0/100.0)
    #y_range_offset = (y.max()-y.min())*(5.0/100.0)
    #xlim = (x.min()-x_range_offset, x.max()+x_range_offset)
    #ylim = (y.min() - y_range_offset, y.max() + y_range_offset)
    #ax.set(xlim = xlim, ylim = ylim, xlabel = "x", ylabel="y", title = "sample")
    #ax.legend()
    plt.show()# This should be in the last
    #plt.savefig('figure.pdf') # Comment one of the show or savefig

if __name__ == "__main__":
    main()
