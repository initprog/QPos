import sys
from PyQt6 import QtGui, QtWidgets, QtCore

"""child widget calling parent's method"""

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.do_something() #sanity check
        self.cw = ChildWidget(self)
        self.setCentralWidget(self.cw)
        self.show()

    def do_something(self):
        print('doing something!')


class ChildWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ChildWidget, self).__init__(parent=parent)

        self.button1 = QtWidgets.QPushButton()
        self.button1.setText("Button 1")
        self.button1.clicked.connect(self.do_something_else)

        self.button2 = QtWidgets.QPushButton()
        self.button2.setText('Button 2')
        self.button2.clicked.connect(self.parent().do_something)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        self.show()

    def do_something_else(self):
        print('doing something else!')


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()