# -*- coding: utf-8 -*-

from matplotlib import style
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import PyQt6.QtWidgets as QWidgets
from PyQt6.QtWidgets import QMessageBox

import numpy as np
import scipy.io as sio
import pandas as pd

class DemoRoutine():
    def __init__(self,  parent=None):
        pass

    def exampleMillPlot(self):
        """
        Milling Data Source:
        https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
        """
        
        m = sio.loadmat('dataset/mill/mill.mat',struct_as_record=True)
        data = m['mill']
        l = data.dtype.names
        df_labels = pd.DataFrame()
        for i in range(7):
            # list for storing the label data for each field
            x = []
    
            # iterate through each of the unique cuts
            for j in range(167):
                x.append(data[0,j][i][0][0])
            x = np.array(x)
            df_labels[str(i)] = x

        # add column names to the dataframe
        df_labels.columns = l[0:7]
    
        # create a column with the unique cut number
        df_labels['cut_no'] = [i for i in range(167)]
        
        fig, ax = plt.subplots(2)

        ax[0].plot(data[0,166]['smcAC'],'g-',label='smcAC')
        ax[0].plot(data[0,166]['smcDC'],color='orange',label='smcDC')
        ax[1].plot(data[0,105]['smcAC'],'g-',label='smcAC')
        ax[1].plot(data[0,105]['smcDC'],color='orange',label='smcDC')
        
        plt.legend()
        
        style.use('ggplot')
        self.canvas = FigureCanvas(fig)
        self.canvas.draw()
        
        hbox = QWidgets.QHBoxLayout()
        hbox.addWidget(self.canvas)
        
        return hbox
        
    def exampleErrorDisconnect(self):
        mbox = QMessageBox()
        mbox.setIcon(QMessageBox.Icon.Critical)
        mbox.setText("Server Disconnected")
        mbox.setWindowTitle("Error")
        mbox.exec()
        
    def exampleErrorEmpty(self):
        mbox = QMessageBox()
        mbox.setIcon(QMessageBox.Icon.Critical)
        mbox.setText("Empty Data")
        mbox.setWindowTitle("Error")
        mbox.exec()
        
    def exampleErrorUnimplemented(self):
        mbox = QMessageBox()
        mbox.setIcon(QMessageBox.Icon.Critical)
        mbox.setText("Sadly, Not Implemented")
        mbox.setWindowTitle("Error")
        mbox.exec()
