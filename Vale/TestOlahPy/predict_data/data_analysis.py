# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

import matplotlib.pyplot as plt

class DataAnalysis():

    def __init__(self):
        super(DataAnalysis, self).__init__()

    def map_corr(self,var_in):
        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        fig = plt.figure(figsize=(40,30))
        plt.matshow(var_in.corr(),fignum=fig.number)
        plt.xticks(range(var_in.select_dtypes(['number']).shape[1]),
                   var_in.select_dtypes(['number']).columns,
                   fontsize=14,
                   rotation=45)
        plt.yticks(range(var_in.select_dtypes(['number']).shape[1]),
                   var_in.select_dtypes(['number']).columns,
                   fontsize=14)
        cbar = plt.Colorbar()
        cbar.ax.tick_params(labelsize=14)
        plt.title('Correlation Matrix', fontsize=16)

