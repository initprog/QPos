from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from qpos import login, main, user
import os, sys

def run():
    app = QApplication(sys.argv)
    win = main.MainApp()
    win.show()
    
    sys.exit(app.exec())

def appicon():
    """ Get application icon """
    icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), f"asset{os.sep}Q.png"))
    return icon