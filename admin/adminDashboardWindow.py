from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

from auditLogWindow import AuditLogWindow
from viewAllUsersWindow import ViewAllUsersWindow
from viewAllDonationsWindow import ViewAllDonationsWindow
from viewAllRequestsWindow import ViewAllRequestsWindow
from reverseWindow import ReverseWindow
from updateDeliveryWindow import UpdateDeliveryWindow

class AdminDashboardWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("adminDashboardWindow.ui", self)

        self.viewUsersButton.clicked.connect(self.openViewUsers)
        self.viewDonationsButton.clicked.connect(self.openViewDonations)
        self.viewRequestsButton.clicked.connect(self.openViewRequests)
        self.viewAuditLogsButton.clicked.connect(self.openAuditLogs)
        self.reverseButton.clicked.connect(self.openReverse)
        self.updateDeliveryButton.clicked.connect(self.openUpdateDelivery)
        self.logoutButton.clicked.connect(self.logout)

    def openViewUsers(self):
        dialog = ViewAllUsersWindow(self)
        dialog.exec()

    def openViewDonations(self):
        dialog = ViewAllDonationsWindow(self)
        dialog.exec()

    def openViewRequests(self):
        dialog = ViewAllRequestsWindow(self)
        dialog.exec()

    def openAuditLogs(self):
        dialog = AuditLogWindow(self)
        dialog.exec()

    def openReverse(self):
        dialog = ReverseWindow(self)
        dialog.exec()

    def openUpdateDelivery(self):
        dialog = UpdateDeliveryWindow(self)
        dialog.exec()

    def logout(self):
        self.accept()
