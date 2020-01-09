import matplotlib.pyplot as plt
import numpy as np

class im_plotter(object):
    def __init__(self, nr_rows = 1, nr_cols = 1, figsize = (5,5)):
        self.fig, self.ax = plt.subplots(nrows = nr_rows, ncols = nr_cols,
                                         figsize=figsize, squeeze=False)
        self.index = 0
        self.nr_rows = nr_rows
        self.nr_cols = nr_cols

    def plot_img(self, img, label = "", cmap = 'gray', ax_label = 'off'):
        if self.index == self.nr_rows*self.nr_cols : return
        self.ax[self.index//self.nr_cols][self.index%self.nr_cols].imshow(img, cmap = cmap)
        self.ax[self.index//self.nr_cols][self.index%self.nr_cols].set_title(label)
        self.ax[self.index//self.nr_cols][self.index%self.nr_cols].axis(ax_label)
        self.index+=1

    def save_plot(self, file_name):
        plt.savefig(file_name)
