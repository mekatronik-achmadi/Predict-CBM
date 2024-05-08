#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import PyQt5.QtWidgets as QWidgets

from ValePredictPI.sample_ui.table_fetch_app import MainGui

server_root = '142.40.33.208'
server_base = 'pti-pi'

if __name__ == "__main__":
    app = QWidgets.QApplication(sys.argv)
    ui = MainGui()
    ui.api_connect(server_root,server_base)
    ui.show()
    sys.exit(app.exec())
