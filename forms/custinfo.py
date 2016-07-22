# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cust_info.ui'
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

class Ui_custInfoWindow(object):
    def setupUi(self, custInfoWindow):
        custInfoWindow.setObjectName(_fromUtf8("custInfoWindow"))
        custInfoWindow.setWindowModality(QtCore.Qt.WindowModal)
        custInfoWindow.resize(950, 430)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(custInfoWindow.sizePolicy().hasHeightForWidth())
        custInfoWindow.setSizePolicy(sizePolicy)
        custInfoWindow.setMinimumSize(QtCore.QSize(950, 430))
        custInfoWindow.setMaximumSize(QtCore.QSize(950, 430))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/add.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        custInfoWindow.setWindowIcon(icon)
        custInfoWindow.setStyleSheet(_fromUtf8("#custInfoWindow\n"
"{border-image: url(:/backgrounds/images/backgounds/_8.jpg);\n"
"}"))
        self.centralwidget = QtGui.QWidget(custInfoWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEditName = QtGui.QLineEdit(self.groupBox)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditMobileNumber = QtGui.QLineEdit(self.groupBox)
        self.lineEditMobileNumber.setObjectName(_fromUtf8("lineEditMobileNumber"))
        self.horizontalLayout_2.addWidget(self.lineEditMobileNumber)
        self.lineEditMobileNumber_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEditMobileNumber_2.setObjectName(_fromUtf8("lineEditMobileNumber_2"))
        self.horizontalLayout_2.addWidget(self.lineEditMobileNumber_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidgetAddedItems = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetAddedItems.setEnabled(False)
        self.tableWidgetAddedItems.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidgetAddedItems.setObjectName(_fromUtf8("tableWidgetAddedItems"))
        self.tableWidgetAddedItems.setColumnCount(9)
        self.tableWidgetAddedItems.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddedItems.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.tableWidgetAddedItems)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBoxNumberToDelete = QtGui.QComboBox(self.centralwidget)
        self.comboBoxNumberToDelete.setEnabled(False)
        self.comboBoxNumberToDelete.setObjectName(_fromUtf8("comboBoxNumberToDelete"))
        self.horizontalLayout.addWidget(self.comboBoxNumberToDelete)
        self.pushButtonDeleteItem = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDeleteItem.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDeleteItem.setIcon(icon1)
        self.pushButtonDeleteItem.setObjectName(_fromUtf8("pushButtonDeleteItem"))
        self.horizontalLayout.addWidget(self.pushButtonDeleteItem)
        self.pushButtonAddnew = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAddnew.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/plus.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddnew.setIcon(icon2)
        self.pushButtonAddnew.setObjectName(_fromUtf8("pushButtonAddnew"))
        self.horizontalLayout.addWidget(self.pushButtonAddnew)
        self.pushButtonSave = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSave.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSave.setIcon(icon3)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        custInfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(custInfoWindow)
        self.statusbar.setStyleSheet(_fromUtf8(""))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        custInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(custInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(custInfoWindow)

    def retranslateUi(self, custInfoWindow):
        custInfoWindow.setWindowTitle(_translate("custInfoWindow", "ADD NEW CUSTOMER AND REPAIR JOB", None))
        self.groupBox.setTitle(_translate("custInfoWindow", "Customer info", None))
        self.lineEditName.setStatusTip(_translate("custInfoWindow", "Customer Name", None))
        self.lineEditName.setPlaceholderText(_translate("custInfoWindow", "Name", None))
        self.lineEditMobileNumber.setStatusTip(_translate("custInfoWindow", "Customer Mobile Number", None))
        self.lineEditMobileNumber.setPlaceholderText(_translate("custInfoWindow", "Mobile 1", None))
        self.lineEditMobileNumber_2.setPlaceholderText(_translate("custInfoWindow", "Mobile 2 (Optional)", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(0)
        item.setText(_translate("custInfoWindow", "MAKE&MODEL", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(1)
        item.setText(_translate("custInfoWindow", "KNOWN FAULTS", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(2)
        item.setText(_translate("custInfoWindow", "BILL", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(3)
        item.setText(_translate("custInfoWindow", "PAID", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(4)
        item.setText(_translate("custInfoWindow", "STATUS", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(5)
        item.setText(_translate("custInfoWindow", "DATE IN", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(6)
        item.setText(_translate("custInfoWindow", "DATE OUT", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(7)
        item.setText(_translate("custInfoWindow", "IMEI/SERIAL NO", None))
        item = self.tableWidgetAddedItems.horizontalHeaderItem(8)
        item.setText(_translate("custInfoWindow", "OTHER INFO", None))
        self.comboBoxNumberToDelete.setStatusTip(_translate("custInfoWindow", "Select Item to delete", None))
        self.pushButtonDeleteItem.setStatusTip(_translate("custInfoWindow", "Delete Selected Item", None))
        self.pushButtonAddnew.setStatusTip(_translate("custInfoWindow", "Add new job", None))
        self.pushButtonSave.setStatusTip(_translate("custInfoWindow", "Save", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    custInfoWindow = QtGui.QMainWindow()
    ui = Ui_custInfoWindow()
    ui.setupUi(custInfoWindow)
    custInfoWindow.show()
    sys.exit(app.exec_())

