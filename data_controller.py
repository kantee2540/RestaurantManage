from PyQt5 import QtWidgets, QtCore
import pymongo
import hashlib


def get_database_client():
    return pymongo.MongoClient("mongodb+srv://kantee2540:K%61n%742540@cluster0-ww6d1.mongodb.net/test?retryWrites=true&w=majority")


def message_box(title, text_message):
    message = QtWidgets.QMessageBox()
    message.setIcon(QtWidgets.QMessageBox.Information)
    message.setText(text_message)
    message.setWindowTitle(title)
    message.exec_()


def login_authen(self):
    try:
        client = get_database_client()
        db = client.get_database("Restaurant")

        username = self.ui.user_edit.text()
        password = hashlib.md5(self.ui.pass_edit.text().encode()).hexdigest()
        login_user = db.User.find_one({"username": username})
        if login_user:
            if password == login_user["password"]:
                self.user = login_user["username"]
                return True
            else:
                return False

        else:
            return False

    except Exception as e:
        print("Error = {}".format(e))
        message_box("Error", "Error : {}".format(e))


def get_user_detail(username):
    try:
        client = get_database_client()
        db = client.get_database("Restaurant")
        user = db.User.find_one({"username": username})
        if user:
            return user["restaurant_name"]
        else:
            return "USER NOT FOUND"

    except Exception as e:
        print("Error = {}".format(e))


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
            clear_lineedit(self)
            self.close()

    except Exception as e:
        message_box("Error", "Error message : \"{}\"Please Contact ch.kantee_st@tni.ac.th".format(e))


def clear_lineedit(self):
    self.ui.rest_edit.clear()
    self.ui.user_edit.clear()
    self.ui.pass_edit.clear()
    self.ui.pass_con_edit.clear()
