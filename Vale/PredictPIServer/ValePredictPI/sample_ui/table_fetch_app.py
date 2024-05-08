# -*- coding: utf-8 -*-

import sys

sys.path.append('../ValePredictPI/')
sys.path.append('../ValePredictPI/sample_ui/')

from PyQt5.QtCore import pyqtSlot

import PyQt5.QtWidgets as QWidgets
from PyQt5.QtWidgets import QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

from table_fetch_ui import Ui_MainGui
from vale_connect import ValeConnect

class MainGui(QMainWindow,Ui_MainGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None

    def api_connect(self,server_path,base_path):
        self.conn = ValeConnect(server_path,base_path)

if __name__ == "__main__":
    app = QWidgets.QApplication(sys.argv)
    ui = MainGui()
    ui.show()
    sys.exit(app.exec())