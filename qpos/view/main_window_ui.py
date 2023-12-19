# Form implementation generated from reading ui file 'e:\dev\ws-py\QPos\ui\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 648)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#menu_widget, #toolBox {\n"
"    background-color: #3333FF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.menu_widget = QtWidgets.QWidget(parent=self.splitter)
        self.menu_widget.setMinimumSize(QtCore.QSize(150, 0))
        self.menu_widget.setStyleSheet("background-color: #06162d;\n"
"color: #fff;\n"
"border: none;")
        self.menu_widget.setObjectName("menu_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_widget)
        self.gridLayout.setContentsMargins(4, 4, 4, 15)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(parent=self.menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("#toolBox {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"    padding-left:5px;\n"
"    text-align:left;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#toolBox::tab:selected {\n"
"    background-color: #2d9cdb;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"    padding:5px 0px 5px 20px;\n"
"    text-align:left;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"    background-color: #85C1E9;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"    background-color: #3498DB;\n"
"}\n"
"\n"
"")
        self.toolBox.setObjectName("toolBox")
        self.general_page = QtWidgets.QWidget()
        self.general_page.setGeometry(QtCore.QRect(0, 0, 162, 512))
        self.general_page.setObjectName("general_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.general_page)
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48 (2).ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.general_page, icon, "")
        self.cars_page = QtWidgets.QWidget()
        self.cars_page.setGeometry(QtCore.QRect(0, 0, 162, 512))
        self.cars_page.setObjectName("cars_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cars_page)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.cars_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.cars_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.cars_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 350, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/car-4-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.cars_page, icon1, "")
        self.social_media_page = QtWidgets.QWidget()
        self.social_media_page.setGeometry(QtCore.QRect(0, 0, 162, 512))
        self.social_media_page.setObjectName("social_media_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.social_media_page)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.social_media_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.social_media_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 388, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/group-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.social_media_page, icon2, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.main_widget = QtWidgets.QWidget(parent=self.splitter)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.search_widget = QtWidgets.QWidget(parent=self.main_widget)
        self.search_widget.setStyleSheet("#search_widget {background-color: #ABB2B9;}")
        self.search_widget.setObjectName("search_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.search_widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-96-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-31-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.search_frame = QtWidgets.QFrame(parent=self.search_widget)
        self.search_frame.setMinimumSize(QtCore.QSize(300, 30))
        self.search_frame.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_frame.setFont(font)
        self.search_frame.setStyleSheet("#search_frame {\n"
"    border:  1px solid #aa7e6f;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#search_btn {\n"
"    padding:5px 5px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#search_btn:pressed {\n"
"    padding-left: 10px;\n"
"}")
        self.search_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.search_frame)
        self.horizontalLayout_10.setContentsMargins(15, 0, 5, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.search_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_10.addWidget(self.lineEdit_5)
        self.search_btn = QtWidgets.QPushButton(parent=self.search_frame)
        self.search_btn.setStyleSheet("")
        self.search_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/search-3-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_10.addWidget(self.search_btn)
        self.horizontalLayout.addWidget(self.search_frame)
        spacerItem4 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.auth_user = QtWidgets.QPushButton(parent=self.search_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth_user.sizePolicy().hasHeightForWidth())
        self.auth_user.setSizePolicy(sizePolicy)
        self.auth_user.setMinimumSize(QtCore.QSize(30, 30))
        self.auth_user.setMaximumSize(QtCore.QSize(30, 30))
        self.auth_user.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.auth_user.setStyleSheet("border-radius : 15; \n"
"background-color: white;")
        self.auth_user.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/user-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.auth_user.setIcon(icon5)
        self.auth_user.setIconSize(QtCore.QSize(20, 20))
        self.auth_user.setFlat(True)
        self.auth_user.setObjectName("auth_user")
        self.horizontalLayout.addWidget(self.auth_user)
        self.gridLayout_4.addWidget(self.search_widget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.main_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("#tabWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"    margin-left: 3px;\n"
"    image: url(:/icon/icon/x-mark-4-32.ico)\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    \n"
"    image: url(:/icon/icon/x-mark-4-48.ico);\n"
"}")
        self.tabWidget.setIconSize(QtCore.QSize(10, 10))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)
        self.tabWidget.setCurrentIndex(-1)
        self.pushButton_8.toggled['bool'].connect(self.menu_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QPos"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "Dashboard"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.general_page), _translate("MainWindow", "General"))
        self.pushButton_3.setText(_translate("MainWindow", "Toyota"))
        self.pushButton_4.setText(_translate("MainWindow", "Lexus"))
        self.pushButton_5.setText(_translate("MainWindow", "Mazda"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.cars_page), _translate("MainWindow", "Cars"))
        self.pushButton_6.setText(_translate("MainWindow", "YouTube"))
        self.pushButton_7.setText(_translate("MainWindow", "Tumbr"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.social_media_page), _translate("MainWindow", "Social Media"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Search Something..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
