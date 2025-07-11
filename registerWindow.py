from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox

class RegisterWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("registerWindow.ui", self)

        self.registerButton.clicked.connect(self.handleRegister)

    def handleRegister(self):
        name = self.nameLineEdit.text().strip()
        email = self.emailLineEdit.text().strip()
        password = self.passwordLineEdit.text()
        confirm_password = self.confirmPasswordLineEdit.text()

        if not name or not email or not password or not confirm_password:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Password Error", "Passwords do not match.")
            return

        # Here, you would typically add user to DB or file (mock for now)
        # --- MOCK ONLY ---
        QMessageBox.information(self, "Registration Successful", f"Account registered for {name}!")
        self.accept()
