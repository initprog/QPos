from PyQt6.QtWidgets import QWidget, QMessageBox, QMainWindow, QDialogButtonBox
from PyQt6 import QtGui
from qpos import app
from qpos.ui import initial, orderMain

class UserAuth(initial.Ui_Form):
    def __init__(self):
        self.win = QWidget()
        self.setupUi(self.win)
        self.win.setWindowIcon(app.appicon())
        self.win.show()
        self.initUI()

    def initUI(self):
        # connect button to function
        self.isPassword.clicked.connect(self.checkPassword)
    def showMessageBox(self,title,message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()
        
    def checkPassword(self):
        if self.passwordInput.text() == '1234':
            self.openOrder()
        elif self.passwordInput.text() == '':
            self.showMessageBox('Error', 'Please enter a password')
        else:
            self.showMessageBox('Error', 'Incorrect password.')

    # make new window of SaleStat
    def openOrder(self):
        self.win = QMainWindow()
        self.ds = Order()

class Order(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ds = orderMain.OrderMain()