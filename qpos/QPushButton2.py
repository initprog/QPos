import os
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QEvent, QObject

class PushButton(QtWidgets.QPushButton):
  """
  Create a push button with two icons on the left and right of the text.
  Parameters:
    (str): Button text
    iconLeft (str): path to icon file for the left icon
    iconRight (str): path to icon file for the right icon
    iconSize (QSize): size of the icons
  """
  def __init__(self, *args, **kwargs):
    isize = kwargs['iconSize']
    pixLeft = QtGui.QPixmap(kwargs['iconLeft']).scaled(isize)
    pixRight = QtGui.QPixmap(kwargs['iconRight']).scaled(isize)
    kwargs.pop('iconLeft')
    kwargs.pop('iconRight')
    super(PushButton, self).__init__(*args, **kwargs)

    hSpacer = QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)

    label_left = QtWidgets.QLabel()
    label_left.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    label_left.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
    label_left.setPixmap(pixLeft)

    label_right = QtWidgets.QLabel()
    label_right.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    label_right.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
    label_right.setPixmap(pixRight)

    lay = QtWidgets.QHBoxLayout(self)
    lay.setContentsMargins(0, 0, 0, 0)

    # -- Problem with left icon and button text spacing
    #lay.addWidget(label_left, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
    
    # to correct left icon spacing with button text
    icon = QtGui.QIcon()
    icon.addPixmap(pixLeft)
    self.setIcon(icon)

    lay.addWidget(label_right, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
    self.setStyleSheet('text-align: left;padding-right:20px')

class TestUI(QtWidgets.QWidget):
  def __init__(self, parent=None):
      super(TestUI, self).__init__(parent)

      # initialization object
      layout = QtWidgets.QGridLayout()
      self.installEventFilter(self)

      path = os.path.join(os.path.dirname(__file__), f"asset{os.sep}icon")
      icon1 = f"{path}{os.sep}cog-48w.png"
      icon2 = f"{path}{os.sep}rchevron.svg"
      iconx = QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowRight)

      pbo = PushButton('Test button', iconLeft=icon1, iconRight=icon2, iconSize=QtCore.QSize(16,16))
      pbo2 = PushButton('More settings', iconLeft=icon1, iconRight=icon2, iconSize=QtCore.QSize(16,16))
      pbo3 = PushButton('Document comments', iconLeft=icon1, iconRight=icon2, iconSize=QtCore.QSize(16,16))
      
      layout.addWidget(pbo)
      layout.addWidget(pbo2)
      layout.addWidget(pbo3)
      
      self.setLayout(layout)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = TestUI()
    window.show()

    sys.exit(app.exec())