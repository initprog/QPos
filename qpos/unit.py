from PyQt6 import QtGui, QtCore, QtWidgets
#from PyQt6.QtWidgets import QWidget, QHeaderView
from PyQt6.QtSql import QSqlQuery, QSqlRelationalTableModel
from qpos.db import Qdb
from qpos.view.unit_ui import Ui_Form as Unit_Form
from qpos.view.entity_ui import Ui_Form as Entity_Form

class Unit(QtWidgets.QWidget):
    def __init__(self):
        super(Unit, self).__init__()
        self.ui = Entity_Form()
        self.ui.setupUi(self)
        self.dtl = Unit_Form()

        self.db = Qdb()
        query = QSqlQuery('SELECT COUNT(id) FROM unit', self.db)
        if query.next() and int(query.value(0)) == 0:
            
            self.ui.lblEntity.setText('Your units')
            txt = 'Units are used to specify how you want to measure your items.'
            self.ui.lblDescription.setText(txt)
            self.ui.btnCreate.setText('Create a unit')
            self.ui.lblIcon.setPixmap(QtGui.QPixmap(":/icon/icon/unit-128.png"))
            return

        self.ui.lblHeader.setText('Your Units')
        self.ui.btnAdd.setText('Add a Unit')
        self.ui.stackedWidget.setCurrentWidget(self.ui.pgList)
        
        self.ui.btnAdd.clicked.connect(self.open_detail)
        self.ui.tvTable.doubleClicked.connect(self.open_detail)

        self.model = QSqlRelationalTableModel(db=self.db)
        self.model.setTable("Unit")
        self.model.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, QtCore.QTranslator.tr('ID'))
        self.model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, QtCore.QTranslator.tr('Name'))

        # select one row
        self.ui.tvTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tvTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        
        self.ui.tvTable.setModel(self.model)
        self.ui.tvTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tvTable.horizontalHeader().setStretchLastSection(True)
        
        self.model.select()

        print(f'Row count {self.model.rowCount()}')

    def open_detail(self, index):
        self.dtl = UnitDetail(self, index)
        self.dtl.show()

class UnitDetail(Unit_Form, QtWidgets.QWidget):
    def __init__(self, parent, idx):
        super().__init__()
        self.parent = parent
        self.setupUi(self)

        # use of type hinting
        self.idx:QtCore.QModelIndex = idx

        # mapper
        self.mapper = QtWidgets.QDataWidgetMapper()
        self.mapper.setModel(idx.model())
        self.mapper.addMapping(self.leName, 1)
        self.mapper.setCurrentIndex(idx.row())

        if idx == False:
            self.btnDelete.hide()

        self.btnSave.clicked.connect(self.save)
        self.btnDelete.clicked.connect(self.delete)

    def save(self):
        self.mapper.submit()

    def delete(self):
        self.idx.model().removeRow(self.idx)

    def closeEvent(self, event):
        # saving record or not is user responsibility
        self.mapper.revert()
        event.accept()

