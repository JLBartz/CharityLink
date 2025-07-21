from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class AdminDashboardWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("adminDashboardWindow.ui", self)

        # Connect buttons to stubs (fill in later)
        self.viewUsersButton.clicked.connect(self.view_users)
        self.viewDonationsButton.clicked.connect(self.view_donations)
        self.viewRequestsButton.clicked.connect(self.view_requests)
        self.viewAuditLogsButton.clicked.connect(self.view_audit_logs)
        self.logoutButton.clicked.connect(self.accept)

    def view_users(self):
        # TODO: Implement user viewing logic
        pass

    def view_donations(self):
        # TODO: Implement donation viewing logic
        pass

    def view_requests(self):
        # TODO: Implement request viewing logic
        pass

    def view_audit_logs(self):
        # TODO: Implement audit log viewing logic
        pass
