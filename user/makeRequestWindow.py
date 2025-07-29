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
    # Field extraction
        name = self.nameLineEdit.text().strip()
        category = self.categoryComboBox.currentText()
        quantity = self.quantitySpinBox.value()
        location = self.locationLineEdit.text().strip()

    # Input validation
        if not name or not category or quantity < 1 or not location:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

    # Insert the goods request
        conn = sqlite3.connect("CharityLink-Updated.db")
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO goods_requests (requester_id, name, category, quantity, location, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.user_id, name, category, quantity, location, "pending"))

        request_id = cur.lastrowid  # ✅ Get the newly inserted request ID

        # Match with a suitable donation item
        cur.execute("""
            SELECT id FROM donation_items
            WHERE category = ? AND quantity >= ? AND location LIKE ?
            AND status = 'open'
            LIMIT 1
        """, (category, quantity, f"%{location}%"))


        donation_match = cur.fetchone()

        if donation_match:
            donation_item_id = donation_match[0]

            cur.execute("""
                INSERT INTO matches (match_type, donation_item_id, goods_request_id, quantity_matched)
                VALUES (?, ?, ?, ?)
            """, ("item", donation_item_id, request_id, quantity))

            # Update statuses to reflect match
            cur.execute("UPDATE donation_items SET status = 'matched' WHERE id = ?", (donation_item_id,))
            cur.execute("UPDATE goods_requests SET status = 'matched' WHERE id = ?", (request_id,))

        # Commit and close
        conn.commit()
        conn.close()

        # Notify user
        QMessageBox.information(self, "Success", "Your request has been submitted!")
        self.accept()

