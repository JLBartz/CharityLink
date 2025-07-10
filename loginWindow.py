from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("loginInputDialog.ui", self)

        self.submitLoginButton.clicked.connect(self.checkLogin)

        self.mock_users = {
            "donor@example.com": {"password": "donor123", "name": "Donor Dan"},
            "recipient@example.com": {"password": "recipient123", "name": "Recip Rica"}
        }

    def checkLogin(self):
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()

        user = self.mock_users.get(email)

        if user and user["password"] == password:
            QMessageBox.information(self, "Login Successful", f"Welcome, {user['name']}!")
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
        dialog.exec()
