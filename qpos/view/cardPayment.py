from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 6, 1422, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.timeLabel.setMinimumSize(QtCore.QSize(400, 100))
        self.timeLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.timeLabel.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.timeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_2.addWidget(self.timeLabel)
        self.timeBox = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.timeBox.setStyleSheet("font: 75 40pt \"Sego UI\";")
        self.timeBox.setMinimumSize(QtCore.QSize(400, 100))
        self.timeBox.setMaximumSize(QtCore.QSize(400, 100))
        self.timeBox.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.timeBox.setReadOnly(True)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout_2.addWidget(self.timeBox)
        spacerItem = QtWidgets.QSpacerItem(200, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.goBackBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.goBackBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.goBackBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Sego UI")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.goBackBtn.setFont(font)
        self.goBackBtn.setStyleSheet("font: 75 35pt \"Sego UI\";\n"
"background-color: rgb(255, 129, 112);")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(190, 180, 460, 631))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn9.setMinimumSize(QtCore.QSize(150, 150))
        self.btn9.setMaximumSize(QtCore.QSize(150, 150))
        self.btn9.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 0, 2, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn8.setMinimumSize(QtCore.QSize(150, 150))
        self.btn8.setMaximumSize(QtCore.QSize(150, 150))
        self.btn8.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 0, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn7.setMinimumSize(QtCore.QSize(150, 150))
        self.btn7.setMaximumSize(QtCore.QSize(150, 150))
        self.btn7.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 0, 0, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn4.setMinimumSize(QtCore.QSize(150, 150))
        self.btn4.setMaximumSize(QtCore.QSize(150, 150))
        self.btn4.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn5.setMinimumSize(QtCore.QSize(150, 150))
        self.btn5.setMaximumSize(QtCore.QSize(150, 150))
        self.btn5.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn2.setMinimumSize(QtCore.QSize(150, 150))
        self.btn2.setMaximumSize(QtCore.QSize(150, 150))
        self.btn2.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 2, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn6.setMinimumSize(QtCore.QSize(150, 150))
        self.btn6.setMaximumSize(QtCore.QSize(150, 150))
        self.btn6.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn1.setMinimumSize(QtCore.QSize(150, 150))
        self.btn1.setMaximumSize(QtCore.QSize(150, 150))
        self.btn1.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 2, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn3.setMinimumSize(QtCore.QSize(150, 150))
        self.btn3.setMaximumSize(QtCore.QSize(150, 150))
        self.btn3.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 2, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.splitter)
        self.btn0.setMinimumSize(QtCore.QSize(460, 150))
        self.btn0.setMaximumSize(QtCore.QSize(460, 150))
        self.btn0.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.btn0.setObjectName("btn0")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(707, 220, 691, 461))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.priceLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.priceLabel.setMinimumSize(QtCore.QSize(150, 100))
        self.priceLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.priceLabel.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.priceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.priceLabel.setObjectName("priceLabel")
        self.horizontalLayout_4.addWidget(self.priceLabel)
        self.priceBox = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        self.priceBox.setMinimumSize(QtCore.QSize(400, 100))
        self.priceBox.setMaximumSize(QtCore.QSize(400, 100))
        self.priceBox.setReadOnly(True)
        self.priceBox.setObjectName("priceBox")
        self.horizontalLayout_4.addWidget(self.priceBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cardNoLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.cardNoLabel.setMinimumSize(QtCore.QSize(150, 100))
        self.cardNoLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.cardNoLabel.setStyleSheet("font: 75 35pt \"Sego UI\";")
        self.cardNoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cardNoLabel.setObjectName("cardNoLabel")
        self.horizontalLayout_5.addWidget(self.cardNoLabel)
        self.cardNoBox = QtWidgets.QTextEdit(self.layoutWidget2)
        self.cardNoBox.setMinimumSize(QtCore.QSize(400, 100))
        self.cardNoBox.setMaximumSize(QtCore.QSize(400, 100))
        self.cardNoBox.setReadOnly(True)
        self.cardNoBox.setObjectName("cardNoBox")
        self.horizontalLayout_5.addWidget(self.cardNoBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.payBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.payBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.payBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Sego UI")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.payBtn.setFont(font)
        self.payBtn.setStyleSheet("font: 75 35pt \"Sego UI\";\n"
"background-color: rgb(170, 170, 127);")
        self.payBtn.setObjectName("payBtn")
        self.horizontalLayout_3.addWidget(self.payBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Card Payment"))
        self.timeLabel.setText(_translate("Form", "Time: "))
        self.goBackBtn.setText(_translate("Form", "Go Back"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn3.setText(_translate("Form", "3"))
        self.btn0.setText(_translate("Form", "0"))
        self.priceLabel.setText(_translate("Form", "결제 Amount"))
        self.cardNoLabel.setText(_translate("Form", "Card 번호"))
        self.payBtn.setText(_translate("Form", "결제하기"))

class CardPayment(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    e = CardPayment()
    sys.exit(app.exec_())

