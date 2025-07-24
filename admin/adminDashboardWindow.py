from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
from admin.viewAllUsersWindow import ViewAllUsersWindow
from db import log_audit_action
'''
from auditLogWindow import AuditLogWindow
from viewAllDonationsWindow import ViewAllDonationsWindow
from reverseWindow import ReverseWindow
from viewAllRequestsWindow import ViewAllRequestsWindow
from updateDeliveryWindow import UpdateDeliveryWindow
'''

class AdminDashboardWindow(QDialog):
    def __init__(self, login_window=None, user_id=None):
        super().__init__(login_window)
        loadUi("admin/adminDashboardWindow.ui", self)

        self.login_window = login_window
        self.user_id = user_id

        self.viewUsersButton.clicked.connect(self.openViewUsers)
        self.logoutButton.clicked.connect(self.logout)  # Connect logout button

    def openViewUsers(self):
        dialog = ViewAllUsersWindow(self)
        dialog.exec()

    def logout(self):
        if self.user_id:
            log_audit_action(self.user_id, "Logout")
        self.login_window.show()
        self.close()

'''
        self.viewDonationsButton.clicked.connect(self.openViewDonations)
        self.viewRequestsButton.clicked.connect(self.openViewRequests)
        self.viewAuditLogsButton.clicked.connect(self.openAuditLogs)
        self.reverseButton.clicked.connect(self.openReverse)
        self.updateDeliveryButton.clicked.connect(self.openUpdateDelivery)
        self.logoutButton.clicked.connect(self.logout)

    def openViewRequests(self):
        dialog = ViewAllRequestsWindow(self)
        dialog.exec()

    def openUpdateDelivery(self):
        dialog = UpdateDeliveryWindow(self)
        dialog.exec()

    def logout(self):
        self.accept()

    def openViewDonations(self):
        dialog = ViewAllDonationsWindow(self)
        dialog.exec()

    def openAuditLogs(self):
        dialog = AuditLogWindow(self)
        dialog.exec()

    def openReverse(self):
        dialog = ReverseWindow(self)
        dialog.exec()
'''
    

    
