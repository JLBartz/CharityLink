from PyQt6.QtGui import QIcon

def apply_window_icon(window, icon_path="images/charity.png"):
    window.setWindowIcon(QIcon(icon_path))
