# -*- coding: utf-8 -*-

import sys

sys.path.append('../ValePredictPI/')
sys.path.append('../ValePredictPI/sample_ui/')

from PyQt5.QtCore import pyqtSlot

import PyQt5.QtWidgets as QWidgets
from PyQt5.QtWidgets import QMainWindow

from PyQt5 import QtCore

from pyqt_pandas_model import PandasModel

from table_fetch_ui import Ui_MainGui
from vale_connect import ValeConnect

class MainGui(QMainWindow,Ui_MainGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.tmrReqApi = QtCore.QTimer(self)
        self.tmrReqApi.timeout.connect(self.update_table)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.conn = ValeConnect(self.txtDataServer.text(),self.txtDataBase.text())
        self.tmrReqApi.start(1000)

    def update_table(self):
        print("================")

        tags_list = [self.txtTagA, self.txtTagB, self.txtTagC]
        table_list = [self.tblDataA, self.tblDataB, self.tblDataC]

        for i in range(3):
            df = self.conn.get_stream_rec_valuetime_pd(self.conn.get_webid_point(tags_list[i].text()))
            dfmodel = PandasModel(df)
            table_list[i].setModel(dfmodel)
            table_list[i].resizeColumnsToContents()

        print('Updated')

if __name__ == "__main__":
    app = QWidgets.QApplication(sys.argv)
    ui = MainGui()
    ui.show()
    sys.exit(app.exec())