# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fixed_items.ui'
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

class Ui_fixedWindow(object):
    def setupUi(self, fixedWindow):
        fixedWindow.setObjectName(_fromUtf8("fixedWindow"))
        fixedWindow.setWindowModality(QtCore.Qt.WindowModal)
        fixedWindow.resize(900, 415)
        fixedWindow.setMinimumSize(QtCore.QSize(900, 415))
        fixedWindow.setMaximumSize(QtCore.QSize(900, 415))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/naira.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fixedWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(fixedWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonReceiveMoney = QtGui.QPushButton(self.centralwidget)
        self.pushButtonReceiveMoney.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButtonReceiveMoney.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonReceiveMoney.setText(_fromUtf8(""))
        self.pushButtonReceiveMoney.setIcon(icon)
        self.pushButtonReceiveMoney.setObjectName(_fromUtf8("pushButtonReceiveMoney"))
        self.horizontalLayout.addWidget(self.pushButtonReceiveMoney)
        self.pushButtonSendSms = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSendSms.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButtonSendSms.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonSendSms.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/envelope2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSendSms.setIcon(icon1)
        self.pushButtonSendSms.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonSendSms.setObjectName(_fromUtf8("pushButtonSendSms"))
        self.horizontalLayout.addWidget(self.pushButtonSendSms)
        self.verticalLayout.addLayout(self.horizontalLayout)
        fixedWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fixedWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fixedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(fixedWindow)
        QtCore.QMetaObject.connectSlotsByName(fixedWindow)

    def retranslateUi(self, fixedWindow):
        fixedWindow.setWindowTitle(_translate("fixedWindow", "FIXED ITEMS", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("fixedWindow", "id", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("fixedWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("fixedWindow", "Customer Name", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("fixedWindow", "Price", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("fixedWindow", "Customer Informed", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("fixedWindow", "Paid", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("fixedWindow", "Payment Date", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("fixedWindow", "Returned Date", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("fixedWindow", "Received Date", None))
        self.pushButtonReceiveMoney.setStatusTip(_translate("fixedWindow", "Money received", None))
        self.pushButtonSendSms.setStatusTip(_translate("fixedWindow", "Alert Customer", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    fixedWindow = QtGui.QMainWindow()
    ui = Ui_fixedWindow()
    ui.setupUi(fixedWindow)
    fixedWindow.show()
    sys.exit(app.exec_())

