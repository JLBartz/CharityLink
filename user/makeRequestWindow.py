from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.uic import loadUi
import sqlite3

class MakeRequestWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("user/makeRequestWindow.ui", self)
        self.user_id = user_id

        self.submitButton.clicked.connect(self.handleSubmit)
        # No reference to closeButton!

    def handleSubmit(self):
        name = self.nameLineEdit.text().strip()
        category = self.categoryComboBox.currentText()
        quantity = self.quantitySpinBox.value()
        location = self.locationLineEdit.text().strip()

        if not name or not category or quantity < 1 or not location:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

        conn = sqlite3.connect("CharityLink-Updated.db")
        cur = conn.cursor()

        # Insert goods request
        cur.execute("""
            INSERT INTO goods_requests (requester_id, name, category, quantity, location, status)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (self.user_id, name, category, quantity, location, "pending"))
        request_id = cur.lastrowid

        # Find match
        cur.execute("""
            SELECT id FROM donation_items
            WHERE category = ? AND quantity >= ? AND location LIKE ?
            AND status = 'open'
            LIMIT 1
        """, (category, quantity, f"%{location}%"))

        donation_match = cur.fetchone()

        if donation_match:
            donation_item_id = donation_match[0]

            # Create match
            cur.execute("""
                INSERT INTO matches (match_type, donation_item_id, goods_request_id, quantity_matched)
                VALUES (?, ?, ?, ?)
            """, ("item", donation_item_id, request_id, quantity))
            match_id = cur.lastrowid

            #Create delivery record
            cur.execute("INSERT INTO deliveries (match_id, status) VALUES (?, ?)", (match_id, "pending"))

            # Update statuses
            cur.execute("UPDATE donation_items SET status = 'matched' WHERE id = ?", (donation_item_id,))
            cur.execute("UPDATE goods_requests SET status = 'matched' WHERE id = ?", (request_id,))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success", "Your request has been submitted!")
        self.accept()


