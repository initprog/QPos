from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget
from PyQt6.QtSql import QSqlQuery, QSqlTableModel, QSqlRelation, QSqlRelationalTableModel, QSqlRelationalDelegate
from qpos.db import Qdb
from qpos.view.item_ui import Ui_Form as Item_Form
from qpos.view.entity_ui import Ui_Form as Entity_Form

class Item(QWidget):
    def __init__(self):
        super(Item, self).__init__()
        
        self.db = Qdb()
        query = QSqlQuery('SELECT COUNT(id) FROM item', self.db)
        if query.next() and int(query.value(0)) == 0:
            self.ui = Entity_Form()
            self.ui.setupUi(self)
            self.ui.lblEntity.setText('Your item library')
            txt = 'Organize what you sell with the item library.'\
                ' Create items to help speed-up checkout, view sales reports and track inventory.'\
                ' Download our template to create and update items with import.'
            self.ui.lblDescription.setText(txt)
            self.ui.btnCreate.setText('Create an item')
            self.ui.lblIcon.setPixmap(QtGui.QPixmap(":/icon/icon/items-128.png"))
            return

        self.ui = Item_Form()
        self.ui.setupUi(self)
        self.model = QSqlRelationalTableModel(db=self.db)
        self.model.setTable("Item")
        self.ui.tvItem.setModel(self.model)

        self.model_variation = QSqlRelationalTableModel(db=self.db)
        self.model_variation.setTable("ItemVariation")
        self.ui.tvVariation.setModel(self.model_variation)

        self.model.select()
        self.model_variation.select()
