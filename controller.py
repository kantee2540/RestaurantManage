# To Run this project run this file

import sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport

import main
import register
import login
import addtable
import menu
import addmenu
import editmenu
import edit_rest_info
import history
import check_bill
import done_bill
import result

import data_controller


def message_box(title, text_message):
    message = QtWidgets.QMessageBox()
    message.setIcon(QtWidgets.QMessageBox.Information)
    message.setText(text_message)
    message.setWindowTitle(title)
    message.exec_()


def yes_no_message_box(self, title, text_message):
    message = QtWidgets.QMessageBox.question(self, title, text_message,
                                             QtWidgets.QMessageBox.Yes,
                                             QtWidgets.QMessageBox.No)
    if message == QtWidgets.QMessageBox.Yes:
        return True
    else:
        return False


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
        if data_controller.login_authen(self) and (self.ui.user_edit != "" and self.ui.pass_edit != ""):
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
        self.ui.addmenu_action.triggered.connect(self.click_add_table)
        self.ui.refresh_action.triggered.connect(self.table_manage)
        self.ui.actionMenu.triggered.connect(self.click_menu)
        self.ui.actionAdd_Menu.triggered.connect(self.click_add_menu)
        self.ui.actionEditRest.triggered.connect(self.click_edit_rest)
        self.ui.cancelmenu_action.triggered.connect(self.click_cancel_order)
        self.ui.actionCal.triggered.connect(self.click_check_bill)
        self.ui.actionHistory.triggered.connect(self.click_history)
        self.ui.actionResult.triggered.connect(self.click_see_result)

        self.ui.add_table_button.clicked.connect(self.click_add_table)
        self.ui.cancel_button.clicked.connect(self.click_cancel_order)
        self.ui.check_bill.clicked.connect(self.click_check_bill)

        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.rightClickEvent)

    def click_add_table(self):
        add_table_page.setWindowModality(QtCore.Qt.ApplicationModal)
        add_table_page.show()
        add_table_page.table_manage()

    def click_menu(self):
        menu_page.setWindowModality(QtCore.Qt.ApplicationModal)
        menu_page.show()
        menu_page.table_manage()

    def click_add_menu(self):
        add_menu_page.setWindowModality(QtCore.Qt.ApplicationModal)
        add_menu_page.show()

    def click_edit_rest(self):
        edit_rest.setWindowModality(QtCore.Qt.ApplicationModal)
        edit_rest.show()
        edit_rest.set_rest_name()

    def click_cancel_order(self):
        index = self.ui.tableView.currentIndex().row()
        rest_name = self.settings.value('rest_name')
        table_name = self.row_value[index][0]
        if yes_no_message_box(self, "ยกเลิกรายการ", "คุณต้องการยกเลิกรายการหรือไม่"):
            if data_controller.cancel_table_order(rest_name, table_name):
                self.table_manage()

    def click_check_bill(self):
        index = self.ui.tableView.currentIndex().row()
        table_name = self.row_value[index][0]
        rest_name = self.settings.value('rest_name')
        check_bill_page.setWindowModality(QtCore.Qt.ApplicationModal)
        check_bill_page.show()
        check_bill_page.list_menu(table_name, rest_name)

    def click_history(self):
        history_page.setWindowModality(QtCore.Qt.ApplicationModal)
        history_page.show()
        history_page.table_manage()

    def click_see_result(self):
        result_page.setWindowModality(QtCore.Qt.ApplicationModal)
        result_page.show()
        result_page.display_result()

    def sign_out(self):
        self.hide()
        login_page.show()

    def rightClickEvent(self, event):
        menu = QtWidgets.QMenu(self)
        cancel_action = QtWidgets.QAction("รีเฟรช", self)
        menu.addAction(cancel_action)
        action = menu.exec_(self.ui.tableView.viewport().mapToGlobal(event))
        if action == cancel_action:
            self.table_manage()

    def table_manage(self):
        table_header = ["ชื่อโต๊ะ", "จำนวนคน", "เวลาเข้า", "ราคามื้อนี้"]
        self.model = QtGui.QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(table_header)
        self.ui.tableView.setColumnWidth(0, 160)
        self.ui.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.tableView.clicked.connect(self.selected_item_tableview)
        self.ui.cancel_button.setEnabled(False)
        self.ui.check_bill.setEnabled(False)
        self.ui.cancelmenu_action.setEnabled(False)
        self.ui.actionCal.setEnabled(False)
        self.values = data_controller.get_table_data(self.settings.value('rest_name'))
        self.row_value = []
        self.count_menu = []

        for i in self.values:
            all_quantity = 0
            for j in i["menu_set"]:
                all_quantity += j["quantity"]
            self.count_menu.append(int(all_quantity))

            sub_value = [i["table_name"], i["person"], i["in_time"], "{:,}".format(i["price"])]
            self.row_value.append(sub_value)

        for value in self.row_value:
            row = []
            for item in value:
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def selected_item_tableview(self, index):
        self.ui.cancel_button.setEnabled(True)
        self.ui.check_bill.setEnabled(True)
        self.ui.cancelmenu_action.setEnabled(True)
        self.ui.actionCal.setEnabled(True)

        row = index.row()
        for q, i in enumerate(self.row_value[row]):
            if q == 0:
                table_name = "{}".format(i)
                self.ui.table_no.setText(table_name)
            elif q == 1:
                person_text = "จำนวนคน : {}".format(i)
                self.ui.person.setText(person_text)
            elif q == 2:
                in_time = "เวลาที่เข้า : {}".format(i)
                self.ui.timein.setText(in_time)
            elif q == 3:
                total_txt = "ราคาอาหารมื้อนี้ : {}".format(i)
                self.ui.total_price.setText(total_txt)

        order_text = "จำนวนเมนูอาหาร : {}".format(self.count_menu[row])
        self.ui.order_num.setText(order_text)

    def exit_app(self):
        QtWidgets.qApp.exit()


class MenuDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MenuDialog, self).__init__(parent)
        self.ui = menu.Ui_Dialog()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings('config', 'restaurant')
        self.ui.add_menu_button.clicked.connect(self.click_add_menu)
        self.ui.remove_menu_button.clicked.connect(self.click_remove_menu)
        self.ui.edit_menu_button.clicked.connect(self.click_edit_menu)

    def table_manage(self):
        table_header = ["ชื่ออาหาร", "ประเภท", "ราคา"]
        self.model = QtGui.QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(table_header)
        self.ui.tableView.setColumnWidth(0, 200)
        self.ui.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.values = data_controller.get_menu_data(self.settings.value('rest_name'))
        self.row_value = []

        for i in self.values:
            sub_value = [i["menu_name"], i["category"], i["price"]]
            self.row_value.append(sub_value)

        for value in self.row_value:
            row = []
            for x, item in enumerate(value):
                if x == 2:
                    cell = QtGui.QStandardItem("{:,}".format(item))
                else:
                    cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def click_remove_menu(self):
        row = self.ui.tableView.currentIndex().row()
        remove_menu = self.row_value[row][0]
        txt = "คุณต้องการลบเมนูอาหาร {} หรือไม่".format(remove_menu)
        if yes_no_message_box(self, "ลบเมนูอาหาร", txt):
            self.remove_menu(remove_menu)

    def remove_menu(self, remove_menu):
        if data_controller.remove_menu(remove_menu):
            print("Menu : {} has removed".format(remove_menu))
            self.table_manage()
        else:
            print("Remove failed!")

    def click_add_menu(self):
        add_menu_page.setWindowModality(QtCore.Qt.ApplicationModal)
        add_menu_page.show()

    def click_edit_menu(self):
        row = self.ui.tableView.currentIndex().row()
        edit_menu = self.row_value[row][0]
        edit_type = self.row_value[row][1]
        edit_price = self.row_value[row][2]

        edit_menu_page.old_menu = edit_menu
        edit_menu_page.setWindowModality(QtCore.Qt.ApplicationModal)
        edit_menu_page.ui.menu_name_lineedit.setText(edit_menu)

        if edit_type == "บุฟเฟ่":
            edit_menu_page.ui.menu_type_comboBox.setCurrentIndex(1)
        elif edit_type == "เครื่องดื่ม":
            edit_menu_page.ui.menu_type_comboBox.setCurrentIndex(2)
        else:
            edit_menu_page.ui.menu_type_comboBox.setCurrentIndex(0)

        edit_menu_page.ui.price_spinbox.setValue(edit_price)
        edit_menu_page.show()


class AddMenuDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddMenuDialog, self).__init__(parent)
        self.ui = addmenu.Ui_Dialog()
        self.ui.setupUi(self)
        self.setting = QtCore.QSettings('config', 'restaurant')
        self.ui.ok_button.clicked.connect(self.click_add_menu)
        self.ui.cancel_button.clicked.connect(self.click_cancel)

    def click_cancel(self):
        self.hide()

    def click_add_menu(self):
        menu_name = self.ui.menu_name_lineedit.text()
        menu_category = self.ui.menu_type_comboBox.currentText()
        price = float(self.ui.price_spinbox.text())
        restaurant_name = self.setting.value('rest_name')
        if data_controller.add_menu(menu_name, price, menu_category, restaurant_name):
            self.hide()
            menu_page.table_manage()
            add_table_page.table_manage()
        else:
            message_box("Error", "Cannot Add menu")


class EditMenuDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditMenuDialog, self).__init__(parent)
        self.ui = editmenu.Ui_Dialog()
        self.ui.setupUi(self)
        self.old_menu = ""
        self.ui.ok_button.clicked.connect(self.click_update)
        self.ui.cancel_button.clicked.connect(self.click_cancel)

    def click_update(self):
        menu_name = self.ui.menu_name_lineedit.text()
        price = float(self.ui.price_spinbox.text())
        menu_category = self.ui.menu_type_comboBox.currentText()
        if data_controller.update_menu(self.old_menu, menu_name, price, menu_category):
            self.hide()
            menu_page.table_manage()
        else:
            message_box("Error", "Cannot Update menu")

    def click_cancel(self):
        self.hide()


class AddTablePage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AddTablePage, self).__init__(parent)
        self.ui = addtable.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setting = QtCore.QSettings('config', 'restaurant')
        self.ui.add_table_button.clicked.connect(self.add_table)
        self.ui.cancel_button.clicked.connect(self.click_cancel)
        self.ui.add_menu_button.clicked.connect(self.click_add_menu)
        self.ui.remove_button.clicked.connect(self.click_remove)
        self.ui.addmenu_link.clicked.connect(self.click_add_new_menu)

    def table_manage(self):
        table_header = ["ชื่ออาหาร", "ราคา"]
        result_table_header = ["ชื่ออาหาร", "จำนวน", "ราคา"]
        self.model = QtGui.QStandardItemModel(self)
        self.model_result = QtGui.QStandardItemModel(self)
        self.ui.menu_table.setModel(self.model)
        self.ui.result_table.setModel(self.model_result)
        self.model.setHorizontalHeaderLabels(table_header)
        self.model_result.setHorizontalHeaderLabels(result_table_header)
        self.ui.menu_table.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.menu_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.result_table.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.result_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.menu_table.setColumnWidth(0, 130)
        self.ui.remove_button.setEnabled(False)
        self.ui.result_table.clicked.connect(self.select_item_tableview)
        self.selected_menu = []

        self.values = data_controller.get_menu_data(self.setting.value('rest_name'))
        self.row_value = []
        self.total_price = 0
        self.set_text_totalprice()

        for i in self.values:
            sub_value = [i["menu_name"], i["price"]]
            self.row_value.append(sub_value)

        for value in self.row_value:
            row = []
            for x, item in enumerate(value):
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def click_add_menu(self):
        row = self.ui.menu_table.currentIndex().row()
        data = self.row_value[row]
        quantity = float(self.ui.quantity_spinBox.text())
        net_price = data[1] * quantity
        data_dict = {"menu_name": data[0], "quantity": quantity, "price": net_price}
        self.total_price += net_price
        self.set_text_totalprice()

        menu_item = QtGui.QStandardItem(str(data_dict["menu_name"]))
        quantity_item = QtGui.QStandardItem(str(data_dict["quantity"]))
        price_item = QtGui.QStandardItem("{:,}".format(data_dict["price"]))

        self.model_result.appendRow([menu_item, quantity_item, price_item])
        self.selected_menu.append(data_dict)

    def click_remove(self):
        index = self.ui.result_table.currentIndex().row()
        self.model_result.removeRow(index)
        self.total_price -= self.selected_menu[index]["price"]
        self.set_text_totalprice()
        self.selected_menu.pop(index)
        if len(self.selected_menu) <= 0:
            self.ui.remove_button.setEnabled(False)

    def set_text_totalprice(self):
        self.ui.total_price_text.setText("ราคารวมทั้งหมด : {:,}".format(self.total_price))
        self.ui.total_price_text.repaint()

    def select_item_tableview(self):
        self.ui.remove_button.setEnabled(True)

    def click_cancel(self):
        self.hide()

    def add_table(self):
        if self.ui.table_name_lineedit.text() != "":
            table_name = self.ui.table_name_lineedit.text()
            person = self.ui.person_spinBox.text()
            restaurant = self.setting.value("rest_name")
            menu_set = self.selected_menu
            if data_controller.add_table(table_name, person, menu_set, restaurant):
                self.hide()
                main_page.table_manage()
                self.ui.table_name_lineedit.clear()
                self.ui.person_spinBox.setValue(1)
            else:
                message_box("Error", "Cannot Insert your information to database")
        else:
            message_box("กรอกให้ครบ", "กรุณาใส่ชื่อหรือเลขโต๊ะ")

    def click_add_new_menu(self):
        add_menu_page.setWindowModality(QtCore.Qt.ApplicationModal)
        add_menu_page.show()


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


