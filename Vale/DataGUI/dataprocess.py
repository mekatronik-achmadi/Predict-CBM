# -*- coding: utf-8 -*-

from matplotlib import style
from matplotlib.figure import Figure
import matplotlib.animation as animation	
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import PyQt6.QtWidgets as QWidgets

import numpy as np

class DataProcess():
    
    def __init__(self,  parent=None):
        pass
        
    def examplePlot(self):
        self.X = np.arange(0, 10, 0.1)
        self.Y = np.sin(self.X)
        
        self.fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('white')
        self.ax.grid(True,which='both',ls='-')
        self.ax.clear()
        self.line, = self.ax.plot(self.X, self.Y)
        
        style.use('ggplot')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        
        hbox = QWidgets.QHBoxLayout()
        hbox.addWidget(self.canvas)
        
        self.ani = animation.FuncAnimation(self.fig, self.graphupdate, interval=1, repeat=False,  cache_frame_data=False)
        self.ani._start()
        
        return hbox

    def graphupdate(self,args):
        self.line.set_data(self.X,self.Y)
