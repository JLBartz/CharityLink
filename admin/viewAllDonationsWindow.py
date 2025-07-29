from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6.uic import loadUi
from utils import apply_window_icon
import sqlite3

class ViewAllDonationsWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("admin/viewAllDonationsWindow.ui", self)
        apply_window_icon(self)

        self.user_id = user_id
        self.loadDonations()
        self.closeButton.clicked.connect(self.close)

    def loadDonations(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()

        # If you want to view all donations (not just from a specific donor), remove the WHERE clause
        c.execute("""
            SELECT d.id, u.name, d.name, d.category, d.description, d.quantity, d.location, d.status, d.created_at
            FROM donation_items d
            JOIN users u ON d.donor_id = u.id
        """)
        
        donations = c.fetchall()
        conn.close()

        self.donationsTable.setRowCount(0)
        self.donationsTable.setColumnCount(9)
        self.donationsTable.setHorizontalHeaderLabels([
            "Donation ID", "Donor Name", "Item Name", "Category", "Description",
            "Quantity", "Location", "Status", "Created At"
        ])

        for row_num, row_data in enumerate(donations):
            self.donationsTable.insertRow(row_num)
            for col, data in enumerate(row_data):
                self.donationsTable.setItem(row_num, col, QTableWidgetItem(str(data)))
