import sqlite3
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class ViewAllDonationsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("viewAllDonationsWindow.ui", self)
        self.closeButton.clicked.connect(self.close)
        self.setupTable()
        self.loadAllDonations()

    def setupTable(self):
        table = self.donationsTable
        headers = [
            "ID", "Donor Name", "Email", "Item Name", "Category", "Description",
            "Quantity", "Location", "Status", "Created"
        ]
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setEditTriggers(table.EditTrigger.NoEditTriggers)
        table.setSelectionBehavior(table.SelectionBehavior.SelectRows)

    def loadAllDonations(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("""
            SELECT
                d.id,
                u.name,
                u.email,
                d.name,
                d.category,
                d.description,
                d.quantity,
                d.location,
                d.status,
                d.created_at
            FROM donation_items d
            JOIN users u ON d.donor_id = u.id
            ORDER BY d.created_at DESC
        """)
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
