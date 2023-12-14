import os
from datetime import datetime
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from qpos.ui.login import Ui_login
from qpos import app

class Login(Ui_login):
    def __init__(self):
        self.win = QWidget()
        self.setupUi(self.win)
        self.win.setWindowIcon(app.appicon())
        self.msgLabel.setText('')
        self.userEdit.setFocus()
        logo = os.path.join(os.path.dirname(__file__), f"asset{os.sep}Q.png")
        self.logo.setPixmap(QPixmap(logo))
        self.logo.setScaledContents(True)
        self.win.show()
        self.signinButton.clicked.connect(self.signinButton_clicked)

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
        self.msgLabel.setText("Your password might contain characters from a-z 0-9 and special characters.")
        print(f'clicked {datetime.now()}')

