from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(1500, 900)
        #Form.setMinimumSize(QtCore.QSize(1500, 900))
        #Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(740, 230, 751, 661))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.orderList = QtWidgets.QTableView(self.splitter_2)
        self.orderList.setMinimumSize(QtCore.QSize(0, 380))
        self.orderList.setMaximumSize(QtCore.QSize(16777215, 380))
        self.orderList.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.orderList.setObjectName("orderList")
        self.orderList.verticalHeader().setVisible(False)
        self.orderList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.orderList.resizeColumnsToContents()
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(120, 80))
        self.label_6.setMaximumSize(QtCore.QSize(120, 80))
        self.label_6.setStyleSheet("font: 75 24pt \"Sego UI\";")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.totalPriceBox = QtWidgets.QTextEdit(self.layoutWidget)
        self.totalPriceBox.setStyleSheet("font: 75 45pt \"Sego UI\";")
        self.totalPriceBox.setReadOnly(True)
        self.totalPriceBox.setMinimumSize(QtCore.QSize(400, 80))
        self.totalPriceBox.setMaximumSize(QtCore.QSize(400, 80))
        self.totalPriceBox.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.totalPriceBox.setObjectName("totalPriceBox")
        self.horizontalLayout_5.addWidget(self.totalPriceBox)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(150, 80))
        self.label_8.setMaximumSize(QtCore.QSize(20, 80))
        self.label_8.setStyleSheet("font: 75 24pt \"Sego UI\";")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.resetBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.resetBtn.setMinimumSize(QtCore.QSize(350, 100))
        self.resetBtn.setMaximumSize(QtCore.QSize(350, 100))
        self.resetBtn.setStyleSheet("font: 75 24pt \"Sego UI\";\n"
"background-color: rgb(255, 160, 52);")
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout_6.addWidget(self.resetBtn)
        self.payBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.payBtn.setMinimumSize(QtCore.QSize(350, 100))
        self.payBtn.setMaximumSize(QtCore.QSize(350, 100))
        self.payBtn.setStyleSheet("font: 75 24pt \"Sego UI\";\n"
"background-color: rgb(94, 180, 255);")
        self.payBtn.setObjectName("payBtn")
        self.horizontalLayout_6.addWidget(self.payBtn)
        self.productList = QtWidgets.QListView(Form)
        self.productList.setStyleSheet("font: 75 30pt \"Sego UI\";")
        self.productList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.productList.setGeometry(QtCore.QRect(10, 250, 700, 600))
        self.productList.setMinimumSize(QtCore.QSize(700, 600))
        self.productList.setMaximumSize(QtCore.QSize(700, 600))
        self.productList.setObjectName("productList")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 120, 1220, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sortByChickenBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.sortByChickenBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.sortByChickenBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.sortByChickenBtn.setStyleSheet("font: 75 24pt \"Sego UI\";\n"
"background-color: rgb(252, 190, 113);")
        self.sortByChickenBtn.setObjectName("sortByChickenBtn")
        self.horizontalLayout_3.addWidget(self.sortByChickenBtn)
        self.sortByDrinkBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.sortByDrinkBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.sortByDrinkBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.sortByDrinkBtn.setStyleSheet("font: 75 24pt \"Sego UI\";\n"
"background-color: rgb(85, 201, 234);")
        self.sortByDrinkBtn.setObjectName("sortByDrinkBtn")
        self.horizontalLayout_3.addWidget(self.sortByDrinkBtn)
        self.sortByOtherBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.sortByOtherBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.sortByOtherBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.sortByOtherBtn.setStyleSheet("font: 75 24pt \"Sego UI\";\n"
"background-color: rgb(159, 217, 111);")
        self.sortByOtherBtn.setObjectName("sortByOtherBtn")
        self.horizontalLayout_3.addWidget(self.sortByOtherBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(8, 9, 1481, 102))
        self.layoutWidget3.setObjectName("layoutWidget3")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setMinimumSize(QtCore.QSize(140, 50))
        self.label.setMaximumSize(QtCore.QSize(120, 50))
        self.label.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.timeBox = QtWidgets.QTextEdit(self.layoutWidget3)
        self.timeBox.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.timeBox.setReadOnly(True)
        self.timeBox.setMinimumSize(QtCore.QSize(200, 50))
        self.timeBox.setMaximumSize(QtCore.QSize(200, 50))
        self.timeBox.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout.addWidget(self.timeBox)
        spacerItem1 = QtWidgets.QSpacerItem(200, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.refundBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.refundBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.refundBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Sego UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.refundBtn.setFont(font)
        self.refundBtn.setStyleSheet("font: 75 24pt \"Sego UI\";\n"
"background-color: rgb(255, 129, 112);")
        self.refundBtn.setObjectName("refundBtn")
        self.horizontalLayout.addWidget(self.refundBtn)
        self.admBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.admBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.admBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.admBtn.setStyleSheet("font: 75 24pt \"Sego UI\";\n"
"background-color: rgb(126, 224, 170);")
        self.admBtn.setObjectName("admBtn")
        self.horizontalLayout.addWidget(self.admBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Order Main"))
        self.label_6.setText(_translate("Form", "Sum"))
        self.label_8.setText(_translate("Form", "Won"))
        self.resetBtn.setText(_translate("Form", "Reset"))
        self.payBtn.setText(_translate("Form", "Payment"))
        self.sortByChickenBtn.setText(_translate("Form", "Chicken"))
        self.sortByDrinkBtn.setText(_translate("Form", "Beverage"))
        self.sortByOtherBtn.setText(_translate("Form", "Etc"))
        self.label.setText(_translate("Form", "Time: "))
        self.refundBtn.setText(_translate("Form", "Refund"))
        self.admBtn.setText(_translate("Form", "Management"))

