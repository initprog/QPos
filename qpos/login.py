import os
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from qpos.view.login import Ui_login
from qpos import app, utils

class Login(Ui_login, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowIcon(app.appicon())
        self.msgLabel.setText('')
        self.userEdit.setFocus()
        logo = os.path.join(os.path.dirname(__file__), f"asset{os.sep}Q.png")
        self.logo.setPixmap(QPixmap(logo))
        self.logo.setScaledContents(True)
        self.setFixedSize(self.size())  # no resize
        self.signinButton.clicked.connect(self.signinButton_clicked)
        self.show()

    def closeEvent(self, event):
        if self.parent.auth_user != None:
            print(f'ok to close {self.parent.auth_user}')
            self.parent.ui.auth_user.setToolTip(self.parent.auth_user)
            event.accept()
        else:
            # cannot close login form without passing authentication
            event.ignore()

    def signinButton_clicked(self):
        self.msgLabel.setText('')
        if self.userEdit.text() == '':
            self.msgLabel.setText('Please enter the user id')
            self.userEdit.setFocus()
            return
        elif self.pwdEdit.text() == '':
            self.msgLabel.setText('Please enter the password')
            self.pwdEdit.setFocus()
            return
        
        # check database
        valid = utils.authenticate(self.userEdit.text(), self.pwdEdit.text())
        if not valid:
            self.msgLabel.setText("User Id and/or password do not match.")
            self.userEdit.setFocus()
            return
        self.parent.auth_user = self.userEdit.text()
        self.close()