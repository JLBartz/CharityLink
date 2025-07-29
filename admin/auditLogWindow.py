import sqlite3
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from utils import apply_window_icon

DB_PATH = "CharityLink-Updated.db"

class AuditLogWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("admin/auditLogWindow.ui", self)
        apply_window_icon(self)
        
        self.populate_log_table_from_db()

        self.closeButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

    def populate_log_table_from_db(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            # JOIN users to show email instead of just user_id
            cursor.execute("""
                SELECT audit_logs.created_at, users.email, audit_logs.action, audit_logs.details
                FROM audit_logs
                LEFT JOIN users ON audit_logs.user_id = users.id
                ORDER BY audit_logs.created_at DESC
            """)
            rows = cursor.fetchall()

            self.logTable.setRowCount(len(rows))
            self.logTable.setColumnCount(4)
            self.logTable.setHorizontalHeaderLabels(["Timestamp", "User Email", "Action", "Details"])

            for row_idx, row_data in enumerate(rows):
                for col_idx, value in enumerate(row_data):
                    self.logTable.setItem(row_idx, col_idx, QTableWidgetItem(str(value) if value is not None else ""))

            conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load audit logs:\n{str(e)}")
        
