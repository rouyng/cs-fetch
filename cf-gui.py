import sys
from timeit import default_timer as timer

from PyQt5 import QtCore, QtGui, QtWidgets

import cf
from gui.cfguimain import Ui_MainWindow
from gui.cfoptions import Ui_OptionsWindow


class cfMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(cfMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class cfOptionsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(cfOptionsWindow, self).__init__()
        self.ui = Ui_OptionsWindow()
        self.ui.setupUi(self)


class OptionsGuiControl:
    """Cs-Fetch options window gui contoller class"""
    def __init__(self, widget, view, configuration_file):
        self._view = view
        self._widget = widget
        self._configfile = configuration_file
        self._load_config(self._configfile)
        self._connect_signals()

    def _connect_signals(self):
        self._view.okButton.clicked.connect(lambda: self._save_config(self._configfile))
        self._view.cancelButton.clicked.connect(lambda: self._cancel())

    def _load_config(self, file):
        # load options from cf.conf and display them in appropriate widgets
        pass

    def _save_config(self, file):
        # save options from GUI to cf.conf, hide view and reinitialize
        self._widget.close()

    def _cancel(self):
        # hide view and reload config from file when cancel button is pressed
        self._widget.close()
        self._load_config(self._configfile)


class CfGuiControl:
    """Cs-Fetch main window GUI controller class"""
    def __init__(self, view, options_view, configuration_file):
        self._view = view
        self._configfile = configuration_file
        self._options_view = options_view
        self._results = {}
        self._labelfont = QtGui.QFont()
        self._labelfont.setBold(True)
        self._connect_signals()
        self._result_data = {'Welcome to Cs-Fetch!': 'Enter a callsign and press "Search"'}
        self._csinput = None
        self._session = None
        self._start = None
        self._end = None
        self._fill_results_table(self._result_data)
        self._initialize_session()

    def _initialize_session(self):
        self._session = cf.initialize(self._configfile)
        if not self._session:
            print(f'Could not find configuration file, please check that {self._configfile} exists')
            sys.exit()
        else:
            self._show_session_status(self._session)


    def _connect_signals(self):
        self._view.searchbutton.clicked.connect(self._process_callsign_input)
        self._view.actionAbout.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://github.com/rouyng/callsign-fetch')))
        self._view.actionExit.triggered.connect(lambda: sys.exit())
        self._view.actionOptions.triggered.connect(lambda: self._options_view.show())
        self._view.searchinput.returnPressed.connect(self._view.searchbutton.click)

    def _process_callsign_input(self):
        self._view.resultsTable.clear()
        self._view.resultsTable.setColumnCount(0)
        self._view.resultsTable.setRowCount(0)
        self._csinput = self._view.searchinput.text()
        self._result_data = {}
        if not cf.validatecallsign(self._csinput):
            # if user's input passes validation, cf.validatecallsign returns False, and we can query the API
            start = timer()  # start timing api fetch
            self._show_progress_status(self._csinput)
            self._results = cf.fetchcallsigndata(self._session, self._csinput)
            end = timer()  # end timing api fetch
            if self._results.__class__ == str:
                # if the results of cf.fetchcallsigndata() are a string, the API has produced an error
                self._view.resultsTable.setColumnCount(0)
                self._view.resultsTable.setRowCount(0)
                self._show_error_status(self._results)
                if 'Session does not exist or expired' in self._results:
                    cf.initialize(self._configfile)
            else:
                for key in cf.get_fields_to_print(self._configfile):
                    if key in self._results.keys() & cf.field_labels.keys():
                        self._result_data[cf.field_labels[key]] = self._results[key]
                self._fill_results_table(self._result_data)
                self._view.resultsTable.resizeColumnsToContents()
                self._show_timer_status(end - start)
        else:
            self._view.statusbar.showMessage(cf.validatecallsign(self._csinput))
            self._view.searchinput.clear()

    def _fill_results_table(self, data):
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

    def _show_session_status(self, sessionid):
        self._view.statusbar.showMessage(f'Session ID: {sessionid}', 0)

    def _show_error_status(self, error_text):
        self._view.statusbar.showMessage(f'Error: {error_text}', 0) # show error in status bar for 5 sec

    def _show_timer_status(self, time):
        self._view.statusbar.showMessage(f'Retrieved callsign info in {time: .2f} seconds', 0)

    def _show_progress_status(self, entered_callsign):
        self._view.statusbar.showMessage(f'Retrieving information about {entered_callsign}', 0)

# TODO: additional widget for adjusting options within GUI
# TODO: additional widget for "About" menu item
# TODO: copy results to clipboard button
# TODO: icons for window and task bar

if __name__ == '__main__':
    configfile = 'cf.conf'
    app = QtWidgets.QApplication([])
    app_main = cfMainWindow()
    app_options = cfOptionsWindow()
    app_main.show()
    main_controller = CfGuiControl(view=app_main.ui, options_view=app_options, configuration_file=configfile)
    options_controller = OptionsGuiControl(widget=app_options, view=app_options.ui, configuration_file=configfile)
    sys.exit(app.exec_())


