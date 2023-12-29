from PyQt6.QtWidgets import QWidget

from qpos.view.more_ui import Ui_Form


class More(QWidget):
    def __init__(self):
        super(More, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
