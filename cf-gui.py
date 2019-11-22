import sys
from timeit import default_timer as timer

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
        self._result_data = {'Welcome to Cs-Fetch!': 'Enter a callsign and press "Search"'}
        self._csinput = None
        self._session = None
        self._start = None
        self._end = None
        self._fillTable(self._result_data)
        self._InitializeSession()

    def _InitializeSession(self):
        self._session = cf.initialize(self._configfile)
        if not self._session:
            print(f'Could not find configuration file, please check that {self._configfile} exists')
            sys.exit()
        else:
            self._sessionStatus(self._session)


    def _connectSignals(self):
        self._view.searchbutton.clicked.connect(self._getCallsignInput)
        self._view.actionAbout.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://github.com/rouyng/callsign-fetch')))
        self._view.actionExit.triggered.connect(lambda: sys.exit())
        self._view.searchinput.returnPressed.connect(self._view.searchbutton.click)

    def _getCallsignInput(self):
        self._view.resultsTable.clear()
        self._view.resultsTable.setColumnCount(0)
        self._view.resultsTable.setRowCount(0)
        self._csinput = self._view.searchinput.text()
        self._result_data = {}
        if not cf.validatecallsign(self._csinput):
            # if user's input passes validation, cf.validatecallsign returns False, and we can query the API
            start = timer()  # start timing api fetch
            self._progressStatus(self._csinput)
            self._results = cf.fetchcallsigndata(self._session, self._csinput)
            end = timer()  # end timing api fetch
            if self._results.__class__ == str:
                # if the results of cf.fetchcallsigndata() are a string, the API has produced an error
                self._view.resultsTable.setColumnCount(0)
                self._view.resultsTable.setRowCount(0)
                self._errorStatus(self._results)
                if 'Session does not exist or expired' in self._results:
                    cf.initialize(self._configfile)
            else:
                for key in cf.get_fields_to_print(self._configfile):
                    if key in self._results.keys() & cf.field_labels.keys():
                        self._result_data[cf.field_labels[key]] = self._results[key]
                self._fillTable(self._result_data)
                self._view.resultsTable.resizeColumnsToContents()
                self._timerStatus(end - start)
        else:
            self._view.statusbar.showMessage(cf.validatecallsign(self._csinput))
            self._view.searchinput.clear()

    def _fillTable(self, data):
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

    def _sessionStatus(self, sessionid):
        self._view.statusbar.showMessage(f'Session ID: {sessionid}', 0)

    def _errorStatus(self, error_text):
        self._view.statusbar.showMessage(f'Error: {error_text}', 0) # show error in status bar for 5 sec

    def _timerStatus(self, time):
        self._view.statusbar.showMessage(f'Retrieved callsign info in {time: .2f} seconds', 0)

    def _progressStatus(self, entered_callsign):
        self._view.statusbar.showMessage(f'Retrieving information about {entered_callsign}', 0)

# TODO: additional widget for adjusting options within GUI
# TODO: additional widget for "About" menu item
# TODO: copy results to clipboard button
# TODO: icons for window and task bar

if __name__ == '__main__':
    configfile = 'cf.conf'
    app = QtWidgets.QApplication([])
    application = cfMainWindow()
    application.show()
    controller = CfGuiControl(view=application.ui, configurationfile=configfile)
    sys.exit(app.exec_())


