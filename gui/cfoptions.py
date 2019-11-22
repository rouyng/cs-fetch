# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cf_options_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(400, 300)
        OptionsWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.accountBox = QtWidgets.QGroupBox(OptionsWindow)
        self.accountBox.setGeometry(QtCore.QRect(0, 0, 211, 111))
        self.accountBox.setObjectName("accountBox")
        self.userField = QtWidgets.QLineEdit(self.accountBox)
        self.userField.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.userField.setObjectName("userField")
        self.pwField = QtWidgets.QLineEdit(self.accountBox)
        self.pwField.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.pwField.setInputMask("")
        self.pwField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwField.setClearButtonEnabled(False)
        self.pwField.setObjectName("pwField")
        self.userLabel = QtWidgets.QLabel(self.accountBox)
        self.userLabel.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.userLabel.setObjectName("userLabel")
        self.label_2 = QtWidgets.QLabel(self.accountBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.accountBox)
        self.label.setGeometry(QtCore.QRect(20, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.okButton = QtWidgets.QPushButton(OptionsWindow)
        self.okButton.setGeometry(QtCore.QRect(230, 270, 75, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(OptionsWindow)
        self.cancelButton.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(OptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Options"))
        self.accountBox.setTitle(_translate("OptionsWindow", "Account"))
        self.userLabel.setText(_translate("OptionsWindow", "Username"))
        self.label_2.setText(_translate("OptionsWindow", "Password"))
        self.label.setText(_translate("OptionsWindow", "Create an account at <a href=\"https://www.hamqth.com/register.php\">HamQTH.com</a>"))
        self.okButton.setText(_translate("OptionsWindow", "Ok"))
        self.cancelButton.setText(_translate("OptionsWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptionsWindow = QtWidgets.QWidget()
    ui = Ui_OptionsWindow()
    ui.setupUi(OptionsWindow)
    OptionsWindow.show()
    sys.exit(app.exec_())
