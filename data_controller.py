from PyQt5 import QtWidgets, QtCore
import pymongo
import hashlib
import datetime

projectDb = "Restaurant"


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
        db = client.get_database(projectDb)

        username = self.ui.user_edit.text()
        password = hashlib.md5(self.ui.pass_edit.text().encode()).hexdigest()
        login_user = db.User.find_one({"username": username})
        if login_user:
            if password == login_user["password"]:
                #self.user = login_user["username"]
                self.setting.setValue('user', login_user["username"])
                self.setting.setValue('rest_name', login_user["restaurant_name"])
                return True
            else:
                return False

        else:
            return False

    except Exception as e:
        print("Error = {}".format(e))
        message_box("Error", "Error : {}".format(e))


def update_rest_name(old_name, new_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        up_user = db.User.update({"restaurant_name": old_name}, {"$set": {"restaurant_name": new_name}})
        up_table = db.Table.update_many({"restaurant_name": old_name}, {"$set": {"restaurant_name": new_name}})
        up_menu = db.Menu.update_many({"restaurant_name": old_name}, {"$set": {"restaurant_name": new_name}})
        if up_user and up_table and up_menu:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message : \"{}\"Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_user_detail(username):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
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
        db = client.get_database(projectDb)

        restaurant_name = self.ui.rest_edit.text()
        username = self.ui.user_edit.text()
        password = self.ui.pass_edit.text()
        password_encrypt = hashlib.md5(password.encode()).hexdigest()

        data = {"restaurant_name": restaurant_name, "username": username, "password": password_encrypt}
        rs = db.User.insert_one(data)
        if rs:
            message_box("Register", "ลงทะเบียนสำเร็จ\n ชื่อบัญชีเข้าใช้ของคุณ : {}".format(username))
            clear_lineedit(self)
            self.close()

    except Exception as e:
        message_box("Error", "Error message : \"{}\"Please Contact ch.kantee_st@tni.ac.th".format(e))


def add_table(table_name, person, menu_set, restaurant):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        current_time = datetime.datetime.now().strftime("%X")
        today = datetime.datetime.now().strftime("%x")

        added_list = []
        total_price = 0
        for i in menu_set:
            price = i["price"]
            total_price += price

            # +1 order
            if i["menu_name"] not in added_list:
                added_list.append(i["menu_name"])
                db.Menu.update({"menu_name": i["menu_name"]}, {"$inc": {"order": + 1}})
            else:
                continue

        data = {"table_name": table_name,
                "person": person,
                "in_time": current_time,
                "date": today,
                "price": total_price,
                "menu_set": menu_set,
                "status": "A",
                "restaurant_name": restaurant}
        at = db.Table.insert_one(data)
        if at:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_table_data(rest_name):
    # STATUS DEFINE
    # A => Active
    # T => Time 's up
    # C => Cancelled
    # S => Success and has paid
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        table_data = db.Table.find({"$and": [{"restaurant_name": rest_name}, {"status": "A"}]})
        if table_data:
            return table_data

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_one_table_data(rest_name, table_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        table_data = db.Table.find_one({"$and": [{"restaurant_name": rest_name}, {"table_name": table_name}, {"status": "A"}]})
        if table_data:
            return table_data

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def commit_bill(rest_name, table_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        cb = db.Table.update({"$and": [{"restaurant_name": rest_name}, {"table_name": table_name}]},
                             {"$set": {"status": "S"}})
        if cb:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_all_table_data(rest_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        table_data = db.Table.find({"restaurant_name": rest_name})
        if table_data:
            return table_data

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def remove_history(rest_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        dht = db.Table.delete_many({"$and": [{"restaurant_name": rest_name}, {"status": {"$nin": ["A"]}}]})
        if dht:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def cancel_table_order(rest_name, table_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        ct = db.Table.update({"$and": [{"table_name": table_name}, {"restaurant_name": rest_name}]},
                             {"$set": {"status": "C"}})
        if ct:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def add_menu(menu_name, price, category, restaurant):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        data = {"menu_name": menu_name,
                "price": price,
                "category": category,
                "restaurant_name": restaurant,
                "order": 0}
        am = db.Menu.insert_one(data)
        if am:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_menu_data(rest_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        data = db.Menu.find({"restaurant_name": rest_name})
        if data:
            return data

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def remove_menu(menu_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        dm = db.Menu.delete_one({"menu_name": menu_name})
        if dm:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def update_menu(old_menu_name, menu_name, price, category):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        data = db.Menu.update({"menu_name": old_menu_name},
                              {"$set": {"menu_name": menu_name,
                                        "price": price,
                                        "category": category}})
        if data:
            return True
        else:
            return False

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_top_table(rest_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        data = db.Table.find({"$and": [{"restaurant_name": rest_name},
                                       {"status": "S"}]}).sort("price", pymongo.DESCENDING).limit(10)
        if data:
            return data

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_top_menu(rest_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        data = db.Menu.find({"restaurant_name": rest_name}).sort("order", pymongo.DESCENDING).limit(10)
        if data:
            return data

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def get_total_value(rest_name):
    try:
        client = get_database_client()
        db = client.get_database(projectDb)
        today = datetime.datetime.now().strftime("%x")
        data_today = db.Table.find({"$and": [{"restaurant_name": rest_name},
                                    {"date": today}, {"status": "S"}]})
        data_all = db.Table.find({"$and": [{"restaurant_name": rest_name}, {"status": "S"}]})
        count_cancelled = db.Table.count_documents({"$and": [{"restaurant_name": rest_name}, {"status": "C"}]})
        count_done = db.Table.count_documents({"$and": [{"restaurant_name": rest_name}, {"status": "S"}]})

        if data_today and data_all:
            total_today = 0
            total_all = 0

            for i in data_today:
                total_today += i["price"]

            for j in data_all:
                total_all += j["price"]

            return {"total_today": total_today, "total_all": total_all,
                    "count_cancel": count_cancelled, "count_done": count_done}

    except Exception as e:
        message_box("Error", "Error message: \"{}\" Please Contact ch.kantee_st@tni.ac.th".format(e))


def clear_lineedit(self):
    self.ui.rest_edit.clear()
    self.ui.user_edit.clear()
    self.ui.pass_edit.clear()
    self.ui.pass_con_edit.clear()
