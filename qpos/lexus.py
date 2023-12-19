from PyQt6.QtWidgets import QWidget

from qpos.view.lexus_ui import Ui_Form


class Lexus(QWidget):
    def __init__(self):
        super(Lexus, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
