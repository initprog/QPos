# https://gist.github.com/Riateche/5984815
#import sip
#sip.setapi('QString', 2)
#sip.setapi('QVariant', 2)


from PyQt6 import QtCore, QtGui, QtWidgets

class TableModel(QtCore.QAbstractTableModel):
    """
    A simple 5x4 table model to demonstrate the delegates
    """
    def rowCount(self, parent=QtCore.QModelIndex()): return 5
    def columnCount(self, parent=QtCore.QModelIndex()): return 4

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if not index.isValid(): return None
        if not role==QtCore.Qt.ItemDataRole.DisplayRole: return None
        return "{0:02d}".format(index.row())
        
    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.DisplayRole):
        print ("setData", index.row(), index.column(), value)

    def flags(self, index):
        if (index.column() == 0):
            return QtCore.Qt.ItemFlag.ItemIsEditable | QtCore.Qt.ItemFlag.ItemIsEnabled
        else:
            return QtCore.Qt.ItemFlag.ItemIsEnabled

class ButtonDelegate(QtWidgets.QItemDelegate):

    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        combo = QtWidgets.QPushButton(str(index.data()), parent)

        #self.connect(combo, QtCore.SIGNAL("currentIndexChanged(int)"), self, QtCore.SLOT("currentIndexChanged()"))
        combo.clicked.connect(self.currentIndexChanged)
        return combo
        
    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        #editor.setCurrentIndex(int(index.model().data(index)))
        editor.blockSignals(False)
        
    def setModelData(self, editor, model, index):
        model.setData(index, editor.text())
        
    @QtCore.pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

class ComboDelegate(QtWidgets.QItemDelegate):
    """
    A delegate that places a fully functioning QComboBox in every
    cell of the column to which it's applied
    """
    def __init__(self, parent):

        QtWidgets.QItemDelegate.__init__(self, parent)
        
    def createEditor(self, parent, option, index):
        combo = QtWidgets.QComboBox(parent)
        li = []
        li.append("Zero")
        li.append("One")
        li.append("Two")
        li.append("Three")
        li.append("Four")
        li.append("Five")
        combo.addItems(li)
        #???self.connect(combo, QtCore.PYQT_SIGNAL("currentIndexChanged(int)"), self, QtCore.PYQT_SLOT("currentIndexChanged()"))
        return combo
        
    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.setCurrentIndex(int(index.model().data(index)))
        editor.blockSignals(False)
        
    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentIndex())
        
    @QtCore.pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

class TableView(QtWidgets.QTableView):
    """
    A simple table to demonstrate the QComboBox delegate.
    """
    def __init__(self, *args, **kwargs):
        QtWidgets.QTableView.__init__(self, *args, **kwargs)

        # Set the delegate for column 0 of our table
        # self.setItemDelegateForColumn(0, ButtonDelegate(self))
        self.setItemDelegateForColumn(0, ComboDelegate(self))
        self.setItemDelegateForColumn(1, ButtonDelegate(self))

    
if __name__=="__main__":
    from sys import argv, exit

    class Widget(QtWidgets.QWidget):
        """
        A simple test widget to contain and own the model and table.
        """
        def __init__(self, parent=None):
            QtWidgets.QWidget.__init__(self, parent)

            l=QtWidgets.QVBoxLayout(self)
            self._tm=TableModel(self)
            self._tv=TableView(self)
            #self._tv.setGridStyle(QtCore.Qt.NoPen)
            self._tv.setShowGrid(False)
            self._tv.setAlternatingRowColors(True)
            self._tv.setModel(self._tm)
            for row in range(0, self._tm.rowCount()):
                self._tv.openPersistentEditor(self._tm.index(row, 0))
                self._tv.openPersistentEditor(self._tm.index(row, 1))
            
            l.addWidget(self._tv)

    a=QtWidgets.QApplication(argv)
    w=Widget()
    w.move(0, 0)
    w.resize(800, 600)    
    w.show()
    w.raise_()
    exit(a.exec())