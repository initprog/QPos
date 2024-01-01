# Form implementation generated from reading ui file 'e:\dev\ws-py\QPos\ui\entity.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from qpos.asset import resource_rc
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(694, 617)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pgList = QtWidgets.QWidget()
        self.pgList.setObjectName("pgList")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pgList)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtMessage = QtWidgets.QTextEdit(parent=self.pgList)
        self.txtMessage.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txtMessage.setAutoFillBackground(False)
        self.txtMessage.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.txtMessage.setReadOnly(True)
        self.txtMessage.setObjectName("txtMessage")
        self.verticalLayout.addWidget(self.txtMessage)
        self.lblHeader = QtWidgets.QLabel(parent=self.pgList)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblHeader.setFont(font)
        self.lblHeader.setObjectName("lblHeader")
        self.verticalLayout.addWidget(self.lblHeader)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAdd = QtWidgets.QPushButton(parent=self.pgList)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_2.addWidget(self.btnAdd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.search = QtWidgets.QLineEdit(parent=self.pgList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setMinimumSize(QtCore.QSize(300, 0))
        self.search.setStatusTip("")
        self.search.setWhatsThis("")
        self.search.setClearButtonEnabled(True)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tvTable = QtWidgets.QTableView(parent=self.pgList)
        self.tvTable.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.tvTable.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tvTable.setObjectName("tvTable")
        self.verticalLayout.addWidget(self.tvTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.stackedWidget.addWidget(self.pgList)
        self.pgDetail = QtWidgets.QWidget()
        self.pgDetail.setObjectName("pgDetail")
        self.stackedWidget.addWidget(self.pgDetail)
        self.pgNoRecord = QtWidgets.QWidget()
        self.pgNoRecord.setObjectName("pgNoRecord")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pgNoRecord)
        self.verticalLayout_3.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.lblIcon = QtWidgets.QLabel(parent=self.pgNoRecord)
        self.lblIcon.setMinimumSize(QtCore.QSize(128, 128))
        self.lblIcon.setMaximumSize(QtCore.QSize(128, 128))
        self.lblIcon.setText("")
        self.lblIcon.setPixmap(QtGui.QPixmap(":/icon/icon/folder-128.png"))
        self.lblIcon.setScaledContents(True)
        self.lblIcon.setObjectName("lblIcon")
        self.verticalLayout_3.addWidget(self.lblIcon, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lblEntity = QtWidgets.QLabel(parent=self.pgNoRecord)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblEntity.setFont(font)
        self.lblEntity.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblEntity.setObjectName("lblEntity")
        self.verticalLayout_3.addWidget(self.lblEntity)
        self.lblDescription = QtWidgets.QLabel(parent=self.pgNoRecord)
        self.lblDescription.setMinimumSize(QtCore.QSize(0, 60))
        self.lblDescription.setWordWrap(True)
        self.lblDescription.setObjectName("lblDescription")
        self.verticalLayout_3.addWidget(self.lblDescription)
        self.btnCreate = QtWidgets.QPushButton(parent=self.pgNoRecord)
        self.btnCreate.setMinimumSize(QtCore.QSize(120, 0))
        self.btnCreate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.btnCreate.setFont(font)
        self.btnCreate.setObjectName("btnCreate")
        self.verticalLayout_3.addWidget(self.btnCreate, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.pgNoRecord)
        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblHeader.setText(_translate("Form", "Entity Name"))
        self.btnAdd.setText(_translate("Form", "Add Entity"))
        self.search.setPlaceholderText(_translate("Form", "search item"))
        self.lblEntity.setText(_translate("Form", "Item Category"))
        self.lblDescription.setText(_translate("Form", "Categories help organize your items, determine how customers navigate your online store, report on item sales and route items to specific printers."))
        self.btnCreate.setText(_translate("Form", "Create category"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
