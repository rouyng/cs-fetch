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

    def _connectSignals(self):
        #self._view.clearbutton.clicked.connect(self._view.clearOutputText)
        self._view.searchbutton.clicked.connect(self.getcsinput)

    def getcsinput(self):
        self.csinput = self._view.searchinput.text()
         self._results = cf.fetchcallsigndata(session, self.csinput)
         if len(self._results) > 0:
             for k, v in self._results:
                 self._view.listWidget.addItem(f'<b>{k}</b>: {v}')

    def displaysession(self, sessionid):
        self._view.statusbar.showMessage(f'Session ID: {sessionid}', 0)


if __name__ == '__main__':
    configfile = 'cf.conf'
    session = cf.initialize(configfile)
    app = QtWidgets.QApplication([])
    application = cfMainWindow()
    application.show()
    controller = CfGuiControl(view=application.ui)
    controller.displaysession(session)
    sys.exit(app.exec_())