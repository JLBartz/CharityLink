from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog
import sys

from loginWindow import LoginWindow

app = QApplication(sys.argv)
log = LoginWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(log)
widget.setWindowTitle("CharityLink")
widget.setFixedHeight(600)
widget.setFixedWidth(1000)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting the program...")