# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_log.ui'
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

class Ui_logWindow(object):
    def setupUi(self, logWindow):
        logWindow.setObjectName(_fromUtf8("logWindow"))
        logWindow.setWindowModality(QtCore.Qt.WindowModal)
        logWindow.resize(709, 428)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/log.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        logWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(logWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonSelectDate = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSelectDate.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSelectDate.setFont(font)
        self.pushButtonSelectDate.setObjectName(_fromUtf8("pushButtonSelectDate"))
        self.horizontalLayout.addWidget(self.pushButtonSelectDate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetLogItems = QtGui.QTableWidget(self.centralwidget)
        self.tableWidgetLogItems.setStatusTip(_fromUtf8(""))
        self.tableWidgetLogItems.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetLogItems.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetLogItems.setObjectName(_fromUtf8("tableWidgetLogItems"))
        self.tableWidgetLogItems.setColumnCount(4)
        self.tableWidgetLogItems.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetLogItems.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetLogItems.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetLogItems.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetLogItems.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidgetLogItems)
        logWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(logWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        logWindow.setStatusBar(self.statusbar)

        self.retranslateUi(logWindow)
        QtCore.QMetaObject.connectSlotsByName(logWindow)

    def retranslateUi(self, logWindow):
        logWindow.setWindowTitle(_translate("logWindow", "LOG ACTIVITIES", None))
        self.pushButtonSelectDate.setStatusTip(_translate("logWindow", "Select Date", None))
        self.pushButtonSelectDate.setText(_translate("logWindow", "Select Date", None))
        self.tableWidgetLogItems.setSortingEnabled(True)
        item = self.tableWidgetLogItems.horizontalHeaderItem(0)
        item.setText(_translate("logWindow", "Sn", None))
        item = self.tableWidgetLogItems.horizontalHeaderItem(1)
        item.setText(_translate("logWindow", "Time", None))
        item = self.tableWidgetLogItems.horizontalHeaderItem(2)
        item.setText(_translate("logWindow", "Staff", None))
        item = self.tableWidgetLogItems.horizontalHeaderItem(3)
        item.setText(_translate("logWindow", "Activity", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    logWindow = QtGui.QMainWindow()
    ui = Ui_logWindow()
    ui.setupUi(logWindow)
    logWindow.show()
    sys.exit(app.exec_())

