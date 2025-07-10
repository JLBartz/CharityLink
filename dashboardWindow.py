from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog

class DashboardWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("dashboardWindow.ui", self)
