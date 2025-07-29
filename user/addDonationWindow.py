from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QMessageBox
from utils import apply_window_icon
import sqlite3

class AddDonationWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("user/addDonationWindow.ui", self)
        apply_window_icon(self)

        self.user_id = user_id  # Pass logged-in user's ID
        self.submitButton.clicked.connect(self.submitDonation)

    def submitDonation(self):
        name = self.itemNameLineEdit.text().strip()
        description = self.descriptionLineEdit.text().strip()
        category = self.categoryComboBox.currentText()
        quantity = self.quantitySpinBox.value()
        location = self.locationLineEdit.text().strip()

        # Basic validation
        if not name or not category or quantity <= 0 or not location:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields.")
            return

        try:
            conn = sqlite3.connect("CharityLink-Updated.db")
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO donation_items 
                (donor_id, name, category, description, quantity, location)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.user_id, name, category, description, quantity, location))

            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Donation successfully added.")
            self.accept()  # Close the dialog

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
