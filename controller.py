# To Run this project run this file

from PyQt5 import QtWidgets, QtGui, QtCore

import main
import register
import login

import random
from data_controller import login_authen, register_process, get_user_detail


def message_box(title, text_message):
    message = QtWidgets.QMessageBox()
    message.setIcon(QtWidgets.QMessageBox.Information)
    message.setText(text_message)
    message.setWindowTitle(title)
    message.exec_()


class LoginPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login_click)
        self.ui.register_button.clicked.connect(self.register_click)
        self.user = ""
        self.main_window = MainPage()
        self.register_window = RegisterPage()
        self.ui.pass_edit.returnPressed.connect(self.login_click)

    def login_click(self):
        if login_authen(self):
            self.hide()
            self.main_window.show()
            rest_name = get_user_detail(self.user)
            self.main_window.ui.tableName.setText(rest_name)
            print("LOGIN = {}".format(rest_name))
            self.ui.user_edit.clear()
            self.ui.pass_edit.clear()
        else:
            message_box("Login", "Username or password incorrect please try again")

    def register_click(self):
        self.register_window.show()


class MainPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings(self)
        self.ui.actionSignout.triggered.connect(self.sign_out)
        self.ui.actionQuit.triggered.connect(self.exit_app)
        self.table_manage()

    def sign_out(self):
        self.hide()
        myApp.show()

    def table_manage(self):
        table_header = ["ชื่อโต๊ะ", "จำนวนคน", "เวลาเข้า", "เวลาที่เหลือ", "ราคามื้อนี้"]
        self.model = QtGui.QStandardItemModel()
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
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def selected_item_tableview(self, index):
        row = index.row()
        for q, i in enumerate(self.values[row]):
            if q == 0:
                table_name = "{}".format(i)
                self.ui.table_no.setText(table_name)
            elif q == 1:
                person_text = "จำนวนคน : {}".format(i)
                self.ui.person.setText(person_text)

    def exit_app(self):
        QtWidgets.qApp.exit()


class RegisterPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RegisterPage, self).__init__(parent)
        self.ui = register.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.error_label.hide()
        self.ui.register_button.clicked.connect(self.register_click)

    def register_click(self):
        restaurant_name = self.ui.rest_edit.text()
        username = self.ui.user_edit.text()
        password = self.ui.pass_edit.text()
        password_confirm = self.ui.pass_con_edit.text()
        if restaurant_name != "" and username != "" and password != "" and password_confirm != "" and password == password_confirm:
            register_process(self)
        else:
            self.ui.error_label.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myApp = LoginPage()
    myApp.show()
    sys.exit(app.exec_())