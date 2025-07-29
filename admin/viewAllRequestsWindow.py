from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6.uic import loadUi
from utils import apply_window_icon
import sqlite3

class ViewAllRequestsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("admin/viewAllRequestsWindow.ui", self)
        apply_window_icon(self)
        
        self.load_requests()
        self.closeButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

    def load_requests(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("""
            SELECT r.id, u.name, r.name, r.category, r.quantity, r.location, r.status, r.created_at
            FROM goods_requests r
            JOIN users u ON r.requester_id = u.id
        """)

        requests = c.fetchall()
        conn.close()

        self.requestsTable.setRowCount(0)
        self.requestsTable.setColumnCount(8)
        self.requestsTable.setHorizontalHeaderLabels([
        "Request ID", "Requester Name", "Item Name", "Category", "Quantity", "Location", "Status", "Created At"
])


        for row_num, row_data in enumerate(requests):
            self.requestsTable.insertRow(row_num)
            for col, data in enumerate(row_data):
                self.requestsTable.setItem(row_num, col, QTableWidgetItem(str(data)))


