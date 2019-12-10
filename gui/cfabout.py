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
        aboutDialog.resize(411, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutDialog.sizePolicy().hasHeightForWidth())
        aboutDialog.setSizePolicy(sizePolicy)
        aboutDialog.setWhatsThis("")
        self.okButton = QtWidgets.QPushButton(aboutDialog)
        self.okButton.setGeometry(QtCore.QRect(170, 200, 75, 23))
        self.okButton.setObjectName("okButton")
        self.titleLabel = QtWidgets.QLabel(aboutDialog)
        self.titleLabel.setGeometry(QtCore.QRect(170, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.label = QtWidgets.QLabel(aboutDialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 391, 161))
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About Cs-Fetch"))
        self.okButton.setText(_translate("aboutDialog", "Ok"))
        self.titleLabel.setText(_translate("aboutDialog", "Cs-Fetch"))
        self.label.setText(_translate("aboutDialog", "<p>Cs-Fetch  is a simple amateur radio callsign lookup tool, created by Ross Young, KJ7GES. For more information, please see README.md, or <a href=\"https://github.com/rouyng/callsign-fetch\">visit Cs-Fetch on GitHub</a>. This is free, open source software built with Python. Bug reports and code contributions are welcomed through the above mentioned GitHub repository.</p>  \n"
"<p>Cs-Fetch uses the <a href=\"https://www.hamqth.com/developers.php\">HamQTH.com API</a> to look up details on amateur radio callsigns. Cs-Fetch is an independent project and is not otherwise associated with HamQTH.com or its staff.\n"
"<p> This software is licensed under the conditions of <a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\">the GNU GPL v3</a>. See LICENSE.md for details.</p>\n"
"\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutDialog = QtWidgets.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())
