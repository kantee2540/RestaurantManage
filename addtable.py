# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtable.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 700)
        MainWindow.setMinimumSize(QtCore.QSize(550, 700))
        MainWindow.setMaximumSize(QtCore.QSize(550, 700))
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setVerticalSpacing(13)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.table_name_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.table_name_lineedit.setMinimumSize(QtCore.QSize(0, 30))
        self.table_name_lineedit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.table_name_lineedit.setFont(font)
        self.table_name_lineedit.setText("")
        self.table_name_lineedit.setObjectName("table_name_lineedit")
        self.gridLayout.addWidget(self.table_name_lineedit, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.person_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.person_spinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.person_spinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.person_spinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.person_spinBox.setMinimum(1)
        self.person_spinBox.setObjectName("person_spinBox")
        self.gridLayout.addWidget(self.person_spinBox, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.menu_table = QtWidgets.QTableView(self.centralwidget)
        self.menu_table.setObjectName("menu_table")
        self.gridLayout.addWidget(self.menu_table, 5, 0, 1, 2)
        self.add_table_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_table_button.setMinimumSize(QtCore.QSize(0, 35))
        self.add_table_button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.add_table_button.setObjectName("add_table_button")
        self.gridLayout.addWidget(self.add_table_button, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Table"))
        self.label.setText(_translate("MainWindow", "ชื่อโต๊ะ / เลขโต๊ะ"))
        self.label_3.setText(_translate("MainWindow", "จำนวนคน"))
        self.label_2.setText(_translate("MainWindow", "เมนูอาหาร"))
        self.add_table_button.setText(_translate("MainWindow", "เพิ่มโต๊ะ"))
