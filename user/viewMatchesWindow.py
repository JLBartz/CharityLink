import sqlite3
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class ViewMatchesWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("viewMatchesWindow.ui", self)
        self.user_id = user_id
        self.closeButton.clicked.connect(self.close)
        self.setupTable()
        self.loadMatches()

    def setupTable(self):
        headers = ["Match ID", "Type", "Item/Request", "Status", "Matched At"]
        self.matchesTable.setColumnCount(len(headers))
        self.matchesTable.setHorizontalHeaderLabels(headers)
        self.matchesTable.setEditTriggers(self.matchesTable.EditTrigger.NoEditTriggers)

    def loadMatches(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        # Get matches as donor
        c.execute("""
            SELECT m.id, m.match_type, di.name, m.status, m.matched_at
            FROM matches m
            JOIN donation_items di ON m.donation_item_id = di.id
            WHERE di.donor_id = ?
            UNION ALL
            SELECT m.id, m.match_type, gr.name, m.status, m.matched_at
            FROM matches m
            JOIN goods_requests gr ON m.goods_request_id = gr.id
            WHERE gr.requester_id = ?
            ORDER BY m.matched_at DESC
        """, (self.user_id, self.user_id))
        results = c.fetchall()
        self.matchesTable.setRowCount(len(results))
        for row_idx, row in enumerate(results):
            for col_idx, val in enumerate(row):
                self.matchesTable.setItem(row_idx, col_idx, self.makeTableItem(str(val)))
        conn.close()

    @staticmethod
    def makeTableItem(text):
        from PyQt6.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)
