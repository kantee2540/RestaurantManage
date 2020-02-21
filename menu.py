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
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 3)
        self.add_menu_button = QtWidgets.QPushButton(Dialog)
        self.add_menu_button.setMinimumSize(QtCore.QSize(0, 35))
        self.add_menu_button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_menu_button.setFont(font)
        self.add_menu_button.setObjectName("add_menu_button")
        self.gridLayout.addWidget(self.add_menu_button, 2, 0, 1, 1)
        self.edit_menu_button = QtWidgets.QPushButton(Dialog)
        self.edit_menu_button.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_menu_button.setFont(font)
        self.edit_menu_button.setObjectName("edit_menu_button")
        self.gridLayout.addWidget(self.edit_menu_button, 2, 1, 1, 1)
        self.remove_menu_button = QtWidgets.QPushButton(Dialog)
        self.remove_menu_button.setMinimumSize(QtCore.QSize(0, 35))
        self.remove_menu_button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_menu_button.setFont(font)
        self.remove_menu_button.setObjectName("remove_menu_button")
        self.gridLayout.addWidget(self.remove_menu_button, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Food Menu"))
        self.label.setText(_translate("Dialog", "เมนูอาหารทั้งหมด"))
        self.add_menu_button.setText(_translate("Dialog", "เพิ่มเมนูอาหาร"))
        self.edit_menu_button.setText(_translate("Dialog", "แก้ไขเมนูอาหาร"))
        self.remove_menu_button.setText(_translate("Dialog", "ลบเมนูอาหาร"))
