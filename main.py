# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableName = QtWidgets.QLabel(self.centralwidget)
        self.tableName.setGeometry(QtCore.QRect(20, 10, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tableName.setFont(font)
        self.tableName.setTextFormat(QtCore.Qt.AutoText)
        self.tableName.setObjectName("tableName")
        self.check_bill = QtWidgets.QPushButton(self.centralwidget)
        self.check_bill.setGeometry(QtCore.QRect(660, 580, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_bill.setFont(font)
        self.check_bill.setObjectName("check_bill")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(660, 530, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.add_table_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_table_button.setGeometry(QtCore.QRect(660, 480, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_table_button.setFont(font)
        self.add_table_button.setObjectName("add_table_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(660, 110, 221, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.person = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.person.setFont(font)
        self.person.setTextFormat(QtCore.Qt.PlainText)
        self.person.setObjectName("person")
        self.verticalLayout.addWidget(self.person)
        self.type = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type.setFont(font)
        self.type.setTextFormat(QtCore.Qt.PlainText)
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.timeleft = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeleft.setFont(font)
        self.timeleft.setTextFormat(QtCore.Qt.PlainText)
        self.timeleft.setObjectName("timeleft")
        self.verticalLayout.addWidget(self.timeleft)
        self.timein = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timein.setFont(font)
        self.timein.setTextFormat(QtCore.Qt.PlainText)
        self.timein.setObjectName("timein")
        self.verticalLayout.addWidget(self.timein)
        self.order_num = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.order_num.setFont(font)
        self.order_num.setTextFormat(QtCore.Qt.PlainText)
        self.order_num.setObjectName("order_num")
        self.verticalLayout.addWidget(self.order_num)
        self.table_no = QtWidgets.QLabel(self.centralwidget)
        self.table_no.setGeometry(QtCore.QRect(660, 40, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.table_no.setFont(font)
        self.table_no.setObjectName("table_no")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(15, 51, 621, 591))
        self.tableView.setObjectName("tableView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(660, 90, 221, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_Menu = QtWidgets.QAction(MainWindow)
        self.actionAdd_Menu.setObjectName("actionAdd_Menu")
        self.actionEdit_Menu = QtWidgets.QAction(MainWindow)
        self.actionEdit_Menu.setObjectName("actionEdit_Menu")
        self.actionSignout = QtWidgets.QAction(MainWindow)
        self.actionSignout.setObjectName("actionSignout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSignout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionAdd_Menu)
        self.menuMenu.addAction(self.actionEdit_Menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Restaurant"))
        self.tableName.setText(_translate("MainWindow", "RESTAURANT NAME"))
        self.check_bill.setText(_translate("MainWindow", "คิดเงิน"))
        self.cancel_button.setText(_translate("MainWindow", "ยกเลิกรายการ"))
        self.add_table_button.setText(_translate("MainWindow", "เพิ่มโต๊ะอาหาร"))
        self.person.setText(_translate("MainWindow", "จำนวนคน :"))
        self.type.setText(_translate("MainWindow", "ประเภท :"))
        self.timeleft.setText(_translate("MainWindow", "เวลาที่เหลือ :"))
        self.timein.setText(_translate("MainWindow", "เวลาเข้า :"))
        self.order_num.setText(_translate("MainWindow", "จำนวนเมนูอาหาร :"))
        self.table_no.setText(_translate("MainWindow", "A1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAdd_Menu.setText(_translate("MainWindow", "Add Menu..."))
        self.actionEdit_Menu.setText(_translate("MainWindow", "Edit Menu..."))
        self.actionSignout.setText(_translate("MainWindow", "Signout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
