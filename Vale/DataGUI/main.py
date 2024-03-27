#!/usr/bin/python
# -*- coding: utf-8 -*-

import PyQt6.QtWidgets 
from ui.mainwindow import MainWindow

if __name__ == "__main__":
    import sys
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())
