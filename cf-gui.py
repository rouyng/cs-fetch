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
        self._connectSignals()
        self._csinput = None

    def _connectSignals(self):
        self._view.searchbutton.clicked.connect(self.getcsinput)
        self._view.actionAbout.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://github.com/rouyng/callsign-fetch')))
        self._view.actionExit.triggered.connect(lambda: sys.exit())
        self._view.searchinput.returnPressed.connect(self._view.searchbutton.click)

    def getcsinput(self):
        self._view.listWidget.clear()
        self._csinput = self._view.searchinput.text()
        if not cf.validatecallsign(self._csinput):
            self._results = cf.fetchcallsigndata(session, self._csinput)
            if len(self._results) > 0:
                for key in cf.get_fields_to_print(self._configfile):
                    if key in self._results.keys() & cf.field_labels.keys():
                        item = f'{cf.field_labels[key]}: {self._results[key]}'
                        self._view.listWidget.addItem(item)
            else:
                self._view.listWidget.addItem('No result found!')
        else:
            self._view.listWidget.addItem(cf.validatecallsign(self._csinput))
            self._view.searchinput.clear()

    def displaysession(self, sessionid):
        self._view.statusbar.showMessage(f'Session ID: {sessionid}', 0)


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


