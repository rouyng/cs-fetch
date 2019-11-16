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
    def __init__(self, view):
        self._view = view
        self._results = {}
        self._connectSignals()
        self._csinput = None

    def _connectSignals(self):
        self._view.searchbutton.clicked.connect(self.getcsinput)
        self._view.actionAbout.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://github.com/rouyng/callsign-fetch')))
        self._view.actionExit.triggered.connect(lambda: sys.exit())

    def getcsinput(self):
        self._view.listWidget.clear()
        self._csinput = self._view.searchinput.text()
        if cf.validatecallsign(self._csinput) == False:
            self._results = cf.fetchcallsigndata(session, self._csinput)
            if len(self._results) > 0:
                for k, v in self._results.items():
                    item = f'{k.title()}: {v}'
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
    controller = CfGuiControl(view=application.ui)
    session = cf.initialize(configfile)
    if not session:
        print(f'Could not find configuration file, please check that {configfile} exists')
        sys.exit()
    else:
        controller.displaysession(session)
    sys.exit(app.exec_())


