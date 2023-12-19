from PyQt6.QtWidgets import QWidget

from qpos.view.mazda_ui import Ui_Form


class Mazda(QWidget):
    def __init__(self):
        super(Mazda, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
