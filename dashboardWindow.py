from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog
from addDonationWindow import AddDonationWindow

class DashboardWindow(QDialog):
    def __init__(self, user_id=None):
        super().__init__()
        loadUi("dashboardWindow.ui", self)
        self.user_id = user_id  # 🟢 Save user_id from LoginWindow

        self.addDonationButton.clicked.connect(self.openAddDonation)

    def openAddDonation(self):
        dialog = AddDonationWindow(self.user_id, self)
        dialog.exec()
