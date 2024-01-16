import os
import sys
from PyQt6 import QtGui, QtCore, QtWidgets

class ViewWidget(QtWidgets.QWidget):
    def __init__(self, x, index, parent=None):
        super(ViewWidget, self).__init__(parent)
        self.p_index = QtCore.QPersistentModelIndex(index)
        self.content_button = QtWidgets.QWidget(self)
        lay = QtWidgets.QHBoxLayout(self.content_button)
        lay.setContentsMargins(0, 0, 0, 0)
        
        self.share_btn = QtWidgets.QPushButton("share")
        self.share_btn.clicked.connect(self.share_clicked)
        del_icon = QtGui.QIcon("asset\\icon\\trash-16.png")
        self.delete_btn = QtWidgets.QPushButton(del_icon, '')
        self.delete_btn.clicked.connect(self.delete_clicked)

        lay.addWidget(self.share_btn)
        lay.addWidget(self.delete_btn)
        lay.setAlignment(self.delete_btn, QtCore.Qt.AlignmentFlag.AlignVCenter) # no effect
        self.content_button.move(x, 0)

    @QtCore.pyqtSlot()
    def delete_clicked(self):
        model = self.p_index.model()
        model.removeRow(self.p_index.row())

    @QtCore.pyqtSlot()
    def share_clicked(self):
        text = self.p_index.data()
        full_path = self.p_index.data(QtCore.Qt.ItemDataRole.UserRole + 1)
        print(text, full_path)


class ButtonsDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        self.parent().openPersistentEditor(index)
        super(ButtonsDelegate, self).paint(painter, option, index)

    def createEditor(self, parent, option, index):
        return ViewWidget(500, index, parent)

class Example(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        dirPath  = "c:\\dev\\ws-py\\galaga"

        self.setCentralWidget(QtWidgets.QWidget())
        layout = QtWidgets.QGridLayout(self.centralWidget())

        self.model  =QtGui.QStandardItemModel(self)
        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.clicked.connect(self.onClick)
        self.tableView.verticalHeader().hide()
        self.appendRowItems(dirPath)

        delegate = ButtonsDelegate(self.tableView)
        self.tableView.setItemDelegate(delegate)

        layout.addWidget(self.tableView)
        self.resize(800,500)

    def appendRowItems(self, dir_path):
        for root, dirs, files in os.walk(dir_path):
            if root == dir_path:
                for file in files:
                    item = QtGui.QStandardItem(file)
                    item.setData(os.path.join(root, file))
                    self.model.appendRow(item)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def onClick(self, ix):
        it = self.model.itemFromIndex(ix)
        print(it.data())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    eg =  Example()
    eg.show()
    sys.exit(app.exec())