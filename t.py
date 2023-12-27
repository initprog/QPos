import os
import sys
import re
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelation, QSqlRelationalTableModel, QSqlRelationalDelegate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QWidget, QVBoxLayout, QLineEdit

basedir = os.path.dirname(__file__)
db = QSqlDatabase("QSQLITE")
db.setDatabaseName(os.path.join(basedir, "chinook.sqlite"))
db.open()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        container = QWidget()
        layout = QVBoxLayout()
        self.search = QLineEdit()
        self.search.textChanged.connect(self.update_filter)
        
        self.table = QTableView()

        layout.addWidget(self.search)
        layout.addWidget(self.table)
        container.setLayout(layout)

        #self.model = QSqlTableModel(db=db)
        self.model = QSqlRelationalTableModel(db=db)

        self.table.setModel(self.model)
        self.model.setTable("Track")

        # using QSqlRelationalTableModel
        # params: related-table, related-table-FK, column-to-display
        # These fields become read-only
        self.model.setRelation(2, QSqlRelation("Album", "AlbumId", "Title"))
        self.model.setRelation(3, QSqlRelation("MediaType", "MediaTypeId", "Name"))
        self.model.setRelation(4, QSqlRelation("Genre", "GenreId", "Name"))

        # add combobox, able to change value (need to change focus to other field to make the change recorded)
        delegate = QSqlRelationalDelegate(self.table)
        self.table.setItemDelegate(delegate)

        column_titles = {
            "TrackId": "Track (ID)",
            "Name": "Name",
            "AlbumId": "Album (ID)",
            "MediaTypeId": "Media Type (ID)",
            "GenreId": "Genre (ID)",
            "Composer": "Composer",
            "Milliseconds": "Milliseconds",
            "Bytes": "Bytes",
            "UnitPrice": "Unit Price",
        }
        for n, t in column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Orientation.Horizontal, t)
        self.model.select()
        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(container)

    def update_filter(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'Name LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()