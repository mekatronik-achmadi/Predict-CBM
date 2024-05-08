#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import PyQt6.QtWidgets

from ValePredictPI.vale_gui import ValeGui

class TestValeGui():
    def __init__(self):
        super(TestValeGui, self).__init__()

        vale_ui = ValeGui()

if __name__ == "__main__":
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    ui = ValeGui()
    ui.show()
    sys.exit(app.exec())