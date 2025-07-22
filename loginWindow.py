from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox
from dashboardWindow import DashboardWindow
from adminDashboardWindow import AdminDashboardWindow
from registerWindow import RegisterWindow
import db 

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("loginInputDialog.ui", self)
        self.submitLoginButton.clicked.connect(self.checkLogin)
        self.login_success = False
        self.is_admin = False
        self.logged_in_user_id = None
        self.user_name = None

    def checkLogin(self):
        email = self.emailLineEdit.text().strip()
        password = self.passwordLineEdit.text().strip()

        user = db.validate_login(email, password)
        if user:
            self.login_success = True
            self.logged_in_user_id = user["id"]
            self.user_name = user["name"]
            if user["role"].lower() == "admin":
                self.is_admin = True
                QMessageBox.information(self, "Login Successful", "Welcome, Admin!")
            else:
                self.is_admin = False
                QMessageBox.information(self, "Login Successful", f"Welcome, {self.user_name}!")
            self.accept()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid email or password.")

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("loginWindow.ui", self)
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
