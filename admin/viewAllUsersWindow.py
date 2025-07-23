from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6.uic import loadUi
import sqlite3

class ViewAllUsersWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("admin/viewAllUsersWindow.ui", self)

        self.load_users()
        self.closeButton.clicked.connect(self.close)

    def load_users(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()
        c.execute("SELECT id, name, email, role FROM users")
        users = c.fetchall()
        conn.close()

        self.usersTable.setRowCount(0)
        for row_num, row_data in enumerate(users):
            self.usersTable.insertRow(row_num)
            for col, data in enumerate(row_data):
                self.usersTable.setItem(row_num, col, QTableWidgetItem(str(data)))

