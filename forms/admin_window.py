# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_adminWindow(object):
    def setupUi(self, adminWindow):
        adminWindow.setObjectName(_fromUtf8("adminWindow"))
        adminWindow.setWindowModality(QtCore.Qt.WindowModal)
        adminWindow.resize(600, 508)
        adminWindow.setMinimumSize(QtCore.QSize(600, 500))
        adminWindow.setMaximumSize(QtCore.QSize(600, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        adminWindow.setWindowIcon(icon)
        adminWindow.setStyleSheet(_fromUtf8("#adminWindow{\n"
"border-image: url(:/backgrounds/images/backgounds/_10.jpg);\n"
"}"))
        self.centralwidget = QtGui.QWidget(adminWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 20, 512, 70))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonStaffNew = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonStaffNew.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonStaffNew.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStaffNew.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/staff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStaffNew.setIcon(icon1)
        self.pushButtonStaffNew.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonStaffNew.setObjectName(_fromUtf8("pushButtonStaffNew"))
        self.horizontalLayout.addWidget(self.pushButtonStaffNew)
        self.pushButtonStaffModify = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonStaffModify.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonStaffModify.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStaffModify.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/edit_staff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStaffModify.setIcon(icon2)
        self.pushButtonStaffModify.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonStaffModify.setObjectName(_fromUtf8("pushButtonStaffModify"))
        self.horizontalLayout.addWidget(self.pushButtonStaffModify)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 20, 512, 70))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButtonSparepartsAdd = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButtonSparepartsAdd.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonSparepartsAdd.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSparepartsAdd.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/headphone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSparepartsAdd.setIcon(icon3)
        self.pushButtonSparepartsAdd.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonSparepartsAdd.setObjectName(_fromUtf8("pushButtonSparepartsAdd"))
        self.horizontalLayout_4.addWidget(self.pushButtonSparepartsAdd)
        self.pushButtonSparepartsCheck = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButtonSparepartsCheck.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonSparepartsCheck.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSparepartsCheck.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/headphone_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSparepartsCheck.setIcon(icon4)
        self.pushButtonSparepartsCheck.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonSparepartsCheck.setObjectName(_fromUtf8("pushButtonSparepartsCheck"))
        self.horizontalLayout_4.addWidget(self.pushButtonSparepartsCheck)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(60, 20, 512, 70))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButtonSmsPurchase = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButtonSmsPurchase.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonSmsPurchase.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSmsPurchase.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/envelope_buy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSmsPurchase.setIcon(icon5)
        self.pushButtonSmsPurchase.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonSmsPurchase.setObjectName(_fromUtf8("pushButtonSmsPurchase"))
        self.horizontalLayout_5.addWidget(self.pushButtonSmsPurchase)
        self.pushButtonSmsCheck = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButtonSmsCheck.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonSmsCheck.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSmsCheck.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/envelope2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSmsCheck.setIcon(icon6)
        self.pushButtonSmsCheck.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonSmsCheck.setObjectName(_fromUtf8("pushButtonSmsCheck"))
        self.horizontalLayout_5.addWidget(self.pushButtonSmsCheck)
        self.pushButtonSmsChangeAccount = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButtonSmsChangeAccount.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonSmsChangeAccount.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSmsChangeAccount.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/envelope_plus2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSmsChangeAccount.setIcon(icon7)
        self.pushButtonSmsChangeAccount.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonSmsChangeAccount.setObjectName(_fromUtf8("pushButtonSmsChangeAccount"))
        self.horizontalLayout_5.addWidget(self.pushButtonSmsChangeAccount)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget_4 = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget_4.setGeometry(QtCore.QRect(60, 20, 512, 70))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButtonTransactionLog = QtGui.QPushButton(self.layoutWidget_4)
        self.pushButtonTransactionLog.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonTransactionLog.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonTransactionLog.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/naira.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonTransactionLog.setIcon(icon8)
        self.pushButtonTransactionLog.setObjectName(_fromUtf8("pushButtonTransactionLog"))
        self.horizontalLayout_6.addWidget(self.pushButtonTransactionLog)
        self.pushButtonLogCheck = QtGui.QPushButton(self.layoutWidget_4)
        self.pushButtonLogCheck.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButtonLogCheck.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogCheck.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/log.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogCheck.setIcon(icon9)
        self.pushButtonLogCheck.setObjectName(_fromUtf8("pushButtonLogCheck"))
        self.horizontalLayout_6.addWidget(self.pushButtonLogCheck)
        self.verticalLayout.addWidget(self.groupBox_4)
        adminWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(adminWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        adminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(adminWindow)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        adminWindow.setWindowTitle(_translate("adminWindow", "ADMIN", None))
        self.groupBox.setTitle(_translate("adminWindow", "Manage Staff", None))
        self.pushButtonStaffNew.setText(_translate("adminWindow", "NEW", None))
        self.pushButtonStaffModify.setText(_translate("adminWindow", "MODIFY", None))
        self.groupBox_3.setTitle(_translate("adminWindow", "Accessories", None))
        self.pushButtonSparepartsAdd.setText(_translate("adminWindow", "ADD", None))
        self.pushButtonSparepartsCheck.setText(_translate("adminWindow", "CHECK / UPDATE", None))
        self.groupBox_2.setTitle(_translate("adminWindow", "SMS", None))
        self.pushButtonSmsPurchase.setText(_translate("adminWindow", "PURCHASE", None))
        self.pushButtonSmsCheck.setText(_translate("adminWindow", "UNITS", None))
        self.pushButtonSmsChangeAccount.setText(_translate("adminWindow", "CHANGE ACCOUNT", None))
        self.groupBox_4.setTitle(_translate("adminWindow", "LOG", None))
        self.pushButtonTransactionLog.setText(_translate("adminWindow", "TRANSACTIONS", None))
        self.pushButtonLogCheck.setText(_translate("adminWindow", "ACTIVITY", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    adminWindow = QtGui.QMainWindow()
    ui = Ui_adminWindow()
    ui.setupUi(adminWindow)
    adminWindow.show()
    sys.exit(app.exec_())

