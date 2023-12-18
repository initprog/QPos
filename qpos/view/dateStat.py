from PyQt6 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 240, 901, 651))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 899, 649))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 0, 806, 102))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tableBtn = QtWidgets.QPushButton(self.layoutWidget_3)
        self.tableBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.tableBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.tableBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.tableBtn.setObjectName("tableBtn")
        self.horizontalLayout_7.addWidget(self.tableBtn)
        self.graphBtn = QtWidgets.QPushButton(self.layoutWidget_3)
        self.graphBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.graphBtn.setMaximumSize(QtCore.QSize(400, 100))
        self.graphBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.graphBtn.setObjectName("graphBtn")
        self.horizontalLayout_7.addWidget(self.graphBtn)
        self.viewLayout = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.viewLayout)
        self.viewLayout.setGeometry(QtCore.QRect(10, 110, 881, 531))
        self.viewBox = QtWidgets.QTableWidget(self.viewLayout)
        self.viewBox.setStyleSheet("font: 75 12pt \"Sego UI\";")
        self.viewBox.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.viewBox.setObjectName("viewBox")
        self.graphBox = pg.PlotWidget(self.scrollAreaWidgetContents)
        self.graphBox.setBackground('w')
        self.verticalLayout_1.addWidget(self.viewBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(370, 80, 201, 261))
        self.widget.setObjectName("widget")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(920, 260, 581, 631))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.salesTotalLabel = QtWidgets.QLabel(self.layoutWidget)
        self.salesTotalLabel.setMinimumSize(QtCore.QSize(250, 80))
        self.salesTotalLabel.setMaximumSize(QtCore.QSize(250, 80))
        self.salesTotalLabel.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.salesTotalLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.salesTotalLabel.setObjectName("salesTotalLabel")
        self.horizontalLayout_4.addWidget(self.salesTotalLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.salesTotalBox = QtWidgets.QTextBrowser(self.splitter)
        self.salesTotalBox.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.salesTotalBox.setMinimumSize(QtCore.QSize(450, 100))
        self.salesTotalBox.setMaximumSize(QtCore.QSize(450, 100))
        self.salesTotalBox.setObjectName("salesTotalBox")
        self.wonLabel1 = QtWidgets.QLabel(self.splitter)
        self.wonLabel1.setMinimumSize(QtCore.QSize(100, 100))
        self.wonLabel1.setMaximumSize(QtCore.QSize(100, 100))
        self.wonLabel1.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.wonLabel1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wonLabel1.setObjectName("wonLabel1")
        self.verticalLayout.addWidget(self.splitter)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.salesAvgLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.salesAvgLabel.setMinimumSize(QtCore.QSize(250, 80))
        self.salesAvgLabel.setMaximumSize(QtCore.QSize(250, 80))
        self.salesAvgLabel.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.salesAvgLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.salesAvgLabel.setObjectName("salesAvgLabel")
        self.horizontalLayout_5.addWidget(self.salesAvgLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.salesAvgBox = QtWidgets.QTextBrowser(self.splitter_3)
        self.salesAvgBox.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.salesAvgBox.setMinimumSize(QtCore.QSize(450, 100))
        self.salesAvgBox.setMaximumSize(QtCore.QSize(450, 100))
        self.salesAvgBox.setObjectName("salesAvgBox")
        self.wonLabel2 = QtWidgets.QLabel(self.splitter_3)
        self.wonLabel2.setMinimumSize(QtCore.QSize(100, 100))
        self.wonLabel2.setMaximumSize(QtCore.QSize(100, 100))
        self.wonLabel2.setStyleSheet("font: 75 20pt \"Sego UI\";")
        self.wonLabel2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wonLabel2.setObjectName("wonLabel2")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 1472, 102))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeLabel = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        self.timeLabel.setMinimumSize(QtCore.QSize(170, 100))
        self.timeLabel.setMaximumSize(QtCore.QSize(170, 100))
        self.timeLabel.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.timeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.timeBox = QtWidgets.QTextEdit(self.layoutWidget2)
        self.timeBox.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.timeBox.setMinimumSize(QtCore.QSize(200, 50))
        self.timeBox.setMaximumSize(QtCore.QSize(200, 50))
        self.timeBox.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.timeBox.setObjectName("timeBox")
        self.horizontalLayout.addWidget(self.timeBox)
        self.productStatBtn = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productStatBtn.sizePolicy().hasHeightForWidth())
        self.productStatBtn.setSizePolicy(sizePolicy)
        self.productStatBtn.setMinimumSize(QtCore.QSize(280, 100))
        self.productStatBtn.setMaximumSize(QtCore.QSize(250, 100))
        self.productStatBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.productStatBtn.setObjectName("productStatBtn")
        self.horizontalLayout.addWidget(self.productStatBtn)
        self.productManagementBtn = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productManagementBtn.sizePolicy().hasHeightForWidth())
        self.productManagementBtn.setSizePolicy(sizePolicy)
        self.productManagementBtn.setMinimumSize(QtCore.QSize(280, 100))
        self.productManagementBtn.setMaximumSize(QtCore.QSize(250, 100))
        self.productManagementBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.productManagementBtn.setObjectName("productManagementBtn")
        self.horizontalLayout.addWidget(self.productManagementBtn)
        self.cashAvailableBtn = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cashAvailableBtn.sizePolicy().hasHeightForWidth())
        self.cashAvailableBtn.setSizePolicy(sizePolicy)
        self.cashAvailableBtn.setMinimumSize(QtCore.QSize(260, 100))
        self.cashAvailableBtn.setMaximumSize(QtCore.QSize(260, 100))
        self.cashAvailableBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.cashAvailableBtn.setObjectName("cashAvailableBtn")
        self.horizontalLayout.addWidget(self.cashAvailableBtn)
        self.goBackBtn = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goBackBtn.sizePolicy().hasHeightForWidth())
        self.goBackBtn.setSizePolicy(sizePolicy)
        self.goBackBtn.setMinimumSize(QtCore.QSize(260, 100))
        self.goBackBtn.setMaximumSize(QtCore.QSize(260, 100))
        self.goBackBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.goBackBtn.setObjectName("goBackBtn")
        self.horizontalLayout.addWidget(self.goBackBtn)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 120, 1312, 104))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startDateLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.startDateLabel.setMinimumSize(QtCore.QSize(200, 100))
        self.startDateLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.startDateLabel.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.startDateLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.startDateLabel.setObjectName("startDateLabel")
        self.horizontalLayout_3.addWidget(self.startDateLabel)
        self.startDate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.startDate.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.startDate.setMinimumSize(QtCore.QSize(200, 100))
        self.startDate.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startDate.setFont(font)
        self.startDate.setObjectName("startDate")
        self.horizontalLayout_3.addWidget(self.startDate)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.endDateLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.endDateLabel.setMinimumSize(QtCore.QSize(200, 100))
        self.endDateLabel.setMaximumSize(QtCore.QSize(200, 100))
        self.endDateLabel.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.endDateLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.endDateLabel.setObjectName("endDateLabel")
        self.horizontalLayout_3.addWidget(self.endDateLabel)
        self.endDate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.endDate.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.endDate.setDate(QtCore.QDate.currentDate())
        self.endDate.setMinimumSize(QtCore.QSize(200, 100))
        self.endDate.setMaximumSize(QtCore.QSize(200, 100))
        self.endDate.setMinimumDate(self.startDate.date())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endDate.setFont(font)
        self.endDate.setObjectName("endDate")
        self.horizontalLayout_3.addWidget(self.endDate)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.searchBtn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.searchBtn.setMinimumSize(QtCore.QSize(400, 100))
        self.searchBtn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Sego UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.searchBtn.setFont(font)
        self.searchBtn.setStyleSheet("font: 75 25pt \"Sego UI\";")
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout_3.addWidget(self.searchBtn)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.layoutWidget.raise_()
        self.widget.raise_()
        self.scrollArea.raise_()
        self.splitter_2.raise_()
        self.layoutWidget_2.raise_()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableBtn.setText(_translate("Form", "Graph"))
        self.graphBtn.setText(_translate("Form", "Graph2"))
        self.salesTotalLabel.setText(_translate("Form", "Total sales for the period"))
        self.wonLabel1.setText(_translate("Form", "Won"))
        self.salesAvgLabel.setText(_translate("Form", "Period Sales Average"))
        self.wonLabel2.setText(_translate("Form", "Won"))
        self.timeLabel.setText(_translate("Form", "Time: "))
        self.productStatBtn.setText(_translate("Form", "View Statistics by Item"))
        self.productManagementBtn.setText(_translate("Form", "Item Management"))
        self.cashAvailableBtn.setText(_translate("Form", "Material Management"))
        self.goBackBtn.setText(_translate("Form", "Go Back"))
        self.startDateLabel.setText(_translate("Form", "Start Date"))
        self.endDateLabel.setText(_translate("Form", "End Date"))
        self.searchBtn.setText(_translate("Form", "Check"))

    # change widget attribute by statflag(=which)
    def changeWidgetAttr(self, form, which):
        if which == 'table':
            self.verticalLayout_1.removeWidget(self.graphBox)
            self.verticalLayout_1.removeWidget(self.viewBox)
            self.graphBox.hide()
            self.verticalLayout_1.addWidget(self.viewBox)

        elif which == 'graph':
            self.verticalLayout_1.removeWidget(self.viewBox)
            self.verticalLayout_1.removeWidget(self.graphBox)
            self.verticalLayout_1.addWidget(self.graphBox)
            self.graphBox.show()

    #delete plotwidget and create it again
    def redrawPlotWidget(self, xlist, ylist, axisname):
        xdict = dict(enumerate(self.xlist))
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])

        self.graphBox.deleteLater()
        self.graphBox = pg.PlotWidget(self.scrollAreaWidgetContents, axisItems={'bottom':stringaxis})
        self.verticalLayout_1.addWidget(self.graphBox)
        self.graphBox.setBackground('w')
        self.graphBox.setLabel('bottom',axisname, color='red')
        self.graphBox.setLabel('left','price', color='blue')
        self.graphBox.showGrid(x=True, y=True)

        pen = pg.mkPen(color=(255,0,0))
        self.graphBox.plot(list(xdict.keys()), self.ylist, pen=pen, symbol='o')

        self.title = 'sort by '+axisname
        self.graphBox.setTitle(self.title, color=(0,0,0))




