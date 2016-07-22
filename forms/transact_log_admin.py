# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transact_log_admin.ui'
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

class Ui_transactLog(object):
    def setupUi(self, transactLog):
        transactLog.setObjectName(_fromUtf8("transactLog"))
        transactLog.setWindowModality(QtCore.Qt.WindowModal)
        transactLog.resize(678, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/naira.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        transactLog.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(transactLog)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSelectDate1 = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSelectDate1.setObjectName(_fromUtf8("pushButtonSelectDate1"))
        self.horizontalLayout.addWidget(self.pushButtonSelectDate1)
        self.pushButtonSelectDate2 = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSelectDate2.setObjectName(_fromUtf8("pushButtonSelectDate2"))
        self.horizontalLayout.addWidget(self.pushButtonSelectDate2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(100, 0, 100, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBoxShowCash = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxShowCash.setMaximumSize(QtCore.QSize(50, 16777215))
        self.checkBoxShowCash.setObjectName(_fromUtf8("checkBoxShowCash"))
        self.horizontalLayout_4.addWidget(self.checkBoxShowCash)
        self.checkBoxShowPos = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxShowPos.setMaximumSize(QtCore.QSize(50, 16777215))
        self.checkBoxShowPos.setObjectName(_fromUtf8("checkBoxShowPos"))
        self.horizontalLayout_4.addWidget(self.checkBoxShowPos)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
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
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkBoxShowCalc = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxShowCalc.setObjectName(_fromUtf8("checkBoxShowCalc"))
        self.horizontalLayout_3.addWidget(self.checkBoxShowCalc)
        self.labelTitleIncome = QtGui.QLabel(self.centralwidget)
        self.labelTitleIncome.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitleIncome.setFont(font)
        self.labelTitleIncome.setObjectName(_fromUtf8("labelTitleIncome"))
        self.horizontalLayout_3.addWidget(self.labelTitleIncome)
        self.labelReceived = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelReceived.setFont(font)
        self.labelReceived.setObjectName(_fromUtf8("labelReceived"))
        self.horizontalLayout_3.addWidget(self.labelReceived)
        self.labelTitleExpense = QtGui.QLabel(self.centralwidget)
        self.labelTitleExpense.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitleExpense.setFont(font)
        self.labelTitleExpense.setObjectName(_fromUtf8("labelTitleExpense"))
        self.horizontalLayout_3.addWidget(self.labelTitleExpense)
        self.labelSpent = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSpent.setFont(font)
        self.labelSpent.setObjectName(_fromUtf8("labelSpent"))
        self.horizontalLayout_3.addWidget(self.labelSpent)
        self.labelTitleBalance = QtGui.QLabel(self.centralwidget)
        self.labelTitleBalance.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitleBalance.setFont(font)
        self.labelTitleBalance.setObjectName(_fromUtf8("labelTitleBalance"))
        self.horizontalLayout_3.addWidget(self.labelTitleBalance)
        self.labelBalance = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBalance.setFont(font)
        self.labelBalance.setObjectName(_fromUtf8("labelBalance"))
        self.horizontalLayout_3.addWidget(self.labelBalance)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBoxReceived = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxReceived.setObjectName(_fromUtf8("checkBoxReceived"))
        self.horizontalLayout_2.addWidget(self.checkBoxReceived)
        self.checkBoxSpent = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxSpent.setObjectName(_fromUtf8("checkBoxSpent"))
        self.horizontalLayout_2.addWidget(self.checkBoxSpent)
        self.checkBoxPurpose = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxPurpose.setObjectName(_fromUtf8("checkBoxPurpose"))
        self.horizontalLayout_2.addWidget(self.checkBoxPurpose)
        self.checkBoxMedium = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxMedium.setObjectName(_fromUtf8("checkBoxMedium"))
        self.horizontalLayout_2.addWidget(self.checkBoxMedium)
        self.checkBoxDate = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxDate.setObjectName(_fromUtf8("checkBoxDate"))
        self.horizontalLayout_2.addWidget(self.checkBoxDate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        transactLog.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(transactLog)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        transactLog.setStatusBar(self.statusbar)

        self.retranslateUi(transactLog)
        QtCore.QMetaObject.connectSlotsByName(transactLog)

    def retranslateUi(self, transactLog):
        transactLog.setWindowTitle(_translate("transactLog", "TRANSACTIONS", None))
        self.pushButtonSelectDate1.setText(_translate("transactLog", "Select Date", None))
        self.pushButtonSelectDate2.setText(_translate("transactLog", "Second Date (Optional)", None))
        self.checkBoxShowCash.setText(_translate("transactLog", "Cash", None))
        self.checkBoxShowPos.setText(_translate("transactLog", "POS", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("transactLog", "Id", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("transactLog", "Received", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("transactLog", "Spent", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("transactLog", "Purpose", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("transactLog", "Time", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("transactLog", "Medium", None))
        self.checkBoxShowCalc.setText(_translate("transactLog", "Show Total", None))
        self.labelTitleIncome.setText(_translate("transactLog", "INCOME :", None))
        self.labelReceived.setText(_translate("transactLog", "0", None))
        self.labelTitleExpense.setText(_translate("transactLog", "EXPENSE:", None))
        self.labelSpent.setText(_translate("transactLog", "0", None))
        self.labelTitleBalance.setText(_translate("transactLog", "BALANCE:", None))
        self.labelBalance.setText(_translate("transactLog", "0", None))
        self.checkBoxReceived.setText(_translate("transactLog", "Received", None))
        self.checkBoxSpent.setText(_translate("transactLog", "Spent", None))
        self.checkBoxPurpose.setText(_translate("transactLog", "Purpose", None))
        self.checkBoxMedium.setText(_translate("transactLog", "Medium", None))
        self.checkBoxDate.setText(_translate("transactLog", "Date", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    transactLog = QtGui.QMainWindow()
    ui = Ui_transactLog()
    ui.setupUi(transactLog)
    transactLog.show()
    sys.exit(app.exec_())
