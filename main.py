from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget
import sys

class loginScreen(QDialog):
    def __init__(self):
        super(loginScreen, self).__init__()
        loadUi("loginWindow.ui", self)

app = QApplication(sys.argv)
welcome = loginScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedHeight(1200)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting the program")
