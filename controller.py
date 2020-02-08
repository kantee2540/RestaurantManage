# To Run this project run this file

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import main
import register
import login
import random


class LoginPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login_click)
        self.ui.register_button.clicked.connect(self.register_click)
        self.main_window = MainPage()
        self.register_window = RegisterPage()

    def login_click(self):
        self.main_window.show()
        self.hide()

    def register_click(self):
        self.register_window.show()


class MainPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionSignout.triggered.connect(self.sign_out)
        self.ui.actionQuit.triggered.connect(self.exit_app)
        self.table_manage()

    def sign_out(self):
        self.hide()
        myApp.show()

    def table_manage(self):
        table_header = ["ชื่อโต๊ะ", "จำนวนคน", "เวลาเข้า", "เวลาที่เหลือ", "ราคามื้อนี้"]
        self.model = QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(table_header)
        self.ui.tableView.setColumnWidth(0, 160)
        self.ui.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.tableView.clicked.connect(self.selected_item_tableview)
        self.values = []
        self.abc = ["A", 0, "B", "C", "D"]
        row = 10
        column = 5
        for i in range(row):
            sub_values = []
            self.abc[1] = i
            self.abc[0] = "A{}".format(random.randint(0, 50))
            for j in self.abc:
                sub_values.append(j)
            self.values.append(sub_values)

        for value in self.values:
            row = []
            for item in value:
                cell = QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def selected_item_tableview(self, index):
        row = index.row()
        for q, i in enumerate(self.values[row]):
            if q == 0:
                table_name = "{}".format(i)
                self.ui.table_no.setText(table_name)

    def exit_app(self):
        QtWidgets.qApp.exit()


class RegisterPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RegisterPage, self).__init__(parent)
        self.ui = register.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myApp = LoginPage()
    myApp.show()
    sys.exit(app.exec_())