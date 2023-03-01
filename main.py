import sqlite3
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee_db.db')
        db.open()

        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('menu')
        model.select()

        view.setModel(model)
        view.move(10, 10)
        view.resize(800, 180)

        self.setGeometry(300, 100, 800, 200)
        self.setWindowTitle('Coffee Shop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
