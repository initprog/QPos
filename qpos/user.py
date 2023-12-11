from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from qpos.ui import initial, orderMain

class UserAuth(initial.Ui_Form):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.Form.show()
        self.initUI()

    def initUI(self):
        # connect button to function
        self.isPassword.clicked.connect(self.checkPassword)
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Icon.Ok)
        msgBox.exec_()
    def checkPassword(self):
        if self.passwordInput.text() == '1234':
            self.openOrder()
        elif self.passwordInput.text() == '':
            self.showMessageBox('오류','비밀번호를 입력하십시오')
            #warning = QMessageBox()
            #warning.setIcon(QMessageBox.Warning)
            #warning.setText("비밀번호를 입력하십시오")
            #warning.setWindowTitle("오류")
            #warning.exec()
        else:
            self.showMessageBox('오류','비밀번호가 올바르지 않습니다')
            #warning = QMessageBox()
            #warning.setIcon(QMessageBox.Warning)
            #warning.setText("비밀번호가 올바르지 않습니다")
            #warning.setWindowTitle("오류")
            #warning.exec()

    # make new window of SaleStat
    def openOrder(self):
        self.Form = QtWidgets.QMainWindow()
        self.ds = Order()

class Order(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ds = orderMain.OrderMain()