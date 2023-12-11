from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from qpos import user
import os, sys

def run():
    app = QApplication(sys.argv)
    e = user.UserAuth()
    sys.exit(app.exec())

def appicon():
    """ Get application icon """
    icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), f"asset{os.sep}Q.png"))
    return icon