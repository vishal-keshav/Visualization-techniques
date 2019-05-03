import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Demostrate the basic infra of using pyplot
# Single graph plot only error graph
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
    y1 = x*np.sin(x)
    y2 = 1.3*np.cos(x)

    kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
    #gp = GaussianProcess(corr = 'cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1,
    #                                                        random_start=100)
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=30)
    gp.fit(x[:,np.newaxis], y1)
    x_pred = np.linspace(0, 10,1000)
    y_pred, std = gp.predict(x_pred[:, np.newaxis], return_std = True)
    # Calculate 2*sigma == 95% confidance
    diff = 2*np.sqrt(std)

    ax.plot(x, y1, color = (1.0,0.0,0.0), marker = 'o', alpha = 0.8,
                                                    label = 'raw_data')
    ax.plot(x_pred, y_pred, color = (0.0,1.0,0.0), linestyle = '--',
                                                    label = 'gassian fit data')
    ax.fill_between(x_pred, y_pred - diff, y_pred + diff,color='grey',
                                            alpha=0.5, label = 'error')

    # Setting other charectestics of the plot
    # X lable and y label should have 5% of emapy space on each side
    x_range_offset = (x.max() - x.min())*(5.0/100.0)
    y_range_offset = max((y1.max()-y1.min()),(y2.max()-y2.min()))*(5.0/100.0)
    xlim = (x.min()-x_range_offset, x.max()+x_range_offset)
    ylim = (min(y1.min(), y2.min())-y_range_offset,
                    max(y1.max(), y2.max()) + y_range_offset)
    ax.set(xlim = xlim, ylim = ylim, xlabel = "x", ylabel="y", title = "sample")
    ax.legend()
    plt.show()# This should be in the last
    #plt.savefig('figure.pdf') # Comment one of the show or savefig

if __name__ == "__main__":
    main()
