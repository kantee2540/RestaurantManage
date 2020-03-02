# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_rest_info.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(341, 197)
        Dialog.setMinimumSize(QtCore.QSize(341, 197))
        Dialog.setMaximumSize(QtCore.QSize(341, 197))
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setMinimumSize(QtCore.QSize(0, 30))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setMinimumSize(QtCore.QSize(0, 30))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.new_rest_name_lineedit = QtWidgets.QLineEdit(Dialog)
        self.new_rest_name_lineedit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.new_rest_name_lineedit.setObjectName("new_rest_name_lineedit")
        self.gridLayout.addWidget(self.new_rest_name_lineedit, 3, 1, 1, 1)
        self.old_rest_name = QtWidgets.QLabel(Dialog)
        self.old_rest_name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.old_rest_name.setObjectName("old_rest_name")
        self.gridLayout.addWidget(self.old_rest_name, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "แก้ไขข้อมูลร้าน"))
        self.ok_button.setText(_translate("Dialog", "แก้ไขชื่อร้าน"))
        self.cancel_button.setText(_translate("Dialog", "ยกเลิก"))
        self.label_4.setText(_translate("Dialog", "ชื่อร้านใหม่"))
        self.label.setText(_translate("Dialog", "แก้ไขข้อมูลร้าน"))
        self.new_rest_name_lineedit.setPlaceholderText(_translate("Dialog", "ป้อนชื่อร้านใหม่ของคุณ"))
        self.old_rest_name.setText(_translate("Dialog", "[Rest_Name]"))
        self.label_2.setText(_translate("Dialog", "ชื่อร้านปัจจุบัน"))
