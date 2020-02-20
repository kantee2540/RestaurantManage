# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 252)
        Dialog.setMinimumSize(QtCore.QSize(390, 252))
        Dialog.setMaximumSize(QtCore.QSize(390, 252))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.menu_name_lineedit = QtWidgets.QLineEdit(Dialog)
        self.menu_name_lineedit.setGeometry(QtCore.QRect(20, 80, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_name_lineedit.setFont(font)
        self.menu_name_lineedit.setText("")
        self.menu_name_lineedit.setObjectName("menu_name_lineedit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.menu_type_comboBox = QtWidgets.QComboBox(Dialog)
        self.menu_type_comboBox.setGeometry(QtCore.QRect(20, 140, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_type_comboBox.setFont(font)
        self.menu_type_comboBox.setObjectName("menu_type_comboBox")
        self.menu_type_comboBox.addItem("")
        self.menu_type_comboBox.addItem("")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(260, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(140, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Addmenu"))
        self.label.setText(_translate("Dialog", "เพิ่มเมนูอาหาร"))
        self.label_2.setText(_translate("Dialog", "ชื่อเมนูอาหาร"))
        self.label_3.setText(_translate("Dialog", "ประเภทเมนูอาหาร"))
        self.menu_type_comboBox.setItemText(0, _translate("Dialog", "บุฟเฟ่"))
        self.menu_type_comboBox.setItemText(1, _translate("Dialog", "อาหารจานเดี่ยว"))
        self.cancel_button.setText(_translate("Dialog", "ยกเลิก"))
        self.ok_button.setText(_translate("Dialog", "เพิ่มเมนูอาหาร"))
