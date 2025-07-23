from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox
from user.dashboardWindow import DashboardWindow
from admin.adminDashboardWindow import AdminDashboardWindow
from user.registerWindow import RegisterWindow
from db import validate_login

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("user/loginInputDialog.ui", self)

        self.submitLoginButton.clicked.connect(self.checkLogin)

        # Mock donor account
        self.mock_user_email = "donor@example.com"
        self.mock_user_password = "donor123"
        self.mock_user_name = "Donor"
        self.mock_user_id = 1

        # Mock admin account
        self.admin_email = "charitylink@example.com"
        self.admin_password = "charitylink123"
        self.admin_name = "Admin"
        self.admin_id = 999  # Any unique number

        self.login_success = False
        self.is_admin = False
        self.logged_in_user_id = None

    def checkLogin(self):
        email = self.emailLineEdit.text().strip()
        password = self.passwordLineEdit.text().strip()

    #Mock Donor Login
        if email == self.mock_user_email and password == self.mock_user_password:
            QMessageBox.information(self, "Login Successful", f"Welcome, {self.mock_user_name}!")
            self.login_success = True
            self.is_admin = False
            self.logged_in_user_id = self.mock_user_id
            self.accept()
            return

    #Mock Admin Login
        if email == self.admin_email and password == self.admin_password:
            QMessageBox.information(self, "Login Successful", "Welcome, Admin!")
            self.login_success = True
            self.is_admin = True
            self.logged_in_user_id = self.admin_id
            self.accept()
            return

    #Database Login
        user = validate_login(email, password)
        if user:
            QMessageBox.information(self, "Login Successful", f"Welcome, {user['name']}!")
            self.login_success = True
            self.is_admin = (user["role"].lower() == "admin")
            self.logged_in_user_id = user["id"]
            self.accept()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid email or password.")
            

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("user/loginWindow.ui", self)

        self.loginPushButton.clicked.connect(self.openLoginDialog)
        self.registerPushButton.clicked.connect(self.openRegisterDialog)

    def openLoginDialog(self):
        dialog = LoginDialog(self)
        result = dialog.exec()

        if dialog.login_success:
            user_id = dialog.logged_in_user_id
            if dialog.is_admin:
                self.dashboard = AdminDashboardWindow()
                self.dashboard.show()
            else:
                self.dashboard = DashboardWindow(user_id)
                self.dashboard.show()
            self.close()

    def openRegisterDialog(self):
        dialog = RegisterWindow(self)
        dialog.exec()

