from PyQt6.QtWidgets import QApplication
from qpos import user
import sys

def run():
    app = QApplication(sys.argv)
    e = user.UserAuth()
    sys.exit(app.exec())