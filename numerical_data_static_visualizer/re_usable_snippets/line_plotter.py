import matplotlib.pyplot as plt
import numpy as np

class plotter(object):
    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.labels = []

    def plot_data(self, x, y, color = (1.0, 0.0, 0.0), linestyle='-',
                                    xlabel = "x", ylabel = "y", label = 'plot'):
        self.ax.plot(x, y, color = color, linestyle=linestyle, label = label)
        #self.ax.set_xticks(x[::10])
        #self.ax.set_xticklabels(x[::10], rotation=45)
        self.ax.set(xlabel = xlabel, ylabel=ylabel)
        self.labels.append(label)

    def save_plot(self, file_name):
        self.ax.legend(self.labels)
        plt.savefig(file_name)
