#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import PyQt5.QtWidgets as QWidgets

from ValePredictPI.sample_ui.table_fetch_app import MainGui

if __name__ == "__main__":
    app = QWidgets.QApplication(sys.argv)
    ui = MainGui()
    ui.show()
    sys.exit(app.exec())
