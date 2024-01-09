import platform, ctypes
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from qpos import main
import os, sys

QPOS_APPID = 'nagwos.commerce.pos'

def run():
    app = QApplication(sys.argv)
    with open(os.path.join(os.path.dirname(__file__), f"asset{os.sep}qpos.qss")) as qss:
        css = qss.read()
    #app.setStyleSheet(css)

    # Show app's icon on Windows 11 taskbar
    if platform.system() == 'Windows' and platform.release() == '11':
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(QPOS_APPID)

    win = main.MainApp()
    win.show()
    
    sys.exit(app.exec())

def appicon():
    """ Get application icon """
    icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), f"asset{os.sep}Q.png"))
    return icon