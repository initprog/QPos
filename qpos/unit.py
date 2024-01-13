from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget
from PyQt6.QtSql import QSqlQuery, QSqlTableModel, QSqlRelation, QSqlRelationalTableModel, QSqlRelationalDelegate
from qpos.db import Qdb
from qpos.view.unit_ui import Ui_Form as Unit_Form
from qpos.view.entity_ui import Ui_Form as Entity_Form

class Unit(QWidget):
    def __init__(self):
        super(Unit, self).__init__()
        self.ui = Entity_Form()
        self.ui.setupUi(self)

        self.db = Qdb()
        query = QSqlQuery('SELECT COUNT(id) FROM unit', self.db)
        if query.next() and int(query.value(0)) == 0:
            
            self.ui.lblEntity.setText('Your units')
            txt = 'Units are used to specify how you want to measure your items.'
            self.ui.lblDescription.setText(txt)
            self.ui.btnCreate.setText('Create a unit')
            self.ui.lblIcon.setPixmap(QtGui.QPixmap(":/icon/icon/items-128.png"))
            return

        self.ui.lblHeader.setText('Your Units')
        self.ui.btnAdd.setText('Add a Unit')
        self.ui.stackedWidget.setCurrentWidget(self.ui.pgList)
        
        self.model = QSqlRelationalTableModel(db=self.db)
        self.model.setTable("Unit")
        self.ui.tvTable.setModel(self.model)

        self.model.select()
