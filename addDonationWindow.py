from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox
import sqlite3

class AddDonationWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("addDonationWindow.ui", self)
        self.user_id = user_id  # 🟢 Save user_id

        self.submitButton.clicked.connect(self.submitDonation)

    def submitDonation(self):
        name = self.itemNameLineEdit.text().strip()
        description = self.descriptionLineEdit.text().strip()
        category = self.categoryComboBox.currentText()
        quantity = self.quantitySpinBox.value()
        location = self.locationLineEdit.text().strip()

        if not name or not description or not location:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        try:
            conn = sqlite3.connect("CharityLink-Updated.db")
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO donations (name, description, category, quantity, location, user_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, description, category, quantity, location, self.user_id))

            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Donation successfully added!")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
