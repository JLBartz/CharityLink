from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
from admin.viewAllUsersWindow import ViewAllUsersWindow
from admin.auditLogWindow import AuditLogWindow
from admin.viewAllRequestsWindow import ViewAllRequestsWindow
from admin.updateDeliveryWindow import UpdateDeliveryWindow
from admin.viewAllDonationsWindow import ViewAllDonationsWindow
from admin.reverseWindow import ReverseWindow
from utils import apply_window_icon
from db import log_audit_action


class AdminDashboardWindow(QDialog):
    def __init__(self, login_window=None, user_id=None):
        super().__init__(login_window)
        loadUi("admin/adminDashboardWindow.ui", self)
        apply_window_icon(self)

        self.login_window = login_window
        self.user_id = user_id

        self.viewUsersButton.clicked.connect(self.openViewUsers)
        self.viewAuditLogsButton.clicked.connect(self.openAuditLogs)
        self.viewRequestsButton.clicked.connect(self.openViewRequests)
        self.viewAuditLogsButton.clicked.connect(self.openAuditLogs)
        self.updateDeliveryButton.clicked.connect(self.openUpdateDelivery)
        self.viewDonationsButton.clicked.connect(self.openViewDonations)
        self.reverseButton.clicked.connect(self.openReverse)
        
        self.logoutButton.clicked.connect(self.logout)  


    def openViewUsers(self):
        dialog = ViewAllUsersWindow(self)
        dialog.exec()

    def openAuditLogs(self):
        dialog = AuditLogWindow(self)
        dialog.exec()

    def logout(self):
        if self.user_id:
            log_audit_action(self.user_id, "Logout")
        self.login_window.show()
        self.close()

    def openViewRequests(self):
        dialog = ViewAllRequestsWindow(self)
        dialog.exec()

    def openUpdateDelivery(self):
        dialog = UpdateDeliveryWindow(self)
        dialog.exec()

    def openViewDonations(self):
        dialog = ViewAllDonationsWindow(self.user_id, self)
        dialog.exec()

    def openReverse(self):
        dialog = ReverseWindow(self)
        dialog.exec()

   

    

    
