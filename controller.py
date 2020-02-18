# To Run this project run this file

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

import main
import register
import login
import addmenu

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
        self.ui.pass_edit.returnPressed.connect(self.login_click)

    def login_click(self):
        if data_controller.login_authen(self):
            self.hide()
            main_page.show()
            main_page.table_manage()
            main_page.ui.tableName.setText(self.setting.value('rest_name'))

            self.ui.user_edit.clear()
            self.ui.pass_edit.clear()
        else:
            message_box("Login", "บัญชีผู้ใช้ หรือรหัสผ่านผิด โปรดลองอีกครั้ง\nถ้าหากไม่สำเร็จกรุณาสมัครใหม่หรือติดต่อผู้ดูแลแอพพลิเคชั่นนี้")

    def register_click(self):
        register_page.show()


class MainPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = QtCore.QSettings('config', 'restaurant')

        self.ui.actionSignout.triggered.connect(self.sign_out)
        self.ui.actionQuit.triggered.connect(self.exit_app)
        self.ui.addmenu_action.triggered.connect(self.click_add_menu)
        self.ui.refresh_action.triggered.connect(self.table_manage)

        self.ui.add_table_button.clicked.connect(self.click_add_menu)

    def click_add_menu(self):
        addmenu_page.setWindowModality(QtCore.Qt.ApplicationModal)
        addmenu_page.show()

    def sign_out(self):
        self.hide()
        login_page.show()

    def table_manage(self):
        table_header = ["ชื่อโต๊ะ", "จำนวนคน", "เวลาเข้า", "เวลาที่เหลือ", "ราคามื้อนี้"]
        self.model = QtGui.QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(table_header)
        self.ui.tableView.setColumnWidth(0, 160)
        self.ui.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.ui.tableView.clicked.connect(self.selected_item_tableview)

        self.values = data_controller.get_table_data(self.settings.value('rest_name'))
        self.row_value = []

        for i in self.values:
            sub_value = [i["table_name"], i["person"], i["restaurant_name"]]
            self.row_value.append(sub_value)

        for value in self.row_value:
            row = []
            for item in value:
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def selected_item_tableview(self, index):
        row = index.row()
        for q, i in enumerate(self.row_value[row]):
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
            main_page.table_manage()
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
    # initialize
    login_page = LoginPage()
    main_page = MainPage()
    register_page = RegisterPage()
    addmenu_page = AddMenuPage()

    login_page.show()
    sys.exit(app.exec_())
