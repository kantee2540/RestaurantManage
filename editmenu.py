# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editmenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 349)
        Dialog.setMinimumSize(QtCore.QSize(390, 342))
        Dialog.setMaximumSize(QtCore.QSize(390, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.menu_name_lineedit = QtWidgets.QLineEdit(Dialog)
        self.menu_name_lineedit.setMinimumSize(QtCore.QSize(0, 30))
        self.menu_name_lineedit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_name_lineedit.setFont(font)
        self.menu_name_lineedit.setText("")
        self.menu_name_lineedit.setObjectName("menu_name_lineedit")
        self.verticalLayout.addWidget(self.menu_name_lineedit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.menu_type_comboBox = QtWidgets.QComboBox(Dialog)
        self.menu_type_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.menu_type_comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_type_comboBox.setFont(font)
        self.menu_type_comboBox.setObjectName("menu_type_comboBox")
        self.menu_type_comboBox.addItem("")
        self.menu_type_comboBox.addItem("")
        self.verticalLayout.addWidget(self.menu_type_comboBox)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.price_spinbox = QtWidgets.QDoubleSpinBox(Dialog)
        self.price_spinbox.setMinimumSize(QtCore.QSize(0, 30))
        self.price_spinbox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.price_spinbox.setFont(font)
        self.price_spinbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.price_spinbox.setMaximum(9999.99)
        self.price_spinbox.setObjectName("price_spinbox")
        self.verticalLayout.addWidget(self.price_spinbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EditMenu"))
        self.label.setText(_translate("Dialog", "แก้ไขเมนูอาหาร"))
        self.label_2.setText(_translate("Dialog", "ชื่อเมนูอาหาร"))
        self.label_3.setText(_translate("Dialog", "ประเภทเมนูอาหาร"))
        self.menu_type_comboBox.setItemText(0, _translate("Dialog", "บุฟเฟ่"))
        self.menu_type_comboBox.setItemText(1, _translate("Dialog", "อาหารจานเดี่ยว"))
        self.label_4.setText(_translate("Dialog", "ราคาอาหาร"))
        self.ok_button.setText(_translate("Dialog", "แก้ไขเมนูนี้"))
        self.cancel_button.setText(_translate("Dialog", "ยกเลิก"))
