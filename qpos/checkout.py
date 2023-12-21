from PyQt6 import QtGui, QtCore, QtWidgets
from qpos.view.orderMain import Ui_Form
from contextlib import closing
from qpos.db import conn
import sqlite3
from qpos.view import refund, choosePayment
from qpos import admin

#order list model
orderNo = 1
orderedItems = []
totalPrice = 0
orderModel = QtGui.QStandardItemModel()
orderModel.setHorizontalHeaderLabels(['No', 'Product Name', 'Qty', 'Amount'])

class Checkout(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Checkout, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.ui.sortByChickenBtn.clicked.connect(self.sortByChicken)
        self.ui.sortByDrinkBtn.clicked.connect(self.sortByDrink)
        self.ui.sortByOtherBtn.clicked.connect(self.sortByOther)
        self.ui.productList.doubleClicked.connect(self.addOrder)
        self.ui.resetBtn.clicked.connect(self.reset)
        self.ui.orderList.setModel(orderModel)
        self.ui.orderList.resizeColumnsToContents()
        self.ui.totalPriceBox.setPlainText('{:,}'.format(totalPrice))
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
            self.productList.setModel(model)
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
            self.productList.setModel(model)
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
            self.productList.setModel(model)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    @QtCore.pyqtSlot()
    def reset(self):
        global orderNo, orderedItems, totalPrice
        orderNo = 1
        orderedItems = []
        totalPrice = 0
        orderModel.clear()
        orderModel.setHorizontalHeaderLabels(['No', 'Product Name', 'Qty', 'Amount'])
        self.orderList.setModel(orderModel)
        self.totalPriceBox.setPlainText(str(totalPrice))

    @QtCore.pyqtSlot()
    def pay(self):
        global totalPrice, orderedItems
        if orderedItems == []:
            self.showMessageBox('Error','There are no item to pay for')
            #warning = QMessageBox()
            #warning.setIcon(QMessageBox.Warning)
            #warning.setText("결제할 품목이 없습니다")
            #warning.setWindowTitle("오류")
            #warning.exec()
            return False
        else:
            self.close()
            choosePayment.ChoosePayment(self)
            choosePayment.orderMain.totalPrice = totalPrice
            choosePayment.orderMain.orderModel = orderModel
            choosePayment.orderMain.orderedItems = orderedItems

    @QtCore.pyqtSlot()
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        hour = current.time().hour()
        min  = current.time().minute()
        sec = current.time().second()
        self.ui.timeBox.setPlainText(f"{hour:02d}:{min:02d}:{sec:02d}")

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def addOrder(self, index):
        global orderNo, orderedItems, totalPrice
        productName = index.data()
        sql = "SELECT Price FROM Product WHERE Name='%s'" % productName
        try:
            with closing(conn()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql)
                    data = cursor.fetchall()

            price = int(data[0][0])
            if productName in orderedItems:
                orderRow = int(orderedItems.index(productName))
                orderQuantity = int(orderModel.index(orderRow, 2).data()) + 1
                orderModel.setItem(orderRow, 2, QtGui.QStandardItem('{:,}'.format(orderQuantity)))
                orderModel.setItem(orderRow, 3, QtGui.QStandardItem('{:,}'.format(orderQuantity * price)))
            else:
                orderedItems.append(productName)
                row = [QtGui.QStandardItem('{:,}'.format(orderNo)), QtGui.QStandardItem(productName),
                       QtGui.QStandardItem('1'), QtGui.QStandardItem('{:,}'.format(price))]
                orderModel.appendRow(row)
                orderNo += 1
            totalPrice += price
            self.ui.orderList.resizeColumnsToContents()
            self.ui.totalPriceBox.setPlainText('{:,}'.format(totalPrice))
            self.ui.orderList.setModel(orderModel)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    def openAdmin(self):
        self.Form = QtWidgets.QMainWindow()
        self.ds = admin.AdminAuth()
        self.close()

