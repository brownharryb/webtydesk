# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_send_message.ui'
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

class Ui_dialodGroupSmsAdd(object):
    def setupUi(self, dialodGroupSmsAdd):
        dialodGroupSmsAdd.setObjectName(_fromUtf8("dialodGroupSmsAdd"))
        dialodGroupSmsAdd.setWindowModality(QtCore.Qt.WindowModal)
        dialodGroupSmsAdd.resize(600, 400)
        dialodGroupSmsAdd.setMinimumSize(QtCore.QSize(600, 400))
        dialodGroupSmsAdd.setMaximumSize(QtCore.QSize(600, 400))
        self.verticalLayout = QtGui.QVBoxLayout(dialodGroupSmsAdd)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonAddCustomers = QtGui.QPushButton(dialodGroupSmsAdd)
        self.pushButtonAddCustomers.setObjectName(_fromUtf8("pushButtonAddCustomers"))
        self.horizontalLayout_2.addWidget(self.pushButtonAddCustomers)
        self.pushButtonAddCsv = QtGui.QPushButton(dialodGroupSmsAdd)
        self.pushButtonAddCsv.setObjectName(_fromUtf8("pushButtonAddCsv"))
        self.horizontalLayout_2.addWidget(self.pushButtonAddCsv)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidgetNumbers = QtGui.QTableWidget(dialodGroupSmsAdd)
        self.tableWidgetNumbers.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidgetNumbers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetNumbers.setObjectName(_fromUtf8("tableWidgetNumbers"))
        self.tableWidgetNumbers.setColumnCount(3)
        self.tableWidgetNumbers.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetNumbers.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetNumbers.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetNumbers.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidgetNumbers)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelNumberOfPeople = QtGui.QLabel(dialodGroupSmsAdd)
        self.labelNumberOfPeople.setObjectName(_fromUtf8("labelNumberOfPeople"))
        self.horizontalLayout.addWidget(self.labelNumberOfPeople)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonUpdateToMain = QtGui.QPushButton(dialodGroupSmsAdd)
        self.pushButtonUpdateToMain.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUpdateToMain.setIcon(icon)
        self.pushButtonUpdateToMain.setObjectName(_fromUtf8("pushButtonUpdateToMain"))
        self.horizontalLayout.addWidget(self.pushButtonUpdateToMain)
        self.pushButtonDelete = QtGui.QPushButton(dialodGroupSmsAdd)
        self.pushButtonDelete.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDelete.setIcon(icon1)
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialodGroupSmsAdd)
        QtCore.QMetaObject.connectSlotsByName(dialodGroupSmsAdd)

    def retranslateUi(self, dialodGroupSmsAdd):
        dialodGroupSmsAdd.setWindowTitle(_translate("dialodGroupSmsAdd", "Group Sms", None))
        self.pushButtonAddCustomers.setText(_translate("dialodGroupSmsAdd", "All Customers", None))
        self.pushButtonAddCsv.setText(_translate("dialodGroupSmsAdd", "Outlook CSV", None))
        item = self.tableWidgetNumbers.horizontalHeaderItem(0)
        item.setText(_translate("dialodGroupSmsAdd", "Name", None))
        item = self.tableWidgetNumbers.horizontalHeaderItem(1)
        item.setText(_translate("dialodGroupSmsAdd", "Number", None))
        item = self.tableWidgetNumbers.horizontalHeaderItem(2)
        item.setText(_translate("dialodGroupSmsAdd", "Number2", None))
        self.labelNumberOfPeople.setText(_translate("dialodGroupSmsAdd", "0", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialodGroupSmsAdd = QtGui.QDialog()
    ui = Ui_dialodGroupSmsAdd()
    ui.setupUi(dialodGroupSmsAdd)
    dialodGroupSmsAdd.show()
    sys.exit(app.exec_())

