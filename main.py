import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QMainWindow, QPushButton


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee_db.db')
        db.open()

        self.view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('menu')
        model.select()

        self.view.setModel(model)
        self.view.move(10, 10)
        self.view.resize(800, 180)

        self.btn = QPushButton("Изменить меню", self)
        self.btn.resize(100, 30)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.open_edittor)

        self.setGeometry(300, 100, 820, 250)
        self.setWindowTitle('Coffee Shop')
    
    def open_edittor(self):
        global ex2
        ex2 = EditMenu()
        ex2.show()


class EditMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.initUI()
        self.pushButton.clicked.connect(self.add)
    
    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee_db.db')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('menu')
        model.select()

        self.tableView.setModel(model)

        self.setWindowTitle('Edit/Add Coffee')
    
    def add(self):
        name = self.lineEdit_5.text()
        roasting_degree = self.lineEdit_2.text()
        grounded = self.lineEdit_3.text()
        taste_info = self.lineEdit_4.text()
        price = self.lineEdit_6.text()
        packing_volume = self.lineEdit.text()

        if '' not in [name, roasting_degree, grounded, taste_info] and price.isdigit():
            con = sqlite3.connect("coffee_db.db")
            cur = con.cursor()
            cur.execute("""INSERT INTO menu(name, roasting_degree, grounded, taste_info, price, packing_volume) VALUES (?, ?, ?, ?, ?, ?)""", 
                        (name, roasting_degree, grounded, taste_info, price, packing_volume, )).fetchall()
            con.commit()
            con.close()

            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('coffee_db.db')
            db.open()

            model = QSqlTableModel(self, db)
            model.setTable('menu')
            model.select()

            self.tableView.setModel(model)
            ex.view.setModel(model)

            self.label.setText("Добавить данные")

        else:
            self.label.setText('Что-то не так, попробуйте еще раз!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
