import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import cf
from gui.cfguimain import Ui_MainWindow


class cfMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(cfMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class CfGuiControl:
    """Cs-Fetch GUI controller class"""
    def __init__(self, view, configurationfile):
        self._view = view
        self._configfile = configurationfile
        self._results = {}
        self._labelfont = QtGui.QFont()
        self._labelfont.setBold(True)
        self._connectSignals()
        self._result_data = {'Welcome to CS-Fetch!' : 'Enter a callsign and press "Search" to begin'}
        self._csinput = None
        self._filltable(self._result_data)

    def _connectSignals(self):
        self._view.searchbutton.clicked.connect(self._getcsinput)
        self._view.actionAbout.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://github.com/rouyng/callsign-fetch')))
        self._view.actionExit.triggered.connect(lambda: sys.exit())
        self._view.searchinput.returnPressed.connect(self._view.searchbutton.click)

    def _getcsinput(self):
        self._view.resultsTable.clear()
        self._csinput = self._view.searchinput.text()
        self._result_data = {}
        if not cf.validatecallsign(self._csinput):
            self._results = cf.fetchcallsigndata(session, self._csinput)
            for key in cf.get_fields_to_print(self._configfile):
                if key in self._results.keys() & cf.field_labels.keys():
                    self._result_data[cf.field_labels[key]] = self._results[key]
            self._filltable(self._result_data)
        else:
            self._view.statusbar.showMessage(cf.validatecallsign(self._csinput))
            self._view.searchinput.clear()

    def _filltable(self, data):
        self._view.resultsTable.setColumnCount(2)
        self._view.resultsTable.setRowCount(len(data))
        for i, k in enumerate(data):
            label_item = QtWidgets.QTableWidgetItem(f'{k}')
            label_item.setFont(self._labelfont)
            self._view.resultsTable.setItem(i, 0, label_item)
            if k == 'Callsign':
                self._view.resultsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(data[k].upper()))
            else:
                self._view.resultsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(data[k]))

    def displaysession(self, sessionid):
        self._view.statusbar.showMessage(f'Session ID: {sessionid}', 0)

# TODO: additional widget for adjusting options within GUI
# TODO: additional widget for "About" menu item
# TODO: session timeout/error handling
# TODO: progress/status info in status bar

if __name__ == '__main__':
    configfile = 'cf.conf'
    app = QtWidgets.QApplication([])
    application = cfMainWindow()
    application.show()
    controller = CfGuiControl(view=application.ui, configurationfile=configfile)
    session = cf.initialize(configfile)
    if not session:
        print(f'Could not find configuration file, please check that {configfile} exists')
        sys.exit()
    else:
        controller.displaysession(session)
    sys.exit(app.exec_())


