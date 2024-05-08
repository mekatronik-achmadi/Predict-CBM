# -*- coding: utf-8 -*-

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Ui_Main(object):

    def initUi(self,ValeGui):
        ValeGui.setObjectName('Main Gui')
        ValeGui.resize(1024,600)
        QtCore.QMetaObject.connectSlotsByName(ValeGui)

class ValeGui(QMainWindow,Ui_Main):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUi(self)
