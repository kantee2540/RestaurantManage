# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        MainWindow.setMinimumSize(QtCore.QSize(450, 600))
        MainWindow.setMaximumSize(QtCore.QSize(450, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setEnabled(True)
        self.error_label.setMinimumSize(QtCore.QSize(0, 30))
        self.error_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.error_label.setFont(font)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.rest_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.rest_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.rest_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rest_edit.setFont(font)
        self.rest_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.rest_edit.setObjectName("rest_edit")
        self.verticalLayout.addWidget(self.rest_edit)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.user_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_edit.setFont(font)
        self.user_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.user_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.user_edit.setObjectName("user_edit")
        self.verticalLayout.addWidget(self.user_edit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.pass_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_edit.setFont(font)
        self.pass_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_edit.setObjectName("pass_edit")
        self.verticalLayout.addWidget(self.pass_edit)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pass_con_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_con_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.pass_con_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_con_edit.setFont(font)
        self.pass_con_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pass_con_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_con_edit.setObjectName("pass_con_edit")
        self.verticalLayout.addWidget(self.pass_con_edit)
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setMinimumSize(QtCore.QSize(0, 50))
        self.register_button.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.register_button.setFont(font)
        self.register_button.setObjectName("register_button")
        self.verticalLayout.addWidget(self.register_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ลงทะเบียน"))
        self.error_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">โปรดกรอกรายละเอียดให้ครบ หรือรหัสผ่านไม่ตรงกัน</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "ชื่อร้านค้า"))
        self.label_5.setText(_translate("MainWindow", "บัญชีผู้ใช้"))
        self.label_3.setText(_translate("MainWindow", "รหัสผ่าน"))
        self.label_4.setText(_translate("MainWindow", "ยืนยันรหัสผ่าน"))
        self.register_button.setText(_translate("MainWindow", "ลงทะเบียน"))
