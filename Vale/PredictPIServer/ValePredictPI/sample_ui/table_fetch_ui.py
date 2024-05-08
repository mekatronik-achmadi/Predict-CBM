# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_fetch.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainGui(object):
    def setupUi(self, MainGui):
        MainGui.setObjectName("MainGui")
        MainGui.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainGui)
        self.centralwidget.setObjectName("centralwidget")
        self.tabMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tabMain.setGeometry(QtCore.QRect(10, 10, 1181, 541))
        self.tabMain.setObjectName("tabMain")
        self.tabData = QtWidgets.QWidget()
        self.tabData.setObjectName("tabData")
        self.grpTable = QtWidgets.QGroupBox(self.tabData)
        self.grpTable.setGeometry(QtCore.QRect(0, 110, 1001, 381))
        self.grpTable.setStyleSheet("QGroupBox{border: 2px solid gray; border-radius: 3px;}")
        self.grpTable.setObjectName("grpTable")
        self.txtTagA = QtWidgets.QLineEdit(self.grpTable)
        self.txtTagA.setGeometry(QtCore.QRect(10, 30, 181, 24))
        self.txtTagA.setObjectName("txtTagA")
        self.txtTagB = QtWidgets.QLineEdit(self.grpTable)
        self.txtTagB.setGeometry(QtCore.QRect(340, 30, 181, 24))
        self.txtTagB.setObjectName("txtTagB")
        self.txtTagC = QtWidgets.QLineEdit(self.grpTable)
        self.txtTagC.setGeometry(QtCore.QRect(670, 30, 181, 24))
        self.txtTagC.setObjectName("txtTagC")
        self.tblDataA = QtWidgets.QTableView(self.grpTable)
        self.tblDataA.setGeometry(QtCore.QRect(10, 60, 311, 311))
        self.tblDataA.setObjectName("tblDataA")
        self.tblDataC = QtWidgets.QTableView(self.grpTable)
        self.tblDataC.setGeometry(QtCore.QRect(340, 60, 311, 311))
        self.tblDataC.setObjectName("tblDataC")
        self.tblDataB = QtWidgets.QTableView(self.grpTable)
        self.tblDataB.setGeometry(QtCore.QRect(670, 60, 311, 311))
        self.tblDataB.setObjectName("tblDataB")
        self.grpSource = QtWidgets.QGroupBox(self.tabData)
        self.grpSource.setGeometry(QtCore.QRect(0, 10, 421, 91))
        self.grpSource.setStyleSheet("QGroupBox{border: 2px solid gray; border-radius: 3px;}")
        self.grpSource.setObjectName("grpSource")
        self.txtDataServer = QtWidgets.QLineEdit(self.grpSource)
        self.txtDataServer.setGeometry(QtCore.QRect(80, 20, 241, 24))
        self.txtDataServer.setObjectName("txtDataServer")
        self.lblDataServer = QtWidgets.QLabel(self.grpSource)
        self.lblDataServer.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.lblDataServer.setObjectName("lblDataServer")
        self.lblDataBase = QtWidgets.QLabel(self.grpSource)
        self.lblDataBase.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.lblDataBase.setObjectName("lblDataBase")
        self.txtDataBase = QtWidgets.QLineEdit(self.grpSource)
        self.txtDataBase.setGeometry(QtCore.QRect(80, 50, 241, 24))
        self.txtDataBase.setObjectName("txtDataBase")
        self.btnServerStart = QtWidgets.QPushButton(self.grpSource)
        self.btnServerStart.setGeometry(QtCore.QRect(330, 20, 85, 51))
        self.btnServerStart.setObjectName("btnServerStart")
        self.tabMain.addTab(self.tabData, "")
        self.tabPlot = QtWidgets.QWidget()
        self.tabPlot.setObjectName("tabPlot")
        self.tabMain.addTab(self.tabPlot, "")
        MainGui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainGui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainGui)
        self.statusbar.setObjectName("statusbar")
        MainGui.setStatusBar(self.statusbar)
        self.actionStart = QtWidgets.QAction(MainGui)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainGui)
        self.actionStop.setObjectName("actionStop")
        self.actionExit = QtWidgets.QAction(MainGui)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainGui)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QtWidgets.QAction(MainGui)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menuFile.addAction(self.actionStart)
        self.menuFile.addAction(self.actionStop)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainGui)
        self.tabMain.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainGui)

    def retranslateUi(self, MainGui):
        _translate = QtCore.QCoreApplication.translate
        MainGui.setWindowTitle(_translate("MainGui", "MainWindow"))
        self.grpTable.setTitle(_translate("MainGui", "Data Tables"))
        self.txtTagA.setText(_translate("MainGui", "U-LGS1-GB-X-PK-PK-70-AI"))
        self.txtTagB.setText(_translate("MainGui", "U-LGS1-TGB-X-PK-PK-270-AI"))
        self.txtTagC.setText(_translate("MainGui", "U-LGS1-UGB-X-PK-PK-70-AI"))
        self.grpSource.setTitle(_translate("MainGui", "Data Source"))
        self.txtDataServer.setText(_translate("MainGui", "142.40.33.208"))
        self.lblDataServer.setText(_translate("MainGui", "Data Server "))
        self.lblDataBase.setText(_translate("MainGui", "Data Base"))
        self.txtDataBase.setText(_translate("MainGui", "pti-pi"))
        self.btnServerStart.setText(_translate("MainGui", "Start"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabData), _translate("MainGui", "Data"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabPlot), _translate("MainGui", "tabPlot"))
        self.menuFile.setTitle(_translate("MainGui", "File"))
        self.menuAbout.setTitle(_translate("MainGui", "Help"))
        self.actionStart.setText(_translate("MainGui", "Start"))
        self.actionStop.setText(_translate("MainGui", "Stop"))
        self.actionExit.setText(_translate("MainGui", "Exit"))
        self.actionAbout.setText(_translate("MainGui", "About"))
        self.actionAbout_Qt.setText(_translate("MainGui", "About-Qt"))
