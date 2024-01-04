import os
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QEvent, QObject, Qt
from PyQt6.QtGui import QResizeEvent

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
    parent_size = QtWidgets.QPushButton.sizeHint(self)
    if self.pixmap_right is not None: 
      pixmap_right_width = self.pixmap_right.width()
    print(f"width parent: {parent_size.width()} pixmap: {self.pixmap_left.width()}")
    return QtCore.QSize(parent_size.width() + self.pixmap_left.width() + pixmap_right_width + extra_width, max(parent_size.height(), self.pixmap_left.height()))

  def paintEvent(self, event):
    '''
    Overwriting paintEvent
    '''
    QtWidgets.QPushButton.paintEvent(self, event)
    #r = event.rect()
    pos_x = 5  # hardcoded horizontal margin
    pos_y = int((self.height() - self.pixmap_left.height()) / 2)

    painter = QtGui.QPainter(self)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
    painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform, True)
    painter.drawPixmap(pos_x, pos_y, self.pixmap_left)
    if self.pixmap_right is not None:
      parent_size = QtWidgets.QPushButton.sizeHint(self)
      painter.drawPixmap(pos_x + self.pixmap_right.width() + parent_size.width(), pos_y, self.pixmap_right)
  

class PushButton(QtWidgets.QPushButton):
  def __init__(self, *args, **kwargs):
    super(PushButton, self).__init__(*args, **kwargs)
    #self.setStyleSheet('''background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fdfbf7, stop: 1 #6190F2);
    #    border-style: solid;border-width: 2px;
    #    border-radius: 8px;
    #    border-color: #9BB7F0;padding: 3px;''')

    icon = self.icon()
    icon_size = self.iconSize()
    # remove icon
    self.setIcon(QtGui.QIcon())

    icon2 = QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowLeft)
    label_icon = QtWidgets.QLabel()
    label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    label_icon_left = QtWidgets.QLabel()
    label_icon_left.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    label_icon_left.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    lay = QtWidgets.QHBoxLayout(self)
    lay.setContentsMargins(0, 0, 0, 0)
    lay.addWidget(label_icon_left, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
    lay.addWidget(label_icon, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
    label_icon.setPixmap(icon.pixmap(icon_size))
    label_icon_left.setPixmap(icon2.pixmap(icon_size))

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

      self.pb = QPushButton2('test', self)
      pbo = PushButton('Test Button', icon=iconx, iconSize=QtCore.QSize(16,16))
      #pb2 = QPushButton2('Reporting and Tools', self)
      #pb3 = QPushButton2('Customer', self)
      
      
      self.pb.setPixmap(icon1, icon2)
      #pb2.setPixmap(icon1, icon2)
      #pb3.setPixmap(icon1, icon2)

      layout.addWidget(self.pb)
      layout.addWidget(pbo)
      #layout.addWidget(pb2)
      #layout.addWidget(pb3)
      self.setLayout(layout)

  def eventFilter(self, a0: QObject | None, a1: QEvent | None) -> bool:
    if a1.type() == QtCore.QEvent.Type.Paint:
      if a0 == self.pb:
          print(f'++++++++++++ {self.pb.width()}')
          self.pb.paintEvent(self)
      return True
    return super().eventFilter(a0, a1)
  
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = TestUI()
    window.show()

    sys.exit(app.exec())