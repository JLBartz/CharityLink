from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox
from user.dashboardWindow import DashboardWindow
from admin.adminDashboardWindow import AdminDashboardWindow
from user.registerWindow import RegisterWindow
from utils import apply_window_icon
from db import validate_login, log_audit_action

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("user/loginInputDialog.ui", self)
        apply_window_icon(self)

        self.submitLoginButton.clicked.connect(self.checkLogin)

        # Default values to prevent crash when user closes dialog
        self.login_success = False
        self.is_admin = False
        self.logged_in_user_id = None

    def checkLogin(self):
        email = self.emailLineEdit.text().strip()
        password = self.passwordLineEdit.text().strip()

        user = validate_login(email, password)
        if user:
            QMessageBox.information(self, "Login Successful", f"Welcome, {user['name']}!")
            self.login_success = True
            self.is_admin = (user["role"].lower() == "admin")
            self.logged_in_user_id = user["id"]

            log_audit_action(user["id"], "Login")  # Log the login event

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
                self.dashboard = AdminDashboardWindow(login_window=self)
            else:
                self.dashboard = DashboardWindow(user_id=user_id, login_window=self)
            self.dashboard.show()
            self.hide()


    def openRegisterDialog(self):
        dialog = RegisterWindow(self)
        dialog.exec()

