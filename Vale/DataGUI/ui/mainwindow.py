# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt6.QtCore import PYQT_VERSION_STR
from PyQt6.QtCore import pyqtSlot

import PyQt6.QtWidgets as QWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox

from .Ui_mainwindow import Ui_MainWindow

import sys
sys.path.append('../')
from dataprocess import DataProcess
from demoroutines import DemoRoutine

import platform
import numpy as np
import matplotlib
import scipy 
import pandas

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        
        self.proc = DataProcess()
        self.demo = DemoRoutine()
        
        self.gui_setup()

    def gui_setup(self):        
        hbox = self.demo.exampleMillPlot()
        self.frmDataPlot.setLayout(hbox)
        
        self.statusBar.showMessage("Idle")
        self.setFixedSize(1000, 800)
        #self.showFullScreen()  
        
    @pyqtSlot()
    def on_actionAboutQt_triggered(self):
        QWidgets.QMessageBox.aboutQt(self, "About Qt")

    @pyqtSlot()
    def on_actionAboutPython_triggered(self):
        pyver = "Python: " + platform.python_version() + " "
        pyver += platform.system() + " "
        pyver += platform.release() + " "
        pyver += "\n\n"
        
        npver = "NumPy: " + np.__version__ + "\n"
        qtver = "PyQt: " + PYQT_VERSION_STR + "\n"
        sciver = "SciPy: " + scipy.__version__ + "\n"
        pndver = "Pandas: " + pandas.__version__ + "\n"
        pltver = "Matplotlib: " +  matplotlib.__version__ + "\n"
        
        strversion = pyver + qtver + npver + sciver + pndver + pltver
        
        mbox = QMessageBox()
        mbox.setIcon(QMessageBox.Icon.Information)
        mbox.setText(strversion)
        mbox.setWindowTitle("Version")
        mbox.exec()
        
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        team = "Project Leader: Dr. Dhany Arifianto S.T M.Eng (dhany@ep.its.ac.id)\n"
        team += "\n"
        
        team += "Programmers:\n"
        team += "GUI Integrator: Achmadi ST MT (github.com/mekatronik-achmadi)\n"
        team += "Data Analysis : M. Ammar A. ST MT (github.com/maasyraf-project)\n"
        team += "Result Testing: A. Ainun Najib ST MT (github.com/iyyanf)\n"
        team += "Network System: Aprianto Dwi P ST MT (github.com/arkiven4)\n"
        
        mbox = QMessageBox()
        mbox.setIcon(QMessageBox.Icon.Information)
        mbox.setText(team)
        mbox.setWindowTitle("Team List")
        mbox.exec()
        
    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

    @pyqtSlot()
    def on_btnListDataset_pressed(self):
        self.demo.exampleErrorDisconnect()

    @pyqtSlot()
    def on_btnTestDataset_pressed(self):
        self.demo.exampleErrorDisconnect()

    @pyqtSlot()
    def on_btnFetchDataset_pressed(self):
        self.demo.exampleErrorDisconnect()

    @pyqtSlot()
    def on_btnShowCSV_pressed(self):
        self.demo.exampleErrorEmpty()

    @pyqtSlot()
    def on_btnModifyData_pressed(self):
        self.demo.exampleErrorEmpty()

    @pyqtSlot()
    def on_btnProcess_pressed(self):
        self.demo.exampleErrorUnimplemented()
