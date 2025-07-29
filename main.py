from PyQt6.QtWidgets import QApplication
import sys
from user.loginWindow import LoginWindow
from utils import apply_window_icon

app = QApplication(sys.argv)

window = LoginWindow()
window.setWindowTitle("CharityLink")
window.setFixedSize(1000, 600)
apply_window_icon(window)
window.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting the program...")
