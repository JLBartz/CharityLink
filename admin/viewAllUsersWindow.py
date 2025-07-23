from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
import sqlite3
import os

class ViewAllUsersWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("admin/viewAllUsersWindow.ui", self)

        print("Opening DB from:", os.path.abspath("CharityLink-Updated.db"))

        self.load_users()
        self.closeButton.clicked.connect(self.close)

    def load_users(self):
        try:
            conn = sqlite3.connect("CharityLink-Updated.db")
            c = conn.cursor()
            c.execute("SELECT id, name, email, role FROM users")
            users = c.fetchall()
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load users:\n{e}")
            return
        
        self.usersTable.setRowCount(0)
        self.usersTable.setColumnCount(4)
        self.usersTable.setHorizontalHeaderLabels(["ID", "Name", "Email", "Role"])

        self.usersTable.setRowCount(0)
        for row_num, row_data in enumerate(users):
            self.usersTable.insertRow(row_num)
            for col, data in enumerate(row_data):
                self.usersTable.setItem(row_num, col, QTableWidgetItem(str(data)))

            from PyQt6.QtWidgets import QHeaderView
            header = self.usersTable.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


