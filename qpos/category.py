from PyQt6.QtWidgets import QWidget

from qpos.view.entity_ui import Ui_Form


class ItemCategory(QWidget):
    def __init__(self):
        super(ItemCategory, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lblHeader.setText("Item Category")
        self.ui.btnAdd.setText("Add Categroy")
        
