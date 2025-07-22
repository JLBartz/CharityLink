import sqlite3
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class ViewRequestsWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("viewRequestsWindow.ui", self)
        self.user_id = user_id
        self.closeButton.clicked.connect(self.close)
        self.setupTable()
        self.loadRequests()

    def setupTable(self):
        headers = ["ID", "Name", "Category", "Quantity", "Reason", "Location", "Status", "Created"]
        self.requestsTable.setColumnCount(len(headers))
        self.requestsTable.setHorizontalHeaderLabels(headers)
        self.requestsTable.setEditTriggers(self.requestsTable.EditTrigger.NoEditTriggers)

    def loadRequests(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("""
            SELECT id, name, category, quantity, reason, location, status, created_at
            FROM goods_requests
            WHERE requester_id = ?
            ORDER BY created_at DESC
        """, (self.user_id,))
        results = c.fetchall()
        self.requestsTable.setRowCount(len(results))
        for row_idx, row in enumerate(results):
            for col_idx, val in enumerate(row):
                self.requestsTable.setItem(row_idx, col_idx, self.makeTableItem(str(val)))
        conn.close()

    @staticmethod
    def makeTableItem(text):
        from PyQt6.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)
