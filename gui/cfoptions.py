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
        OptionsWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        OptionsWindow.resize(422, 421)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OptionsWindow.sizePolicy().hasHeightForWidth())
        OptionsWindow.setSizePolicy(sizePolicy)
        OptionsWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.accountBox = QtWidgets.QGroupBox(OptionsWindow)
        self.accountBox.setGeometry(QtCore.QRect(10, 10, 211, 141))
        self.accountBox.setObjectName("accountBox")
        self.userField = QtWidgets.QLineEdit(self.accountBox)
        self.userField.setGeometry(QtCore.QRect(72, 30, 131, 20))
        self.userField.setObjectName("userField")
        self.pwField = QtWidgets.QLineEdit(self.accountBox)
        self.pwField.setGeometry(QtCore.QRect(72, 60, 131, 20))
        self.pwField.setInputMask("")
        self.pwField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwField.setClearButtonEnabled(False)
        self.pwField.setObjectName("pwField")
        self.userLabel = QtWidgets.QLabel(self.accountBox)
        self.userLabel.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.userLabel.setObjectName("userLabel")
        self.pwLabel = QtWidgets.QLabel(self.accountBox)
        self.pwLabel.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.pwLabel.setObjectName("pwLabel")
        self.qthlink = QtWidgets.QLabel(self.accountBox)
        self.qthlink.setGeometry(QtCore.QRect(10, 90, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.qthlink.setFont(font)
        self.qthlink.setTextFormat(QtCore.Qt.RichText)
        self.qthlink.setWordWrap(True)
        self.qthlink.setOpenExternalLinks(True)
        self.qthlink.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.qthlink.setObjectName("qthlink")
        self.okButton = QtWidgets.QPushButton(OptionsWindow)
        self.okButton.setGeometry(QtCore.QRect(240, 390, 75, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(OptionsWindow)
        self.cancelButton.setGeometry(QtCore.QRect(330, 390, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.scrollArea = QtWidgets.QScrollArea(OptionsWindow)
        self.scrollArea.setGeometry(QtCore.QRect(230, 20, 181, 361))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 160, 1103))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(3, 3, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.callsignBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.callsignBox.setObjectName("callsignBox")
        self.verticalLayout.addWidget(self.callsignBox)
        self.nickBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.nickBox.setObjectName("nickBox")
        self.verticalLayout.addWidget(self.nickBox)
        self.qthBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.qthBox.setObjectName("qthBox")
        self.verticalLayout.addWidget(self.qthBox)
        self.countryBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.countryBox.setObjectName("countryBox")
        self.verticalLayout.addWidget(self.countryBox)
        self.adifBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.adifBox.setObjectName("adifBox")
        self.verticalLayout.addWidget(self.adifBox)
        self.ituBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.ituBox.setObjectName("ituBox")
        self.verticalLayout.addWidget(self.ituBox)
        self.cqBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.cqBox.setObjectName("cqBox")
        self.verticalLayout.addWidget(self.cqBox)
        self.gridBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.gridBox.setObjectName("gridBox")
        self.verticalLayout.addWidget(self.gridBox)
        self.adrnameBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.adrnameBox.setObjectName("adrnameBox")
        self.verticalLayout.addWidget(self.adrnameBox)
        self.addr1Box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.addr1Box.setObjectName("addr1Box")
        self.verticalLayout.addWidget(self.addr1Box)
        self.adr2Box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.adr2Box.setObjectName("adr2Box")
        self.verticalLayout.addWidget(self.adr2Box)
        self.addr3Box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.addr3Box.setObjectName("addr3Box")
        self.verticalLayout.addWidget(self.addr3Box)
        self.cityBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.cityBox.setObjectName("cityBox")
        self.verticalLayout.addWidget(self.cityBox)
        self.zipBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.zipBox.setObjectName("zipBox")
        self.verticalLayout.addWidget(self.zipBox)
        self.countryBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.countryBox_2.setObjectName("countryBox_2")
        self.verticalLayout.addWidget(self.countryBox_2)
        self.adifaddrBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.adifaddrBox.setObjectName("adifaddrBox")
        self.verticalLayout.addWidget(self.adifaddrBox)
        self.districtBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.districtBox.setObjectName("districtBox")
        self.verticalLayout.addWidget(self.districtBox)
        self.stateBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.stateBox.setObjectName("stateBox")
        self.verticalLayout.addWidget(self.stateBox)
        self.countyBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.countyBox.setObjectName("countyBox")
        self.verticalLayout.addWidget(self.countyBox)
        self.oblastBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.oblastBox.setObjectName("oblastBox")
        self.verticalLayout.addWidget(self.oblastBox)
        self.dokBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.dokBox.setObjectName("dokBox")
        self.verticalLayout.addWidget(self.dokBox)
        self.iotaBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.iotaBox.setObjectName("iotaBox")
        self.verticalLayout.addWidget(self.iotaBox)
        self.qslBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.qslBox.setObjectName("qslBox")
        self.verticalLayout.addWidget(self.qslBox)
        self.lotwBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.lotwBox.setObjectName("lotwBox")
        self.verticalLayout.addWidget(self.lotwBox)
        self.eqslBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.eqslBox.setObjectName("eqslBox")
        self.verticalLayout.addWidget(self.eqslBox)
        self.qslbBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.qslbBox.setObjectName("qslbBox")
        self.verticalLayout.addWidget(self.qslbBox)
        self.directqslBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.directqslBox.setObjectName("directqslBox")
        self.verticalLayout.addWidget(self.directqslBox)
        self.emailBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.emailBox.setObjectName("emailBox")
        self.verticalLayout.addWidget(self.emailBox)
        self.jabberBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.jabberBox.setObjectName("jabberBox")
        self.verticalLayout.addWidget(self.jabberBox)
        self.icqBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.icqBox.setObjectName("icqBox")
        self.verticalLayout.addWidget(self.icqBox)
        self.msnBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.msnBox.setObjectName("msnBox")
        self.verticalLayout.addWidget(self.msnBox)
        self.skypeBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.skypeBox.setObjectName("skypeBox")
        self.verticalLayout.addWidget(self.skypeBox)
        self.birthyearBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.birthyearBox.setObjectName("birthyearBox")
        self.verticalLayout.addWidget(self.birthyearBox)
        self.licenseyearBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.licenseyearBox.setObjectName("licenseyearBox")
        self.verticalLayout.addWidget(self.licenseyearBox)
        self.photoBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.photoBox.setObjectName("photoBox")
        self.verticalLayout.addWidget(self.photoBox)
        self.latBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.latBox.setObjectName("latBox")
        self.verticalLayout.addWidget(self.latBox)
        self.longBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.longBox.setObjectName("longBox")
        self.verticalLayout.addWidget(self.longBox)
        self.contBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.contBox.setObjectName("contBox")
        self.verticalLayout.addWidget(self.contBox)
        self.utcBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.utcBox.setObjectName("utcBox")
        self.verticalLayout.addWidget(self.utcBox)
        self.fbookBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.fbookBox.setObjectName("fbookBox")
        self.verticalLayout.addWidget(self.fbookBox)
        self.twitBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.twitBox.setObjectName("twitBox")
        self.verticalLayout.addWidget(self.twitBox)
        self.gplusBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.gplusBox.setObjectName("gplusBox")
        self.verticalLayout.addWidget(self.gplusBox)
        self.utubeBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.utubeBox.setObjectName("utubeBox")
        self.verticalLayout.addWidget(self.utubeBox)
        self.linkedBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.linkedBox.setObjectName("linkedBox")
        self.verticalLayout.addWidget(self.linkedBox)
        self.flickrBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.flickrBox.setObjectName("flickrBox")
        self.verticalLayout.addWidget(self.flickrBox)
        self.vimeoBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.vimeoBox.setObjectName("vimeoBox")
        self.verticalLayout.addWidget(self.vimeoBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.dbBox = QtWidgets.QGroupBox(OptionsWindow)
        self.dbBox.setGeometry(QtCore.QRect(10, 160, 211, 121))
        self.dbBox.setObjectName("dbBox")
        self.qthButton = QtWidgets.QRadioButton(self.dbBox)
        self.qthButton.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.qthButton.setObjectName("qthButton")
        self.qrzButton = QtWidgets.QRadioButton(self.dbBox)
        self.qrzButton.setEnabled(False)
        self.qrzButton.setGeometry(QtCore.QRect(10, 50, 82, 31))
        self.qrzButton.setCheckable(True)
        self.qrzButton.setObjectName("qrzButton")
        self.fccButton = QtWidgets.QRadioButton(self.dbBox)
        self.fccButton.setEnabled(False)
        self.fccButton.setGeometry(QtCore.QRect(10, 80, 171, 31))
        self.fccButton.setCheckable(True)
        self.fccButton.setObjectName("fccButton")
        self.label = QtWidgets.QLabel(OptionsWindow)
        self.label.setGeometry(QtCore.QRect(240, 0, 121, 21))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(OptionsWindow)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 211, 91))
        self.groupBox.setObjectName("groupBox")
        self.lightButton = QtWidgets.QRadioButton(self.groupBox)
        self.lightButton.setGeometry(QtCore.QRect(10, 20, 83, 21))
        self.lightButton.setChecked(True)
        self.lightButton.setObjectName("lightButton")
        self.darkButton = QtWidgets.QRadioButton(self.groupBox)
        self.darkButton.setGeometry(QtCore.QRect(10, 57, 83, 21))
        self.darkButton.setObjectName("darkButton")

        self.retranslateUi(OptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Options"))
        self.accountBox.setTitle(_translate("OptionsWindow", "Account"))
        self.userLabel.setText(_translate("OptionsWindow", "Username"))
        self.pwLabel.setText(_translate("OptionsWindow", "Password"))
        self.qthlink.setText(_translate("OptionsWindow", "<html><head/><body><p>Required for using HamQTH database<br/>Create an account at <a href=\"https://www.hamqth.com/register.php\"><span style=\" text-decoration: underline; color:#0000ff;\">HamQTH.com</span></a></p></body></html>"))
        self.okButton.setText(_translate("OptionsWindow", "Ok"))
        self.cancelButton.setText(_translate("OptionsWindow", "Cancel"))
        self.callsignBox.setText(_translate("OptionsWindow", "Callsign"))
        self.nickBox.setText(_translate("OptionsWindow", "Nickname"))
        self.qthBox.setText(_translate("OptionsWindow", "QTH"))
        self.countryBox.setText(_translate("OptionsWindow", "Country"))
        self.adifBox.setText(_translate("OptionsWindow", "ADIF ID"))
        self.ituBox.setText(_translate("OptionsWindow", "ITU"))
        self.cqBox.setText(_translate("OptionsWindow", "CQ (WAZ) zone"))
        self.gridBox.setText(_translate("OptionsWindow", "Grid Square"))
        self.adrnameBox.setText(_translate("OptionsWindow", "Name (from address)"))
        self.addr1Box.setText(_translate("OptionsWindow", "Address 1"))
        self.adr2Box.setText(_translate("OptionsWindow", "Address 2"))
        self.addr3Box.setText(_translate("OptionsWindow", "Address 3"))
        self.cityBox.setText(_translate("OptionsWindow", "City"))
        self.zipBox.setText(_translate("OptionsWindow", "Zip/postal code"))
        self.countryBox_2.setText(_translate("OptionsWindow", "Country (from address)"))
        self.adifaddrBox.setText(_translate("OptionsWindow", "ADIF (from address)"))
        self.districtBox.setText(_translate("OptionsWindow", "District"))
        self.stateBox.setText(_translate("OptionsWindow", "State (USA)"))
        self.countyBox.setText(_translate("OptionsWindow", "County (USA)"))
        self.oblastBox.setText(_translate("OptionsWindow", "Oblast (RUS)"))
        self.dokBox.setText(_translate("OptionsWindow", "DOK"))
        self.iotaBox.setText(_translate("OptionsWindow", "IOTA #"))
        self.qslBox.setText(_translate("OptionsWindow", "QSL Info"))
        self.lotwBox.setText(_translate("OptionsWindow", "Uses LOTW?"))
        self.eqslBox.setText(_translate("OptionsWindow", "Uses EQSL?"))
        self.qslbBox.setText(_translate("OptionsWindow", "Accept QSL via bureau?"))
        self.directqslBox.setText(_translate("OptionsWindow", "Accept direct QSL card?"))
        self.emailBox.setText(_translate("OptionsWindow", "Email address"))
        self.jabberBox.setText(_translate("OptionsWindow", "Jabber"))
        self.icqBox.setText(_translate("OptionsWindow", "ICQ"))
        self.msnBox.setText(_translate("OptionsWindow", "MSN"))
        self.skypeBox.setText(_translate("OptionsWindow", "Skype"))
        self.birthyearBox.setText(_translate("OptionsWindow", "Year of birth"))
        self.licenseyearBox.setText(_translate("OptionsWindow", "Licensed since"))
        self.photoBox.setText(_translate("OptionsWindow", "URL to user\'s photo"))
        self.latBox.setText(_translate("OptionsWindow", "Latitude"))
        self.longBox.setText(_translate("OptionsWindow", "Longitude"))
        self.contBox.setText(_translate("OptionsWindow", "Continent"))
        self.utcBox.setText(_translate("OptionsWindow", "Offset to UTC time"))
        self.fbookBox.setText(_translate("OptionsWindow", "Facebook URL"))
        self.twitBox.setText(_translate("OptionsWindow", "Twitter URL"))
        self.gplusBox.setText(_translate("OptionsWindow", "Google Plus URL"))
        self.utubeBox.setText(_translate("OptionsWindow", "YouTube URL"))
        self.linkedBox.setText(_translate("OptionsWindow", "LinkedIn URL"))
        self.flickrBox.setText(_translate("OptionsWindow", "Flickr URL"))
        self.vimeoBox.setText(_translate("OptionsWindow", "Vimeo URL"))
        self.dbBox.setTitle(_translate("OptionsWindow", "Database"))
        self.qthButton.setText(_translate("OptionsWindow", "HamQTH.com"))
        self.qrzButton.setText(_translate("OptionsWindow", "QRZ.com"))
        self.fccButton.setText(_translate("OptionsWindow", "FCC ULS (USA callsigns only)"))
        self.label.setText(_translate("OptionsWindow", "Select fields to display"))
        self.groupBox.setTitle(_translate("OptionsWindow", "Theme"))
        self.lightButton.setText(_translate("OptionsWindow", "Light"))
        self.darkButton.setText(_translate("OptionsWindow", "Dark"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptionsWindow = QtWidgets.QWidget()
    ui = Ui_OptionsWindow()
    ui.setupUi(OptionsWindow)
    OptionsWindow.show()
    sys.exit(app.exec_())
