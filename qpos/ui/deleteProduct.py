import sqlite3
from contextlib import closing
from qpos.db import conn
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
        self.layoutWidget.setGeometry(QtCore.QRect(12, 8, 1518, 122))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.timeLabel.setMinimumSize(QtCore.QSize(250, 80))
        self.timeLabel.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("Sego UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.timeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.timeBox = QtWidgets.QTextBrowser(self.layoutWidget)
        self.timeBox.setMinimumSize(QtCore.QSize(250, 80))
        self.timeBox.setMaximumSize(QtCore.QSize(250, 80))
        self.timeBox.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.timeBox.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.horizontalLayout.addWidget(self.timeBox)
        self.addProductBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.addProductBtn.setEnabled(False)
        self.addProductBtn.setMinimumSize(QtCore.QSize(300, 120))
        self.addProductBtn.setMaximumSize(QtCore.QSize(300, 120))
        self.addProductBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.addProductBtn.setObjectName("addProductBtn")
        self.horizontalLayout.addWidget(self.addProductBtn)
        self.changePriceBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.changePriceBtn.setEnabled(False)
        self.changePriceBtn.setMinimumSize(QtCore.QSize(300, 120))
        self.changePriceBtn.setMaximumSize(QtCore.QSize(300, 120))
        self.changePriceBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.changePriceBtn.setObjectName("changePriceBtn")
        self.horizontalLayout.addWidget(self.changePriceBtn)
        self.goBackBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.goBackBtn.setMinimumSize(QtCore.QSize(300, 120))
        self.goBackBtn.setMaximumSize(QtCore.QSize(300, 120))
        self.goBackBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 150, 1554, 122))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chickenBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.chickenBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.chickenBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.chickenBtn.setStyleSheet("font: 75 35pt \"Sego UI\";\n"
"background-color: rgb(252, 190, 113);")
        self.chickenBtn.setObjectName("chickenBtn")
        self.horizontalLayout_2.addWidget(self.chickenBtn)
        self.beverageBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.beverageBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.beverageBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.beverageBtn.setStyleSheet("font: 75 35pt \"Sego UI\";\n"
"background-color: rgb(85, 201, 234);")
        self.beverageBtn.setObjectName("beverageBtn")
        self.horizontalLayout_2.addWidget(self.beverageBtn)
        self.othersBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.othersBtn.setMinimumSize(QtCore.QSize(400, 120))
        self.othersBtn.setMaximumSize(QtCore.QSize(400, 120))
        self.othersBtn.setStyleSheet("font: 75 35pt \"Sego UI\";\n"
"background-color: rgb(159, 217, 111);")
        self.othersBtn.setObjectName("othersBtn")
        self.horizontalLayout_2.addWidget(self.othersBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 280, 721, 571))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.showProductBox = QtWidgets.QListView(Form)
        self.showProductBox.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.showProductBox.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.showProductBox.setGeometry(QtCore.QRect(20, 290, 700, 550))
        self.showProductBox.setMinimumSize(QtCore.QSize(700, 550))
        self.showProductBox.setMaximumSize(QtCore.QSize(700, 550))
        self.showProductBox.setObjectName("showProductBox")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(750, 300, 650, 350))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.productNameLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.productNameLabel.setMinimumSize(QtCore.QSize(200, 150))
        self.productNameLabel.setMaximumSize(QtCore.QSize(200, 150))
        self.productNameLabel.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.productNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.productNameLabel.setObjectName("productNameLabel")
        self.horizontalLayout_4.addWidget(self.productNameLabel)
        self.productNameBox = QtWidgets.QLineEdit(self.layoutWidget2)
        self.productNameBox.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.productNameBox.setMinimumSize(QtCore.QSize(400, 150))
        self.productNameBox.setMaximumSize(QtCore.QSize(400, 150))
        self.productNameBox.setObjectName("productNameBox")
        self.horizontalLayout_4.addWidget(self.productNameBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.deleteProductBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.deleteProductBtn.setMinimumSize(QtCore.QSize(200, 100))
        self.deleteProductBtn.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Sego UI")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.deleteProductBtn.setFont(font)
        self.deleteProductBtn.setStyleSheet("font: 75 25pt \"Sego UI\";\n"
                                            "background-color: rgb(255, 94, 97);")
        self.deleteProductBtn.setObjectName("deleteProductBtn")
        self.horizontalLayout_3.addWidget(self.deleteProductBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete Product"))
        self.timeLabel.setText(_translate("Form", "Time: "))
        self.addProductBtn.setText(_translate("Form", "Add Item"))
        self.changePriceBtn.setText(_translate("Form", "Price Change"))
        self.goBackBtn.setText(_translate("Form", "Go Back"))
        self.chickenBtn.setText(_translate("Form", "Chicken"))
        self.beverageBtn.setText(_translate("Form", "Beverage"))
        self.othersBtn.setText(_translate("Form", "Etc"))
        self.productNameLabel.setText(_translate("Form", "Product Name"))
        self.deleteProductBtn.setText(_translate("Form", "삭제"))

class DeleteProduct(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.chickenBtn.clicked.connect(self.sortByChicken)
        self.beverageBtn.clicked.connect(self.sortByDrink)
        self.othersBtn.clicked.connect(self.sortByOther)
        self.deleteProductBtn.clicked.connect(self.deleteProduct)
        self.showProductBox.clicked.connect(self.passProductName)
        self.addProductBtn.clicked.connect(self.gotoAddProduct)
        self.changePriceBtn.clicked.connect(self.gotoChangePrice)
        self.goBackBtn.clicked.connect(self.goBack)
        self.show()

    @pyqtSlot()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = str(current.time().hour())
        min  = str(current.time().minute())
        sec = str(current.time().second())
        self.timeBox.setPlainText(hour+":"+min+":"+sec)

    @pyqtSlot()
    def sortByChicken(self):
        model = QtGui.QStandardItemModel()
        model.clear()
        sql = "SELECT * FROM Product WHERE Category='Chicken'"
        try:
            with closing(conn()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql)
                    data = cursor.fetchall()

            for i in data:
                model.appendRow(QtGui.QStandardItem(str(i[1])))
            self.showProductBox.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @pyqtSlot()
    def sortByDrink(self):
        model = QtGui.QStandardItemModel()
        model.clear()
        sql = "SELECT * FROM Product WHERE Category='Beverage'"
        try:
            with closing(conn()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql)
                    data = cursor.fetchall()

            for i in data:
                model.appendRow(QtGui.QStandardItem(str(i[1])))
            self.showProductBox.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @pyqtSlot()
    def sortByOther(self):
        model = QtGui.QStandardItemModel()
        model.clear()
        sql = "SELECT * FROM Product WHERE Category='Etc'"
        try:
            with closing(conn()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql)
                    data = cursor.fetchall()

            for i in data:
                model.appendRow(QtGui.QStandardItem(str(i[1])))
            self.showProductBox.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @pyqtSlot(QModelIndex)
    def passProductName(self, index):
        self.productNameBox.setText(index.data())

    @pyqtSlot()
    def deleteProduct(self):
        productName = self.productNameBox.text()
        flag = self.checkValidation(productName)
        if flag==False:
            return
        sql = "DELETE FROM Product WHERE Name='%s'" % productName
        try:
            with closing(conn()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql)
                    connection.commit()

        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("문제가 발생하여 삭제가 완료되지 않았습니다\n재시도 하십시오")
            warning.setWindowTitle("오류")
            warning.exec()
        self.productNameBox.clear()
        self.sortByChicken()

    @pyqtSlot()
    def checkValidation(self, name):
        if name == '':
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setText("품목명을 기재하십시오.")
            warning.setWindowTitle("오류")
            warning.exec()
            return False
        sql = "SELECT * FROM Product WHERE Name='%s'" % name
        try:
            with closing(conn()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql)
                    nameCheck = cursor.fetchall()

            if nameCheck == []:
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Warning)
                warning.setText("존재하지 않는 품목명입니다.")
                warning.setWindowTitle("오류")
                warning.exec()
                return False
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return False

    @pyqtSlot()
    def gotoAddProduct(self):
        pass

    @pyqtSlot()
    def gotoChangePrice(self):
        pass

    @pyqtSlot()
    def goBack(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    e = DeleteProduct()
    sys.exit(app.exec_())