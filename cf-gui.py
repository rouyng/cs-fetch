import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QGridLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle('CSFetch')
window.setGeometry(200, 200, 400, 200)
layout = QGridLayout()
welcomeMsg = QLabel('<h1>Welcome to CSFetch, a simple callsign info fetcher!</h1>', parent=window)
layout.addWidget(welcomeMsg, 0, 0, 1, 2)
layout.addWidget(QLineEdit('Callsign'), 1, 0)
layout.addWidget(QPushButton('Search'), 1, 1)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())