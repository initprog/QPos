from PyQt6 import QtWidgets
from qpos import app, login
from qpos.ui.main import Ui_MainWindow

class MainApp(Ui_MainWindow):
  active_user = ''

  def __init__(self):
      self.win = QtWidgets.QMainWindow()
      self.setupUi(self.win)
      self.win.setWindowIcon(app.appicon())      
      self.win.show()
      self.check_user()

  def check_user(self):
     if MainApp.active_user == '':
        print('inside check_user')
        self.login = login.Login()
        self.login.showme()
        #login_win.show()