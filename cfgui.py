import configparser
import sys
from timeit import default_timer as timer

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets

import cf
from gui.cfabout import Ui_aboutDialog
from gui.cfguimain import Ui_MainWindow
from gui.cfoptions import Ui_OptionsWindow


class cfMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(cfMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class cfOptionsWindow(QtWidgets.QWidget):
    def __init__(self):
        super(cfOptionsWindow, self).__init__()
        self.ui = Ui_OptionsWindow()
        self.ui.setupUi(self)


class cfAboutWindow(QtWidgets.QDialog):
    def __init__(self):
        super(cfAboutWindow, self).__init__()
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)


class AboutGuiControl:
    """Cs-Fetch about window gui controller class"""
    def __init__(self, widget, view):
        self._view = view
        self._widget = widget
        self._connect_signals()

    def _connect_signals(self):
        self._view.okButton.clicked.connect(self._widget.close)


class OptionsGuiControl:
    """Cs-Fetch options window gui contoller class"""
    def __init__(self, widget, view, configuration_file, session, app):
        self._view = view
        self._widget = widget
        self._session = session
        self._configfile = configuration_file
        self._fields = [self._session.field_labels[f] for f in self._session.field_list]
        self._app = app
        self._load_config()
        self._connect_signals()

    def _connect_signals(self):
        self._view.okButton.clicked.connect(lambda: self._save_config())
        self._view.cancelButton.clicked.connect(lambda: self._cancel())

    def _load_config(self):
        # load options from active session and display them in appropriate widgets
        self._fields = [self._session.field_labels[f] for f in self._session.field_list]
        for b in self._view.scrollAreaWidgetContents.children():
            if isinstance(b, QtWidgets.QCheckBox):
                if b.text() in self._fields:
                    b.setChecked(True)
                else:
                    b.setChecked(False)
        self._view.userField.setText(self._session.username)  # set username from session
        self._view.pwField.setText(self._session.password)  # set password from session
        if self._session.source == 'hamqth':
            self._view.qthButton.setChecked(True)
        if dark_mode:
            self._view.darkButton.setChecked(True)
            self._view.lightButton.setChecked(False)
        else:
            self._view.darkButton.setChecked(False)
            self._view.lightButton.setChecked(True)

    def _save_config(self):
        # save options from GUI to cf.conf, hide view and reinitialize
        new_fields = []
        source = 'hamqth'
        if self._view.qthButton.isChecked():
            source = 'hamqth'
        global dark_mode
        if self._view.darkButton.isChecked():
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            dark_mode = True
        else:
            app.setStyleSheet('')
            dark_mode = False
        for b in self._view.scrollAreaWidgetContents.children():
            if isinstance(b, QtWidgets.QCheckBox):
                if b.isChecked():
                    new_fields.append(b.text())
        new_fields = [k for k, i in self._session.field_labels.items() if i in new_fields]
        self._session.write_config(new_fields, self._view.userField.text(), self._view.pwField.text(), source)
        self._widget.close()
        self._load_config()

    def _cancel(self):
        # hide view and reload config from file when cancel button is pressed
        self._widget.close()
        self._load_config()


class CfGuiControl:
    """Cs-Fetch main window GUI controller class"""
    def __init__(self, view, options_view, about_view, configuration_file, session):
        self._view = view
        self._configfile = configuration_file
        self._options_view = options_view
        self._about_view = about_view
        self._results = {}
        self._labelfont = QtGui.QFont()
        self._labelfont.setBold(True)
        self._connect_signals()
        self._result_data = {'Welcome to Cs-Fetch!': 'Enter a callsign and press "Search"'}
        self._csinput = None
        self._session = session
        self._start = None
        self._end = None
        self._status_widget = None
        self._fill_results_table(self._result_data)
        self._check_session_status()

    def _check_session_status(self):
        if self._session.session_error:
            self._show_error_status(f'{self._session.session_error.__str__()[:78]}')
        else:
            self._show_session_status(self._session.session_id)

    def _connect_signals(self):
        self._view.searchbutton.clicked.connect(self._process_callsign_input)
        self._view.actionExit.triggered.connect(lambda: sys.exit())
        self._view.actionOptions.triggered.connect(lambda: self._options_view.show())
        self._view.actionAbout.triggered.connect(lambda: self._about_view.show())
        self._view.searchinput.returnPressed.connect(self._view.searchbutton.click)

    def _process_callsign_input(self):
        self._view.resultsTable.clear()
        self._view.resultsTable.setColumnCount(0)
        self._view.resultsTable.setRowCount(0)
        self._csinput = self._view.searchinput.text()
        self._result_data = {}
        validation_failed = cf.validate_callsign(self._csinput)
        if not validation_failed:
            # if user's input passes validation, cf.validate_callsign returns False, and we can query the API
            start = timer()  # start timing api fetch
            self._show_progress_status(self._csinput)
            self._results = cf.fetch_callsign_data(self._session.session_id, self._csinput)
            end = timer()  # end timing api fetch
            if self._results.__class__ == str:
                # if the results of cf.fetch_callsign_data() are not a dictionary, the API has produced an error
                self._view.resultsTable.setColumnCount(0)
                self._view.resultsTable.setRowCount(0)
                self._show_error_status(self._results)
                if 'Session does not exist or expired' in self._results:
                    self._session = cf.FetchSession(self._configfile)
                    self._check_session_status()
            else:
                for key in self._session.field_list:
                    if key in self._results.keys() & self._session.field_labels.keys():
                        self._result_data[self._session.field_labels[key]] = self._results[key]
                self._fill_results_table(self._result_data)
                self._view.resultsTable.resizeColumnsToContents()
                self._show_timer_status(end - start)
        else:
            self._show_error_status(validation_failed)
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
        self._view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Session ID: {sessionid}')
        self._view.statusbar.addWidget(self._status_widget)

    def _show_error_status(self, error_text):
        self._view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Error: {error_text}')
        self._view.statusbar.addWidget(self._status_widget)

    def _show_timer_status(self, time):
        self._view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Retrieved callsign info in {time:.2f} seconds')
        self._view.statusbar.addWidget(self._status_widget)

    def _show_progress_status(self, entered_callsign):
        self._view.statusbar.removeWidget(self._status_widget)
        self._status_widget = QtWidgets.QLabel(f'Retrieving information about {entered_callsign}')
        self._view.statusbar.addWidget(self._status_widget)

# TODO: copy results to clipboard button
# TODO: icons for window and task bar

if __name__ == '__main__':
    configfile = 'cf.conf'
    active_session = cf.FetchSession(configfile)
    app = QtWidgets.QApplication([])
    app.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton, True)  # remove ? from title bars
    app_main = cfMainWindow()
    app_options = cfOptionsWindow()
    app_about = cfAboutWindow()
    config = configparser.ConfigParser(inline_comment_prefixes='#')
    config.read(configfile)
    dark_mode = False
    if config.get('Theme', 'darkmode') == 'yes':
        dark_mode = True
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app_main.show()
    main_controller = CfGuiControl(view=app_main.ui, options_view=app_options, about_view=app_about, configuration_file=configfile, session=active_session)
    options_controller = OptionsGuiControl(widget=app_options, view=app_options.ui, configuration_file=configfile, session=active_session, app=app)
    about_controller = AboutGuiControl(widget=app_about, view=app_about.ui)
    sys.exit(app.exec_())


