from PyQt6.QtWidgets import QWidget

from qpos.view.toyota_ui import Ui_Form


class Toyota(QWidget):
    def __init__(self):
        super(Toyota, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
