from PyQt6.QtWidgets import QWidget

from qpos.view.youtube_ui import Ui_Form


class Youtube(QWidget):
    def __init__(self):
        super(Youtube, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
