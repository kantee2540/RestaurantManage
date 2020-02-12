# To Run this project run this file

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pymongo

import main
import register
import login

import random
import hashlib


def get_database_client():
    return pymongo.MongoClient("mongodb+srv://kantee2540:K%61n%742540@cluster0-ww6d1.mongodb.net/test?retryWrites=true&w=majority")


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
        self.main_window = MainPage()
        self.register_window = RegisterPage()

    def login_click(self):

        #self.main_window.show()
        self.login_authen()

    def login_authen(self):
        try:
            client = get_database_client()
            db = client.get_database("Restaurant")

            username = self.ui.user_edit.text()
            password = hashlib.md5(self.ui.pass_edit.text().encode()).hexdigest()
            login_user = db.User.find_one({"username": username})
            if login_user:
                if password == login_user["password"]:
                    self.hide()
                    self.main_window.show()
                else:
                    message_box("Login", "Username or password incorrect please try again")

            else:
                message_box("Login", "Username or password incorrect please try again")

        except Exception as e:
            print("Error = {}".format(e))

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
            self.register_process()
        else:
            self.ui.error_label.show()

    def register_process(self):
        try:
            client = get_database_client()
            db = client.get_database("Restaurant")

            restaurant_name = self.ui.rest_edit.text()
            username = self.ui.user_edit.text()
            password = self.ui.pass_edit.text()
            password_encrypt = hashlib.md5(password.encode()).hexdigest()

            data = {"restaurant_name": restaurant_name, "username": username, "password": password_encrypt}
            rs = db.User.insert_one(data)
            if rs:
                message_box("Register", "Register successful!\n Your restaurant name : {}".format(username))
                self.clear_lineedit()
                self.close()

        except Exception as e:
            message_box("Error", "Error message : \"{}\"Please Contact ch.kantee_st@tni.ac.th".format(e))

    def clear_lineedit(self):
        self.ui.rest_edit.clear()
        self.ui.user_edit.clear()
        self.ui.pass_edit.clear()
        self.ui.pass_con_edit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myApp = LoginPage()
    myApp.show()
    sys.exit(app.exec_())