import os
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from qpos.ui.login import Ui_login
from qpos import app, utils
from qpos.main import userId

class Login(Ui_login, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(app.appicon())
        self.msgLabel.setText('')
        self.userEdit.setFocus()
        logo = os.path.join(os.path.dirname(__file__), f"asset{os.sep}Q.png")
        self.logo.setPixmap(QPixmap(logo))
        self.logo.setScaledContents(True)
        self.signinButton.clicked.connect(self.signinButton_clicked)
        self.show()

    def closeEvent(self, event):
        global userId
        if userId:
            print(f'ok to close {userId}')
            event.accept()

    def signinButton_clicked(self):
        global userId
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
        userId = self.userEdit.text()
        self.close()