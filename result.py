# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 707)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.top_menu_tableView = QtWidgets.QTableView(self.centralwidget)
        self.top_menu_tableView.setObjectName("top_menu_tableView")
        self.gridLayout.addWidget(self.top_menu_tableView, 2, 1, 1, 1)
        self.top_table_tableView = QtWidgets.QTableView(self.centralwidget)
        self.top_table_tableView.setObjectName("top_table_tableView")
        self.gridLayout.addWidget(self.top_table_tableView, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.cancel_label = QtWidgets.QLabel(self.centralwidget)
        self.cancel_label.setObjectName("cancel_label")
        self.gridLayout.addWidget(self.cancel_label, 7, 0, 1, 1)
        self.done_label = QtWidgets.QLabel(self.centralwidget)
        self.done_label.setObjectName("done_label")
        self.gridLayout.addWidget(self.done_label, 6, 0, 1, 1)
        self.all_sale_label = QtWidgets.QLabel(self.centralwidget)
        self.all_sale_label.setObjectName("all_sale_label")
        self.gridLayout.addWidget(self.all_sale_label, 8, 0, 1, 1)
        self.today_total_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.today_total_label.setFont(font)
        self.today_total_label.setObjectName("today_total_label")
        self.gridLayout.addWidget(self.today_total_label, 5, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.menu_button.setObjectName("menu_button")
        self.verticalLayout.addWidget(self.menu_button)
        self.history_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.history_button.setObjectName("history_button")
        self.verticalLayout.addWidget(self.history_button)
        self.gridLayout.addLayout(self.verticalLayout, 5, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 23))
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
        self.label_3.setText(_translate("MainWindow", "เเมนูที่นิยมสั่งมากที่สุด"))
        self.label_2.setText(_translate("MainWindow", "โต๊ะที่มียอดขายสูงสุด"))
        self.label.setText(_translate("MainWindow", "สรุปยอดขาย"))
        self.cancel_label.setText(_translate("MainWindow", "จำนวนครั้งที่ได้ยกเลิกรายการทั้งหมด : 0"))
        self.done_label.setText(_translate("MainWindow", "จำนวนครั้งชำระเงินทั้งหมด : 0"))
        self.all_sale_label.setText(_translate("MainWindow", "ยอดขายรวมที่ผ่านมาทั้งหมด : 0"))
        self.today_total_label.setText(_translate("MainWindow", "ยอดขายรวมวันนี้ : 0"))
        self.menu_button.setText(_translate("MainWindow", "เมนูอาหารทั้งหมด"))
        self.history_button.setText(_translate("MainWindow", "ประวัติรายการลูกค้า"))
