from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.uic import loadUi
import sqlite3

class MakeRequestWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("makeRequestWindow.ui", self)
        self.user_id = user_id

        self.submitButton.clicked.connect(self.handleSubmit)
        # No reference to closeButton!

    def handleSubmit(self):
        # Example field fetches (update to match your .ui field names!)
        name = self.nameLineEdit.text().strip()
        category = self.categoryComboBox.currentText()
        quantity = self.quantitySpinBox.value()
        location = self.locationLineEdit.text().strip()
        # Add more fields as needed

        # Input validation
        if not name or not category or quantity < 1 or not location:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

        # Insert into the DB (goods_requests table)
        conn = sqlite3.connect("CharityLink-Updated.db")
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO goods_requests (requester_id, name, category, quantity, location, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.user_id, name, category, quantity, location, "pending"))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success", "Your request has been submitted!")
        self.accept()
