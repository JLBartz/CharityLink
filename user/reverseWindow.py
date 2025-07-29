from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
import sqlite3

class ReverseWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("reverseWindow.ui", self)
        self.load_matches()
        self.reverseButton.clicked.connect(self.reverse_selected)

    def load_matches(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("""
            SELECT id, match_type, status, matched_at
            FROM matches
            WHERE status != 'reversed'
        """)
        matches = c.fetchall()
        conn.close()

        self.matchesTable.setRowCount(0)
        for row_num, row_data in enumerate(matches):
            self.matchesTable.insertRow(row_num)
            for col, data in enumerate(row_data):
                self.matchesTable.setItem(row_num, col, QTableWidgetItem(str(data)))

    def reverse_selected(self):
        selected = self.matchesTable.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "No Selection", "Please select a match to reverse.")
            return
        match_id = int(self.matchesTable.item(selected, 0).text())

        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("UPDATE matches SET status = 'reversed' WHERE id = ?", (match_id,))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Reversed", "Selected match has been reversed.")
        self.load_matches()

