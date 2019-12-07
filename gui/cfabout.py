# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cf-about.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(400, 169)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutDialog.sizePolicy().hasHeightForWidth())
        aboutDialog.setSizePolicy(sizePolicy)
        aboutDialog.setWhatsThis("")
        self.okButton = QtWidgets.QPushButton(aboutDialog)
        self.okButton.setGeometry(QtCore.QRect(160, 130, 75, 23))
        self.okButton.setObjectName("okButton")
        self.titleLabel = QtWidgets.QLabel(aboutDialog)
        self.titleLabel.setGeometry(QtCore.QRect(160, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.authorLabel = QtWidgets.QLabel(aboutDialog)
        self.authorLabel.setGeometry(QtCore.QRect(130, 30, 121, 21))
        self.authorLabel.setObjectName("authorLabel")
        self.githubLabel = QtWidgets.QLabel(aboutDialog)
        self.githubLabel.setGeometry(QtCore.QRect(20, 70, 131, 21))
        self.githubLabel.setOpenExternalLinks(True)
        self.githubLabel.setObjectName("githubLabel")
        self.apiLabel = QtWidgets.QLabel(aboutDialog)
        self.apiLabel.setGeometry(QtCore.QRect(180, 70, 201, 21))
        self.apiLabel.setOpenExternalLinks(True)
        self.apiLabel.setObjectName("apiLabel")

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About Cs-Fetch"))
        self.okButton.setText(_translate("aboutDialog", "Ok"))
        self.titleLabel.setText(_translate("aboutDialog", "Cs-Fetch"))
        self.authorLabel.setText(_translate("aboutDialog", "by Ross Young, KJ7GES"))
        self.githubLabel.setText(_translate("aboutDialog", "<a href=\"https://github.com/rouyng/callsign-fetch\">View this project on GitHub</a>"))
        self.apiLabel.setText(_translate("aboutDialog", "<html><head/><body><p>This software uses the <a href=\"https://www.hamqth.com/developers.php\"><span style=\" text-decoration: underline; color:#0000ff;\">HamQTH.com API</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutDialog = QtWidgets.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())
