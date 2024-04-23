# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

import pandas

from matplotlib.figure import Figure

## Data Analysis and Processing class
class DataAnalysis():

    ## Constructor
    def __init__(self):
        super(DataAnalysis, self).__init__()

    ## Correlation Map generator
    # @param var_in Pandas DataFrame
    # @return Figure object
    def fig_map_corr(self,var_in):
        """ Build Correlation Map Figure
        """
        fig = Figure(figsize=(8,8),dpi=100)
        ax = fig.add_subplot(111)
        im = ax.matshow(var_in.corr())
        ax.set_xticks(range(var_in.select_dtypes(['number']).shape[1]),
                   var_in.select_dtypes(['number']).columns,
                   fontsize=6,
                   rotation=90)
        ax.set_yticks(range(var_in.select_dtypes(['number']).shape[1]),
                   var_in.select_dtypes(['number']).columns,
                   fontsize=6)
        fig.colorbar(im,orientation='vertical')

        return fig

