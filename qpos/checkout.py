from PyQt6 import QtGui, QtCore, QtWidgets
#from qpos.view.orderMain import Ui_Form
from qpos.view.order_main_ui import Ui_Form
from contextlib import closing
from qpos.db import conn
import sqlite3
from qpos.view import refund, choosePayment
from qpos import admin

class Checkout(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Checkout, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.orderNo = 1
        self.orderedItems = []
        self.totalPrice = 0
        self.orderModel = QtGui.QStandardItemModel()
        self.orderModel.setHorizontalHeaderLabels(['No', 'Product Name', 'Qty', 'Amount'])
        self.ui.sortByChickenBtn.clicked.connect(self.sortByChicken)
        self.ui.sortByDrinkBtn.clicked.connect(self.sortByDrink)
        self.ui.sortByOtherBtn.clicked.connect(self.sortByOther)
        self.ui.productList.doubleClicked.connect(self.addOrder)
        self.ui.resetBtn.clicked.connect(self.reset)
        self.ui.orderList.setModel(self.orderModel)
        self.ui.orderList.resizeColumnsToContents()
        self.ui.totalPriceBox.setPlainText('{:,}'.format(self.totalPrice))
        self.ui.refundBtn.clicked.connect(self.refundBtnClicked)
        self.ui.payBtn.clicked.connect(self.pay)
        self.ui.admBtn.clicked.connect(self.openAdmin)
        
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msgBox.exec_()

    @QtCore.pyqtSlot()
    def refundBtnClicked(self):
        refund.Refund(self)

    @QtCore.pyqtSlot()
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
            self.ui.productList.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @QtCore.pyqtSlot()
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
            self.ui.productList.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @QtCore.pyqtSlot()
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
            self.ui.productList.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @QtCore.pyqtSlot()
    def reset(self):
        self.orderNo = 1
        self.orderedItems = []
        self.totalPrice = 0
        self.orderModel.clear()
        self.orderModel.setHorizontalHeaderLabels(['No', 'Product Name', 'Qty', 'Amount'])
        self.ui.orderList.setModel(self.orderModel)
        self.ui.totalPriceBox.setPlainText(str(self.totalPrice))

    @QtCore.pyqtSlot()
    def pay(self):
        if self.orderedItems == []:
            self.showMessageBox('Error','There are no item to pay for')
            #warning = QMessageBox()
            #warning.setIcon(QMessageBox.Warning)
            #warning.setText("결제할 품목이 없습니다")
            #warning.setWindowTitle("오류")
            #warning.exec()
            return False
        else:
            #self.close()
            choosePayment.ChoosePayment(self)
            #choosePayment.orderMain.totalPrice = self.totalPrice
            #choosePayment.orderMain.orderModel = self.orderModel
            #choosePayment.orderMain.orderedItems = self.orderedItems

    @QtCore.pyqtSlot()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = current.time().hour()
        min  = current.time().minute()
        sec = current.time().second()
        self.ui.timeBox.setPlainText(f"{hour:02d}:{min:02d}:{sec:02d}")

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def addOrder(self, index):
        productName = index.data()
        sql = "SELECT Price FROM Product WHERE Name='%s'" % productName
        try:
            with closing(conn()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql)
                    data = cursor.fetchall()

            price = int(data[0][0])
            if productName in self.orderedItems:
                orderRow = int(self.orderedItems.index(productName))
                orderQuantity = int(self.orderModel.index(orderRow, 2).data()) + 1
                self.orderModel.setItem(orderRow, 2, QtGui.QStandardItem('{:,}'.format(orderQuantity)))
                self.orderModel.setItem(orderRow, 3, QtGui.QStandardItem('{:,}'.format(orderQuantity * price)))
            else:
                self.orderedItems.append(productName)
                row = [QtGui.QStandardItem('{:,}'.format(self.orderNo)), QtGui.QStandardItem(productName),
                       QtGui.QStandardItem('1'), QtGui.QStandardItem('{:,}'.format(price))]
                self.orderModel.appendRow(row)
                self.orderNo += 1
            self.totalPrice += price
            self.ui.orderList.resizeColumnsToContents()
            self.ui.totalPriceBox.setPlainText('{:,}'.format(self.totalPrice))
            self.ui.orderList.setModel(self.orderModel)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    def openAdmin(self):
        self.Form = QtWidgets.QMainWindow()
        self.ds = admin.AdminAuth()
        #self.close()

