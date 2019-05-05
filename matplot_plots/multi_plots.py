import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
sns.set()

def main():
    # demonstrates the multi-plots with multiple axes in the same figure
    plt.style.use('seaborn-white')
    # get the figure
    fig = plt.figure(figsize=(100,100))
    # Create three axes in the figure for plotting [left, top, width, height]
    """ax1 = fig.add_axes([0.1, 0.65, 0.25, 0.25], xticklabels=[], yticklabels=[])
    ax2 = fig.add_axes([0.35, 0.35, 0.25, 0.25], xticklabels=['a','b','c'])
    ax3 = fig.add_axes([0.65, 0.1, 0.25, 0.25], yticklabels=['p','q','r','s'])
    ax1.set(xlim = (0.0, 1.0), ylim = (0.0, 1.0))
    ax2.set(xlim = (0.0, 2.0), ylim = (0.0, 2.0))
    ax3.set(xlim = (0.0, 3.0), ylim = (0.0, 3.0))"""

    """x = np.linspace(0,10,1000)
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    ax = fig.subplots(3,4, sharex = 'col', sharey = 'row')
    for i in range(3):
        for j in range(4):
            ax[i][j].plot(x,np.sin(x+i+j))
            ax[i][j].set(xticklabels = [], yticklabels = [])"""

    mean = [0,0]
    cov = [[1,2],[1,3]]
    x,y = np.random.multivariate_normal(mean, cov, 10000).T
    print(x.shape, y.shape)
    grid = plt.GridSpec(6,6,hspace=0.2, wspace=0.2)
    # Start addiing axes, gridspec will manage the assymetrc number of axes
    ax1 = fig.add_subplot(grid[0:5,0:5])# 5/6th of the space from left and top
    ax2 = fig.add_subplot(grid[5:6,0:5], xticklabels = [], yticklabels = [])
    ax3 = fig.add_subplot(grid[0:5,5:6], xticklabels = [], yticklabels = [])
    ax1.plot(x,y,'h', markersize=20, alpha = 0.3)
    ax2.hist(x, bins = 100, histtype = 'stepfilled', orientation = 'vertical',
                                    color = (0.2, 0.2, 0.5), alpha = 0.4)
    ax3.hist(y, bins = 100, histtype='stepfilled', orientation = 'horizontal',
                                    color = (0.2, 0.2, 0.5), alpha = 0.4)
    ax2.invert_yaxis()

    #plt.show()
    plt.savefig("sample.pdf")



if __name__ == "__main__":
    main()
