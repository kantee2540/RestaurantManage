# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 702)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 60, 461, 571))
        self.tableView.setObjectName("tableView")
        self.remove_menu_button = QtWidgets.QPushButton(Dialog)
        self.remove_menu_button.setGeometry(QtCore.QRect(360, 650, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_menu_button.setFont(font)
        self.remove_menu_button.setObjectName("remove_menu_button")
        self.edit_menu_button = QtWidgets.QPushButton(Dialog)
        self.edit_menu_button.setGeometry(QtCore.QRect(230, 650, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_menu_button.setFont(font)
        self.edit_menu_button.setObjectName("edit_menu_button")
        self.add_menu_button = QtWidgets.QPushButton(Dialog)
        self.add_menu_button.setGeometry(QtCore.QRect(100, 650, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_menu_button.setFont(font)
        self.add_menu_button.setObjectName("add_menu_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Food Menu"))
        self.label.setText(_translate("Dialog", "เมนูอาหารทั้งหมด"))
        self.remove_menu_button.setText(_translate("Dialog", "ลบเมนูอาหาร"))
        self.edit_menu_button.setText(_translate("Dialog", "แก้ไขเมนูอาหาร"))
        self.add_menu_button.setText(_translate("Dialog", "เพิ่มเมนูอาหาร"))
