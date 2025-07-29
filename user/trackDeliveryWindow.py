from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6.uic import loadUi
import sqlite3
import sqlite3

class TrackDeliveryWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("user/trackDeliveryWindow.ui", self)
        self.user_id = user_id
        self.loadDeliveries()

    def loadDeliveries(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        cur = conn.cursor()

        # Query deliveries for user as donor (of goods)
        cur.execute("""
            SELECT d.id, d.status, d.completed_time, m.match_type, di.name, gr.name
            FROM deliveries d
            JOIN matches m ON d.match_id = m.id
            LEFT JOIN donation_items di ON m.donation_item_id = di.id
            LEFT JOIN goods_requests gr ON m.goods_request_id = gr.id
            WHERE di.donor_id = ?
            UNION
            SELECT d.id, d.status, d.completed_time, m.match_type, di.name, gr.name
            FROM deliveries d
            JOIN matches m ON d.match_id = m.id
            LEFT JOIN donation_items di ON m.donation_item_id = di.id
            LEFT JOIN goods_requests gr ON m.goods_request_id = gr.id
            WHERE gr.requester_id = ?
        """, (self.user_id, self.user_id))

        deliveries = cur.fetchall()
        conn.close()

        self.deliveryTable.setRowCount(len(deliveries))
        self.deliveryTable.setColumnCount(6)
        self.deliveryTable.setHorizontalHeaderLabels([
            "Delivery ID", "Status", "Completed Time", "Match Type", "Item Donated", "Request"
        ])

        for row, delivery in enumerate(deliveries):
            for col, value in enumerate(delivery):
                item = QTableWidgetItem(str(value) if value is not None else "")
                self.deliveryTable.setItem(row, col, item)
