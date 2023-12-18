from PyQt6 import QtWidgets
from qpos import app, login
from qpos.view.main import Ui_MainWindow

userId = None # indicate active user


class MainApp(Ui_MainWindow):

  def __init__(self):
      self.win = QtWidgets.QMainWindow()
      self.setupUi(self.win)
      self.win.setWindowIcon(app.appicon())      
      self.win.show()
      self.check_user()

  def check_user(self):
    global userId
    if userId == None:
      self.login = login.Login()
