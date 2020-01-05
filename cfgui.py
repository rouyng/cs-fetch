import configparser
import sys
from timeit import default_timer as timer

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets

import cf
from gui.cfabout import Ui_aboutDialog
from gui.cfguimain import Ui_MainWindow
from gui.cfoptions import Ui_OptionsWindow


class CfMainWindow(QtWidgets.QMainWindow):
    """class to initialize Main window widget from QT-designer generated class"""
    def __init__(self):
        super(CfMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class CfOptionsWindow(QtWidgets.QWidget):
    """class to initialize Options window widget from QT-designer generated class"""
    def __init__(self):
        super(CfOptionsWindow, self).__init__()
        self.ui = Ui_OptionsWindow()
        self.ui.setupUi(self)


class CfAboutWindow(QtWidgets.QDialog):
    """class to initialize About window widget from QT-designer generated class"""
    def __init__(self):
        super(CfAboutWindow, self).__init__()
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)


class CfGuiControl:
    """Cs-Fetch GUI controller class"""
    def __init__(self, main_view, configuration_file):
        self._main_view = main_view
        self._about_widget = CfAboutWindow()
        self._about_view = self._about_widget.ui
        self._options_widget = CfOptionsWindow()
        self._options_view = self._options_widget.ui
        self._configfile = configuration_file
        self._config = configparser.ConfigParser(inline_comment_prefixes='#')
        self._session = cf.FetchSession(self._configfile)
        self._fields = [self._session.field_labels[f] for f in self._session.field_list]
        self._results = {}
        self._label_font = QtGui.QFont()
        self._label_font.setBold(True)
        self._dark_mode = False
        self._config.read(self._configfile)
        if self._config.get('Theme', 'darkmode') == 'yes':
            self._dark_mode = True
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self._csinput = None
        self._status_widget = None
        self._check_session_status()
        # Populate results area with welcome message
        self._result_data = {'Welcome to Cs-Fetch!': 'Enter a callsign and press "Search"'}
        self._fill_results_table(self._result_data)
        # load configuration into options widget
        self._load_config()
        # connect GUI signals
        self._connect_signals()

    def _connect_signals(self):
        """Connect GUI button/menu signals"""
        # signals related to main widget
        self._main_view.searchbutton.clicked.connect(self._process_callsign_input)
        self._main_view.actionExit.triggered.connect(lambda: sys.exit())
        self._main_view.actionOptions.triggered.connect(self._options_widget.show)
        self._main_view.actionAbout.triggered.connect(self._about_widget.show)
        self._main_view.searchinput.returnPressed.connect(self._main_view.searchbutton.click)
        # signals related to about widget
        self._about_view.okButton.clicked.connect(self._about_widget.close)
        # signals related to options widget
        self._options_view.okButton.clicked.connect(lambda: self._save_config())
        self._options_view.cancelButton.clicked.connect(lambda: self._options_cancel())

    def _check_session_status(self):
        """Checks if the current session has an error message and displays the appropriate status bar message"""
        if self._session.session_error:
            self._show_error_status(f'{self._session.session_error.__str__()[:78]}')
        else:
            self._show_session_status(self._session.session_id)

    def _process_callsign_input(self):
        """Read user's input for callsign search, run validation, fetch results and display results or errors"""
        self._main_view.resultsTable.clear()
        self._main_view.resultsTable.setColumnCount(0)
        self._main_view.resultsTable.setRowCount(0)
        self._csinput = self._main_view.searchinput.text()
        self._result_data = {}
        validation_failed = cf.validate_callsign(self._csinput)
        if not validation_failed:
            # if user's input passes validation, cf.validate_callsign returns False, and we can query the API
            start = timer()  # start timing api fetch
            self._show_progress_status(self._csinput)
            self._results = cf.fetch_callsign_data(self._session.session_id, self._csinput, self._session.source)
            end = timer()  # end timing api fetch
            if self._results.__class__ == str:
                # if the results of cf.fetch_callsign_data() are not a dictionary, the API has produced an error
                self._main_view.resultsTable.setColumnCount(0)
                self._main_view.resultsTable.setRowCount(0)
                self._show_error_status(self._results)
                if 'Session does not exist or expired' in self._results:
                    self._session = cf.FetchSession(self._configfile)
                    self._check_session_status()
            else:
                for key in self._session.field_list:
                    if key in self._results.keys() & self._session.field_labels.keys():
                        self._result_data[self._session.field_labels[key]] = self._results[key]
                self._fill_results_table(self._result_data)
                self._main_view.resultsTable.resizeColumnsToContents()
                self._show_timer_status(end - start)
        else:
            self._show_error_status(validation_failed)
            self._main_view.searchinput.clear()

    def _fill_results_table(self, data: dict):
        """Populate results table with callsign information"""
        self._main_view.resultsTable.setColumnCount(2)
        self._main_view.resultsTable.setRowCount(len(data))
        for i, k in enumerate(data):
            label_item = QtWidgets.QTableWidgetItem(f'{k}')
            label_item.setFont(self._label_font)
            self._main_view.resultsTable.setItem(i, 0, label_item)
            if k == 'Callsign':
                self._main_view.resultsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(data[k].upper()))
            else:
                self._main_view.resultsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(data[k]))

    def _show_session_status(self, sessionid):
        """Clear current status bar widget and display session status message"""
        self._main_view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Session ID: {sessionid}')
        self._main_view.statusbar.addWidget(self._status_widget)

    def _show_error_status(self, error_text):
        """Clear current status bar widget and display error message"""
        self._main_view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Error: {error_text}')
        self._main_view.statusbar.addWidget(self._status_widget)

    def _show_timer_status(self, time):
        """Clear current status bar widget and display message with time to retrieve callsign results"""
        self._main_view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Retrieved callsign info in {time:.2f} seconds')
        self._main_view.statusbar.addWidget(self._status_widget)

    def _show_progress_status(self, entered_callsign):
        """Clear current status bar widget and display message showing callsign info retrieval is in progress"""
        self._main_view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Retrieving information about {entered_callsign}')
        self._main_view.statusbar.addWidget(self._status_widget)

    def _load_config(self):
        """Load options from active session and display them in appropriate widgets within the Options window"""
        self._fields = [self._session.field_labels[f] for f in self._session.field_list]
        for b in self._options_view.scrollAreaWidgetContents.children():
            if isinstance(b, QtWidgets.QCheckBox):
                if b.text() in self._fields:
                    b.setChecked(True)
                else:
                    b.setChecked(False)
        self._options_view.userField.setText(self._session.username)  # set username from session
        self._options_view.pwField.setText(self._session.password)  # set password from session
        if self._session.source == 'hamqth':
            self._options_view.qthButton.setChecked(True)
        if self._dark_mode:
            self._options_view.darkButton.setChecked(True)
            self._options_view.lightButton.setChecked(False)
        else:
            self._options_view.darkButton.setChecked(False)
            self._options_view.lightButton.setChecked(True)

    def _save_config(self):
        """Save options from Options Window to cf.conf, then hide window and reinitialize session"""
        new_fields = []
        source = 'hamqth'
        if self._options_view.qthButton.isChecked():
            source = 'hamqth'
        if self._options_view.darkButton.isChecked():
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self._dark_mode = True
        else:
            app.setStyleSheet('')
            self._dark_mode = False
        for b in self._options_view.scrollAreaWidgetContents.children():
            if isinstance(b, QtWidgets.QCheckBox):
                if b.isChecked():
                    new_fields.append(b.text())
        new_fields = [k for k, i in self._session.field_labels.items() if i in new_fields]
        self._session.write_config(new_fields,
                                   self._options_view.userField.text(),
                                   self._options_view.pwField.text(),
                                   source,
                                   self._dark_mode)
        self._options_widget.close()
        self._load_config()
        self._check_session_status()

    def _options_cancel(self):
        """Hide view and reload config from file when cancel button is pressed"""
        self._options_widget.close()
        self._load_config()

# TODO: copy results to clipboard button
# TODO: icons for window and task bar


if __name__ == '__main__':
    configfile = 'cf.conf'
    app = QtWidgets.QApplication([])
    app.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton, True)  # remove ? from title bars
    app_main = CfMainWindow()
    controller = CfGuiControl(main_view=app_main.ui, configuration_file=configfile)
    app_main.show()
    sys.exit(app.exec_())


