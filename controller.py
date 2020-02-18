# To Run this project run this file

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

import main
import register
import login
import addmenu

import random
import data_controller


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
        self.setting = QtCore.QSettings('config', 'restaurant')
        self.main_window = MainPage()
        self.register_window = RegisterPage()
        self.ui.pass_edit.returnPressed.connect(self.login_click)

    def login_click(self):
        if data_controller.login_authen(self):
            self.hide()
            self.main_window.show()
            self.main_window.ui.tableName.setText(self.setting.value('rest_name'))
            print("LOGIN = {}".format(self.setting.value('rest_name')))
            self.ui.user_edit.clear()
            self.ui.pass_edit.clear()
        else:
            message_box("Login", "บัญชีผู้ใช้ หรือรหัสผ่านผิด โปรดลองอีกครั้ง\nถ้าหากไม่สำเร็จกรุณาสมัครใหม่หรือติดต่อผู้ดูแลแอพพลิเคชั่นนี้")

    def register_click(self):
        self.register_window.show()


class MainPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.addmenu = AddMenuPage()
        self.settings = QtCore.QSettings(self)
        self.ui.actionSignout.triggered.connect(self.sign_out)
        self.ui.actionQuit.triggered.connect(self.exit_app)
        self.ui.add_table_button.clicked.connect(self.click_add_menu)
        self.table_manage()

    def click_add_menu(self):
        self.addmenu.setWindowModality(QtCore.Qt.ApplicationModal)
        self.addmenu.show()

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


class AddMenuPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AddMenuPage, self).__init__(parent)
        self.ui = addmenu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setting = QtCore.QSettings('config', 'restaurant')
        self.ui.add_table_button.clicked.connect(self.add_table)

    def add_table(self):
        table_name = self.ui.table_name_lineedit.text()
        person = self.ui.person_spinBox.text()
        restaurant = self.setting.value("rest_name")
        if data_controller.add_table(table_name, person, restaurant):
            self.hide()
        else:
            message_box("Error", "Cannot Insert your information to database")


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
        if restaurant_name != "" and username != "" and password != "" \
                and password_confirm != "" and password == password_confirm:
            data_controller.register_process(self)
        else:
            self.ui.error_label.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myApp = LoginPage()
    myApp.show()
    sys.exit(app.exec_())
