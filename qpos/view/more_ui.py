# Form implementation generated from reading ui file 'c:\dev\ws-py\QPos\ui\more.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 387)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.btnCategory = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCategory.setFont(font)
        self.btnCategory.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnCategory.setStyleSheet("text-align: left;")
        self.btnCategory.setFlat(True)
        self.btnCategory.setObjectName("btnCategory")
        self.gridLayout.addWidget(self.btnCategory, 0, 0, 1, 1)
        self.btnPaymentTerm = QtWidgets.QPushButton(parent=Form)
        self.btnPaymentTerm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnPaymentTerm.setStyleSheet("text-align: left;")
        self.btnPaymentTerm.setFlat(True)
        self.btnPaymentTerm.setObjectName("btnPaymentTerm")
        self.gridLayout.addWidget(self.btnPaymentTerm, 1, 0, 1, 1)
        self.btnLocator = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnLocator.setFont(font)
        self.btnLocator.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnLocator.setStyleSheet("text-align: left;")
        self.btnLocator.setFlat(True)
        self.btnLocator.setObjectName("btnLocator")
        self.gridLayout.addWidget(self.btnLocator, 1, 2, 1, 1)
        self.btnWarehouse = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnWarehouse.setFont(font)
        self.btnWarehouse.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnWarehouse.setStyleSheet("text-align: left;")
        self.btnWarehouse.setFlat(True)
        self.btnWarehouse.setObjectName("btnWarehouse")
        self.gridLayout.addWidget(self.btnWarehouse, 0, 2, 1, 1)
        self.btnHours = QtWidgets.QPushButton(parent=Form)
        self.btnHours.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnHours.setStyleSheet("text-align: left;")
        self.btnHours.setFlat(True)
        self.btnHours.setObjectName("btnHours")
        self.gridLayout.addWidget(self.btnHours, 2, 0, 1, 1)
        self.btnUnit = QtWidgets.QPushButton(parent=Form)
        self.btnUnit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnUnit.setStyleSheet("text-align: left;")
        self.btnUnit.setFlat(True)
        self.btnUnit.setObjectName("btnUnit")
        self.gridLayout.addWidget(self.btnUnit, 1, 1, 1, 1)
        self.btnJobAssignment = QtWidgets.QPushButton(parent=Form)
        self.btnJobAssignment.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnJobAssignment.setStyleSheet("text-align: left;")
        self.btnJobAssignment.setFlat(True)
        self.btnJobAssignment.setObjectName("btnJobAssignment")
        self.gridLayout.addWidget(self.btnJobAssignment, 2, 1, 1, 1)
        self.btnCustomerGroup = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCustomerGroup.setFont(font)
        self.btnCustomerGroup.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnCustomerGroup.setStyleSheet("text-align: left;")
        self.btnCustomerGroup.setFlat(True)
        self.btnCustomerGroup.setObjectName("btnCustomerGroup")
        self.gridLayout.addWidget(self.btnCustomerGroup, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnCategory.setText(_translate("Form", "Item Category"))
        self.btnPaymentTerm.setText(_translate("Form", "Payment Terms"))
        self.btnLocator.setText(_translate("Form", "Locator"))
        self.btnWarehouse.setText(_translate("Form", "Warehouse"))
        self.btnHours.setText(_translate("Form", "Business Hours"))
        self.btnUnit.setText(_translate("Form", "Unit of Measurement"))
        self.btnJobAssignment.setText(_translate("Form", "Job Assignment"))
        self.btnCustomerGroup.setText(_translate("Form", "Customer Group"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())