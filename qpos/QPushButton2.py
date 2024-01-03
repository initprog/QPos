import os
from PyQt6 import QtWidgets, QtCore, QtGui

class QPushButton2(QtWidgets.QPushButton):
  def __init__(self, text, parent=None):
    super(QPushButton2, self).__init__(text, parent)
    self.parent = parent
    #self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground) # allow setStylesheet -- not required?

  def setPixmap(self, icon_left, icon_right=None, width=16, height=16):
    style = 'text-align: left;'
    style += f'padding-left: {width + 10}'
    self.setStyleSheet(style)
    self.pixmap_left = QtGui.QPixmap(icon_left).scaled(width, height, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
    if icon_right is None:
      self.pixmap_right = None
    else:
      self.pixmap_right = QtGui.QPixmap(icon_right).scaled(width, height, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
    
  def sizeHint(self):
    #parent_size = QtWidgets.QPushButton.sizeHint(self)
    extra_width = 10
    pixmap_right_width = 0
    parent_size = QtWidgets.QPushButton.sizeHint(self);
    if self.pixmap_right is not None: 
      pixmap_right_width = self.pixmap_right.width()
    print(f"width parent: {self.parent.width()} pixmap: {self.pixmap_left.width()}")
    return QtCore.QSize(self.parent.width() + self.pixmap_left.width() + pixmap_right_width + extra_width, max(parent_size.height(), self.pixmap_left.height()))

  def paintEvent(self, event):
    '''
    Overwriting paintEvent
    '''
    QtWidgets.QPushButton.paintEvent(self, event)
    r = event.rect()
    pos_x = 5  # hardcoded horizontal margin
    pos_y = int((self.height() - self.pixmap_left.height()) / 2)

    painter = QtGui.QPainter(self)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
    painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform, True)
    painter.drawPixmap(pos_x, pos_y, self.pixmap_left)
    if self.pixmap_right is not None:
      painter.drawPixmap(pos_x + self.pixmap_right.width() + self.parent.width(), pos_y, self.pixmap_right)


class TestUI(QtWidgets.QWidget):
  def __init__(self, parent=None):
      super(TestUI, self).__init__(parent)

      # initialization object
      layout = QtWidgets.QGridLayout()
      
      path = os.path.join(os.path.dirname(__file__), f"asset{os.sep}icon")
      icon1 = f"{path}{os.sep}cog-48w.png"
      icon2 = f"{path}{os.sep}rchevron.svg"

      pb = QPushButton2('test', self)
      pb2 = QPushButton2('Reporting and Tools', self)
      pb3 = QPushButton2('Customer', self)
      
      
      pb.setPixmap(icon1, icon2)
      pb2.setPixmap(icon1, icon2)
      pb3.setPixmap(icon1, icon2)

      layout.addWidget(pb)
      layout.addWidget(pb2)
      layout.addWidget(pb3)
      self.setLayout(layout)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = TestUI()
    window.show()

    sys.exit(app.exec())