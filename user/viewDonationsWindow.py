import sqlite3
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class ViewDonationsWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("user/viewDonationsWindow.ui", self)
        self.user_id = user_id
        self.closeButton.clicked.connect(self.close)
        self.setupTable()
        self.loadDonations()

    def setupTable(self):
        table = self.donationsTable
        headers = ["ID", "Item Name", "Category", "Description", "Quantity", "Location", "Status", "Created"]
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setEditTriggers(table.EditTrigger.NoEditTriggers)
        table.setSelectionBehavior(table.SelectionBehavior.SelectRows)

    def loadDonations(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("""
            SELECT id, name, category, description, quantity, location, status, created_at
            FROM donation_items
            WHERE donor_id = ?
            ORDER BY created_at DESC
        """, (self.user_id,))
        results = c.fetchall()
        self.donationsTable.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, value in enumerate(row_data):
                self.donationsTable.setItem(row_idx, col_idx, self.makeTableItem(str(value)))
        conn.close()

    @staticmethod
    def makeTableItem(text):
        from PyQt6.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)
