from PyQt6.QtWidgets import QApplication
import sys
from user.loginWindow import LoginWindow

app = QApplication(sys.argv)

window = LoginWindow()
window.setWindowTitle("CharityLink")
window.setFixedSize(1000, 600)
window.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting the program...")
