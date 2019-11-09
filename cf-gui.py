import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QTextEdit


class cfgui(QMainWindow):
    """Mail CSFetch application window"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('CSFetch')
        self.setGeometry(200, 200, 400, 200)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.layout = QGridLayout()
        self.layout.addWidget(QLabel("Welcome to CSFetch!"), 0, 0, 1, 2)
        self._centralWidget.setLayout(self.layout)
        self._createMenu()
        self._createStatusBar()
        self._createcsentry()
        self._createsearchbutton()
        self._createclearbutton()
        self._createsearchoutput()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&File")
        self.menu = self.menuBar().addMenu("&Options")

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Here is the status bar.")
        self.setStatusBar(status)

    def _createcsentry(self):
        self.csentry = QLineEdit('Callsign')
        self.layout.addWidget(self.csentry, 1, 0)

    def _createsearchbutton(self):
        self.searchbutton = QPushButton('Search')
        self.layout.addWidget(self.searchbutton, 1, 1)

    def _createclearbutton(self):
        self.clearbutton = QPushButton('Clear')
        self.layout.addWidget(self.clearbutton, 3, 0, 1, 2)

    def _createsearchoutput(self):
        self.searchoutput = QTextEdit()
        self.searchoutput.setReadOnly(True)
        self.searchoutput.setFixedHeight(100)
        self.layout.addWidget(self.searchoutput, 2, 0, 1, 2)

    def setOutputText(self, text):
        self.searchoutput.setText(text)

    def appendOutputText(self, text):
        self.searchoutput.append(text)

    def clearOutputText(self):
        self.setOutputText('')

class cfguicontrol:
    """Cs-Fetch GUI controller class"""
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _connectSignals(self):
        #self._view.searchbutton.clicked.connect()
        self._view.clearbutton.clicked.connect(self._view.clearOutputText)
        self._view.searchbutton.clicked.connect(self.getcsinput)

    def getcsinput(self):
        csinput = self._view.csentry.text()
        print(csinput)

if __name__ == '__main__':
    app = QApplication([])
    gui = cfgui()
    gui.show()
    gui.setOutputText('Hello World!')
    controller = cfguicontrol(view=gui)
    sys.exit(app.exec_())