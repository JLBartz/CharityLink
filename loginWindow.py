from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox
from dashboardWindow import DashboardWindow

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("loginInputDialog.ui", self)

        self.submitLoginButton.clicked.connect(self.checkLogin)

        self.mock_user_email = "donor@example.com"
        self.mock_user_password = "donor123"
        self.mock_user_name = "Donor"

        self.login_success = False  # <-- flag to indicate login result

    def checkLogin(self):
        email = self.emailLineEdit.text().strip()  
        password = self.passwordLineEdit.text().strip()

        if email == self.mock_user_email and password == self.mock_user_password:
            QMessageBox.information(self, "Login Successful", f"Welcome, {self.mock_user_name}!")

            self.login_success = True  
            self.accept()              
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid email or password.")

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("loginWindow.ui", self)

        self.loginPushButton.clicked.connect(self.openLoginDialog)

    def openLoginDialog(self):
        dialog = LoginDialog(self)
        result = dialog.exec()

        if dialog.login_success:
            self.dashboard = DashboardWindow()
            self.dashboard.show()
            self.close()
