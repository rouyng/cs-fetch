# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cf-options.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(400, 303)
        OptionsWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.accountBox = QtWidgets.QGroupBox(OptionsWindow)
        self.accountBox.setGeometry(QtCore.QRect(10, 10, 211, 111))
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
        self.pwLabel = QtWidgets.QLabel(self.accountBox)
        self.pwLabel.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.pwLabel.setObjectName("pwLabel")
        self.qthlink = QtWidgets.QLabel(self.accountBox)
        self.qthlink.setGeometry(QtCore.QRect(20, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.qthlink.setFont(font)
        self.qthlink.setTextFormat(QtCore.Qt.RichText)
        self.qthlink.setWordWrap(True)
        self.qthlink.setOpenExternalLinks(True)
        self.qthlink.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.qthlink.setObjectName("qthlink")
        self.okButton = QtWidgets.QPushButton(OptionsWindow)
        self.okButton.setGeometry(QtCore.QRect(230, 270, 75, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(OptionsWindow)
        self.cancelButton.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.scrollArea = QtWidgets.QScrollArea(OptionsWindow)
        self.scrollArea.setGeometry(QtCore.QRect(240, 20, 151, 241))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 130, 1072))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout.addWidget(self.checkBox_9)
        self.checkBox_37 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_37.setObjectName("checkBox_37")
        self.verticalLayout.addWidget(self.checkBox_37)
        self.checkBox_18 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout.addWidget(self.checkBox_18)
        self.checkBox_39 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_39.setObjectName("checkBox_39")
        self.verticalLayout.addWidget(self.checkBox_39)
        self.checkBox_20 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout.addWidget(self.checkBox_20)
        self.checkBox_16 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout.addWidget(self.checkBox_16)
        self.checkBox_28 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_28.setObjectName("checkBox_28")
        self.verticalLayout.addWidget(self.checkBox_28)
        self.checkBox_38 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_38.setObjectName("checkBox_38")
        self.verticalLayout.addWidget(self.checkBox_38)
        self.checkBox_45 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_45.setObjectName("checkBox_45")
        self.verticalLayout.addWidget(self.checkBox_45)
        self.checkBox_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout.addWidget(self.checkBox_13)
        self.checkBox_25 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_25.setObjectName("checkBox_25")
        self.verticalLayout.addWidget(self.checkBox_25)
        self.checkBox_27 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_27.setObjectName("checkBox_27")
        self.verticalLayout.addWidget(self.checkBox_27)
        self.checkBox_33 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_33.setObjectName("checkBox_33")
        self.verticalLayout.addWidget(self.checkBox_33)
        self.checkBox_24 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_24.setObjectName("checkBox_24")
        self.verticalLayout.addWidget(self.checkBox_24)
        self.checkBox_43 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_43.setObjectName("checkBox_43")
        self.verticalLayout.addWidget(self.checkBox_43)
        self.checkBox_40 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_40.setObjectName("checkBox_40")
        self.verticalLayout.addWidget(self.checkBox_40)
        self.checkBox_44 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_44.setObjectName("checkBox_44")
        self.verticalLayout.addWidget(self.checkBox_44)
        self.checkBox_35 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_35.setObjectName("checkBox_35")
        self.verticalLayout.addWidget(self.checkBox_35)
        self.checkBox_19 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout.addWidget(self.checkBox_19)
        self.checkBox_29 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_29.setObjectName("checkBox_29")
        self.verticalLayout.addWidget(self.checkBox_29)
        self.checkBox_30 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_30.setObjectName("checkBox_30")
        self.verticalLayout.addWidget(self.checkBox_30)
        self.checkBox_26 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_26.setObjectName("checkBox_26")
        self.verticalLayout.addWidget(self.checkBox_26)
        self.checkBox_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout.addWidget(self.checkBox_15)
        self.checkBox_31 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_31.setObjectName("checkBox_31")
        self.verticalLayout.addWidget(self.checkBox_31)
        self.checkBox_46 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_46.setObjectName("checkBox_46")
        self.verticalLayout.addWidget(self.checkBox_46)
        self.checkBox_21 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_21.setObjectName("checkBox_21")
        self.verticalLayout.addWidget(self.checkBox_21)
        self.checkBox_36 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_36.setObjectName("checkBox_36")
        self.verticalLayout.addWidget(self.checkBox_36)
        self.checkBox_42 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_42.setObjectName("checkBox_42")
        self.verticalLayout.addWidget(self.checkBox_42)
        self.checkBox_23 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_23.setObjectName("checkBox_23")
        self.verticalLayout.addWidget(self.checkBox_23)
        self.checkBox_41 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_41.setObjectName("checkBox_41")
        self.verticalLayout.addWidget(self.checkBox_41)
        self.checkBox_17 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout.addWidget(self.checkBox_17)
        self.checkBox_14 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout.addWidget(self.checkBox_14)
        self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout.addWidget(self.checkBox_10)
        self.checkBox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout.addWidget(self.checkBox_12)
        self.checkBox_22 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_22.setObjectName("checkBox_22")
        self.verticalLayout.addWidget(self.checkBox_22)
        self.checkBox_32 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_32.setObjectName("checkBox_32")
        self.verticalLayout.addWidget(self.checkBox_32)
        self.checkBox_34 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_34.setObjectName("checkBox_34")
        self.verticalLayout.addWidget(self.checkBox_34)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(OptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Options"))
        self.accountBox.setTitle(_translate("OptionsWindow", "Account"))
        self.userLabel.setText(_translate("OptionsWindow", "Username"))
        self.pwLabel.setText(_translate("OptionsWindow", "Password"))
        self.qthlink.setText(_translate("OptionsWindow", "Create an account at <a href=\"https://www.hamqth.com/register.php\">HamQTH.com</a>"))
        self.okButton.setText(_translate("OptionsWindow", "Ok"))
        self.cancelButton.setText(_translate("OptionsWindow", "Cancel"))
        self.checkBox.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_9.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_37.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_18.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_39.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_20.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_16.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_28.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_38.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_45.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_13.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_25.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_27.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_33.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_24.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_43.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_40.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_44.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_35.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_19.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_29.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_30.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_26.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_15.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_31.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_46.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_21.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_36.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_42.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_23.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_41.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_17.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_14.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_10.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_11.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_12.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_22.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_32.setText(_translate("OptionsWindow", "CheckBox"))
        self.checkBox_34.setText(_translate("OptionsWindow", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptionsWindow = QtWidgets.QWidget()
    ui = Ui_OptionsWindow()
    ui.setupUi(OptionsWindow)
    OptionsWindow.show()
    sys.exit(app.exec_())