from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from utils import apply_window_icon
import sqlite3

class UpdateDeliveryWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("admin/updateDeliveryWindow.ui", self)
        apply_window_icon(self)
        
        self.load_deliveries()
        self.updateStatusButton.clicked.connect(self.update_selected)

    def load_deliveries(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("""
            SELECT d.id, d.status, d.completed_time, m.match_type
            FROM deliveries d
            JOIN matches m ON d.match_id = m.id
        """)
        deliveries = c.fetchall()
        conn.close()

        self.deliveriesTable.setRowCount(0)
        for row_num, row_data in enumerate(deliveries):
            self.deliveriesTable.insertRow(row_num)
            for col, data in enumerate(row_data):
                self.deliveriesTable.setItem(row_num, col, QTableWidgetItem(str(data)))

    def update_selected(self):
        selected = self.deliveriesTable.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "No Selection", "Please select a delivery.")
            return
        delivery_id = int(self.deliveriesTable.item(selected, 0).text())

        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("UPDATE deliveries SET status = 'completed', completed_time = datetime('now') WHERE id = ?", (delivery_id,))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Status Updated", "Selected delivery marked as completed.")
        self.load_deliveries()