class EditRestaurantInfo(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditRestaurantInfo, self).__init__(parent)
        self.ui = edit_rest_info.Ui_Dialog()
        self.setting = QtCore.QSettings('config', 'restaurant')
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(self.to_confirm_update)
        self.ui.cancel_button.clicked.connect(self.click_cancel)

    def set_rest_name(self):
        old_name = self.setting.value('rest_name')
        self.ui.old_rest_name.setText(old_name)

    def to_confirm_update(self):
        old_name = self.setting.value('rest_name')
        new_name = self.ui.new_rest_name_lineedit.text()
        mes_str = "คุณต้องการเปลี่ยนชื่อร้าน จาก \"{}\" เป็น \"{}\" หรือไม่".format(old_name, new_name)

        if yes_no_message_box(self, "การแก้ไขข้อมูลร้าน", mes_str):
            self.click_update()

    def click_update(self):
        old_name = self.setting.value('rest_name')
        new_name = self.ui.new_rest_name_lineedit.text()
        if data_controller.update_rest_name(old_name, new_name):
            self.hide()
            self.setting.setValue('rest_name', new_name)
            main_page.ui.tableName.setText(new_name)
            self.ui.new_rest_name_lineedit.clear()

        else:
            message_box("Error", "เกิดข้อผิดพลาดกรุณาลองอีกครั้ง")

    def click_cancel(self):
        self.hide()
        self.ui.new_rest_name_lineedit.clear()


class HistoryDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(HistoryDialog, self).__init__(parent)
        self.ui = history.Ui_Dialog()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings('config', 'restaurant')
        self.ui.clear_history.clicked.connect(self.clear_history)

    def table_manage(self):
        table_header = ["ชื่อโต๊ะ", "จำนวนคน", "เวลาเข้า", "วันที่เข้า", "ราคามื้อนี้", "สถานะ"]
        self.model = QtGui.QStandardItemModel()
        self.ui.tableView.setModel(self.model)

        self.model.setHorizontalHeaderLabels(table_header)
        self.ui.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.tableView.setSortingEnabled(True)
        self.ui.tableView.sortByColumn(4, QtCore.Qt.DescendingOrder)
        rest_name = self.settings.value('rest_name')
        self.data = data_controller.get_all_table_data(rest_name)
        self.row_values = []

        for i in self.data:
            if i["status"] == "A":
                status = "ยังอยู่ที่ร้าน"
            elif i["status"] == "C":
                status = "ยกเลิกรายการแล้ว"
            elif i["status"] == "T":
                status = "หมดเวลาแล้ว"
            elif i["status"] == "S":
                status = "ชำระเงินแล้ว"
            else:
                status = "N/A"

            sub_value = [i["table_name"], i["person"], i["in_time"], i["date"], i["price"], status]
            self.row_values.append(sub_value)

        for x, y in enumerate(self.row_values):
            row = []
            for k, item in enumerate(y):
                if k == 4:
                    cell = QtGui.QStandardItem("{:,}".format(item))
                else:
                    cell = QtGui.QStandardItem(str(item))

                if item == "ยกเลิกรายการแล้ว" or item == "หมดเวลาแล้ว":
                    cell.setForeground(QtGui.QColor(255, 0, 0))
                elif item == "ชำระเงินแล้ว":
                    cell.setForeground(QtGui.QColor(0, 150, 15))
                row.append(cell)
            self.model.appendRow(row)

    def clear_history(self):
        rest_name = self.settings.value('rest_name')
        if yes_no_message_box(self, "ล้างประวัติ", "คุณต้องการที่จะล้างประวัติหรือไม่(สถานะที่ยังอยู่ที่ร้านไม่ถูกลบ)"):
            if data_controller.remove_history(rest_name):
                self.table_manage()


class CheckBillDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CheckBillDialog, self).__init__(parent)
        self.ui = check_bill.Ui_Dialog()
        self.ui.setupUi(self)
        self.setting = QtCore.QSettings('config', 'restaurant')
        self.table_name = ""
        self.ui.cancel_button.clicked.connect(self.dimiss)
        self.ui.check_bill_button.clicked.connect(self.check_bill)

    def dimiss(self):
        self.hide()

    def list_menu(self, table_name, rest_name):
        self.data = data_controller.get_one_table_data(rest_name, table_name)
        self.data_set = {"table_name": self.data["table_name"], "person": self.data["person"], "in_time": self.data["in_time"]}
        self.ui.table_name.setText("{}".format(self.data["table_name"]))
        self.ui.person.setText(self.data["person"])
        self.ui.in_time.setText(self.data["in_time"])
        self.ui.total_price_label.setText("{:,}".format(self.data["price"]))

        header = ["ชื่ออาหาร", "จำนวน", "ราคา"]
        self.model = QtGui.QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(header)
        self.ui.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.tableView.setColumnWidth(0, 100)

        menu_values = []
        for i in self.data["menu_set"]:
            sub_values = [i["menu_name"], i["quantity"], i["price"]]
            menu_values.append(sub_values)

        for j in menu_values:
            row = []
            for k in j:
                cell = QtGui.QStandardItem(str(k))
                row.append(cell)
            self.model.appendRow(row)

    def check_bill(self):
        rest_name = self.setting.value('rest_name')
        table_name = self.data_set["table_name"]
        if data_controller.commit_bill(rest_name, table_name):
            self.hide()
            done_bill_page.setWindowModality(QtCore.Qt.ApplicationModal)
            done_bill_page.set_value(self.data)
            done_bill_page.show()


class DoneBill(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DoneBill, self).__init__(parent)
        self.ui = done_bill.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(self.click_ok)
        self.ui.print_button.clicked.connect(self.click_print)
        self.data = {}

    def set_value(self, item):
        self.data = item

    def click_ok(self):
        self.hide()
        main_page.table_manage()

    def click_print(self):
        strr = "\n{}\n".format(self.data["restaurant_name"])
        strr += "ชื่อโต๊ะ : {}\n".format(self.data["table_name"])
        strr += "จำนวนคน : {}\n".format(self.data["person"])
        strr += "เวลาเข้า : {}\n".format(self.data["in_time"])
        strr += "{}\n".format("*" * 30)

        menu_set = ""
        for x, i in enumerate(self.data["menu_set"]):
            menu_set += "{0:3}. {1:15}\t{2:>4} หน่วย {3:>10}\n".format(x + 1, i["menu_name"], i["quantity"], i["price"])
        strr += menu_set
        strr += "{}\n".format("*" * 30)
        strr += "ราคารวมทั้งหมด {} บาท\n".format(self.data["price"])
        strr += "ขอบคุณที่ใช้บริการ"

        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()

        printer.setPageMargins(10.0, 10.0, 0.0, 0.0, QtPrintSupport.QPrinter.Point)
        printer.setFullPage(True)

        painter.begin(printer)
        painter.drawText(painter.viewport(), QtCore.Qt.AlignTop, strr)
        painter.end()
        message_box("กำลังพิมพ์", "ได้ส่งใบเสร็จไปที่เครื่องพิมพ์แล้ว")


class ResultWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ResultWindow, self).__init__(parent)
        self.ui = result.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setting = QtCore.QSettings('config', 'restaurant')
        self.ui.history_button.clicked.connect(self.click_see_history)
        self.ui.menu_button.clicked.connect(self.click_see_menu)

    def click_see_history(self):
        history_page.setWindowModality(QtCore.Qt.ApplicationModal)
        history_page.show()
        history_page.table_manage()

    def click_see_menu(self):
        menu_page.setWindowModality(QtCore.Qt.ApplicationModal)
        menu_page.show()
        menu_page.table_manage()

    def display_result(self):
        top_table_header = ["ชื่อโต๊ะ", "เวลาเข้า", "วันที่", "ยอดขายรวม"]
        top_menu_header = ["ชื่อเมนู", "ประเภท", "ราคา", "จำนวนครั้งที่สั่ง"]

        self.top_table_model = QtGui.QStandardItemModel()
        self.top_menu_model = QtGui.QStandardItemModel()
        self.ui.top_table_tableView.setModel(self.top_table_model)
        self.ui.top_table_tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.top_table_tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.ui.top_menu_tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.top_menu_tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

        self.ui.top_menu_tableView.setModel(self.top_menu_model)
        self.top_table_model.setHorizontalHeaderLabels(top_table_header)
        self.top_menu_model.setHorizontalHeaderLabels(top_menu_header)

        rest_name = self.setting.value('rest_name')

        self.top_table_data = data_controller.get_top_table(rest_name)
        self.top_menu_data = data_controller.get_top_menu(rest_name)

        self.top_row_value = []
        self.top_menu_value = []

        for i in self.top_table_data:
            sub_value = [i["table_name"], i["in_time"], i["date"], "{:,}".format(i["price"])]
            self.top_row_value.append(sub_value)

        for iy in self.top_row_value:
            row = []
            for item in iy:
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)

            self.top_table_model.appendRow(row)

        for j in self.top_menu_data:
            sub_value = [j["menu_name"], j["category"], "{:,}".format(j["price"]), "{:,}".format(j["order"])]
            self.top_menu_value.append(sub_value)

        for jy in self.top_menu_value:
            row = []
            for item in jy:
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)

            self.top_menu_model.appendRow(row)

        total_data = data_controller.get_total_value(rest_name)
        self.ui.today_total_label.setText("ยอดขายรวมวันนี้ : {:,}".format(total_data["total_today"]))
        self.ui.done_label.setText("จำนวนครั้งชำระเงินทั้งหมด : {:,}".format(total_data["count_done"]))
        self.ui.cancel_label.setText("จำนวนครั้งที่ได้ยกเลิกรายการทั้งหมด : {:,}".format(total_data["count_cancel"]))
        self.ui.all_sale_label.setText("ยอดขายรวมที่ผ่านมาทั้งหมด : {:,}".format(total_data["total_all"]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # initialize
    login_page = LoginPage()
    main_page = MainPage()
    register_page = RegisterPage()
    add_table_page = AddTablePage()
    menu_page = MenuDialog()
    add_menu_page = AddMenuDialog()
    edit_menu_page = EditMenuDialog()
    edit_rest = EditRestaurantInfo()
    history_page = HistoryDialog()
    check_bill_page = CheckBillDialog()
    done_bill_page = DoneBill()
    result_page = ResultWindow()

    login_page.show()
    sys.exit(app.exec_())
