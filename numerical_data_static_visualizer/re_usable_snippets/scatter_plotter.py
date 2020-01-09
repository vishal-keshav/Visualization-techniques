import matplotlib.pyplot as plt
import numpy as np

class scatter(object):
    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes()

    def plot_scatter(self, x, y, c= None, cmap=None):
        self.ax.scatter(x,y,c = c, cmap = cmap)

    def save_plot(self, file_name):
        plt.savefig(file_name)
