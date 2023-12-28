import os
from PyQt6.QtWidgets import QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelation, QSqlRelationalTableModel, QSqlRelationalDelegate
from qpos.db import DEFAULT_DB
from qpos.view.item_ui import Ui_Form

db = QSqlDatabase("QSQLITE")
db.setDatabaseName(DEFAULT_DB)
db.open()

class Item(QWidget):
    def __init__(self):
        super(Item, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = QSqlRelationalTableModel(db=db)
        self.model.setTable("Item")
        self.ui.tvItem.setModel(self.model)

        self.model_variation = QSqlRelationalTableModel(db=db)
        self.model_variation.setTable("ItemVariation")
        self.ui.tvVariation.setModel(self.model_variation)

        self.model.select()
        self.model_variation.select()
