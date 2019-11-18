# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cf-gui-main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.searchinput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchinput.setText("")
        self.searchinput.setObjectName("searchinput")
        self.gridLayout.addWidget(self.searchinput, 0, 0, 1, 1)
        self.resultsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.resultsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.resultsTable.setAlternatingRowColors(True)
        self.resultsTable.setColumnCount(2)
        self.resultsTable.setObjectName("resultsTable")
        self.resultsTable.setRowCount(0)
        self.resultsTable.horizontalHeader().setVisible(True)
        self.resultsTable.horizontalHeader().setDefaultSectionSize(200)
        self.resultsTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.resultsTable, 1, 0, 1, 2)
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setAutoDefault(True)
        self.searchbutton.setDefault(False)
        self.searchbutton.setObjectName("searchbutton")
        self.gridLayout.addWidget(self.searchbutton, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReadme = QtWidgets.QAction(MainWindow)
        self.actionReadme.setObjectName("actionReadme")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.menuFile.addAction(self.actionOptions)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchinput.setPlaceholderText(_translate("MainWindow", "Enter callsign here..."))
        self.searchbutton.setText(_translate("MainWindow", "Search"))
        self.menuFile.setTitle(_translate("MainWindow", "Menu"))
        self.actionReadme.setText(_translate("MainWindow", "Readme"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
