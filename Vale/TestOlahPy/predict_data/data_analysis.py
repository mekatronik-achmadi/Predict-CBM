# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

import pandas

from matplotlib.figure import Figure

class DataAnalysis():

    def __init__(self):
        super(DataAnalysis, self).__init__()

    def fig_map_corr(self,var_in):
        fig = Figure(figsize=(8,8),dpi=100)
        ax = fig.add_subplot(111)
        ax.matshow(var_in.corr())
        ax.set_xticks(range(var_in.select_dtypes(['number']).shape[1]),
                   var_in.select_dtypes(['number']).columns,
                   fontsize=6,
                   rotation=90)
        ax.set_yticks(range(var_in.select_dtypes(['number']).shape[1]),
                   var_in.select_dtypes(['number']).columns,
                   fontsize=6)
        #cbar = ax.colorbar()
        #cbar.ax.tick_params(labelsize=6)
        ax.set_title('Correlation Matrix', fontsize=16)

        return fig

