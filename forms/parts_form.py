# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parts_form.ui'
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

class Ui_dialogSpareParts(object):
    def setupUi(self, dialogSpareParts):
        dialogSpareParts.setObjectName(_fromUtf8("dialogSpareParts"))
        dialogSpareParts.setWindowModality(QtCore.Qt.WindowModal)
        dialogSpareParts.resize(754, 432)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/headphone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogSpareParts.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dialogSpareParts)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEditSearchText = QtGui.QLineEdit(dialogSpareParts)
        self.lineEditSearchText.setObjectName(_fromUtf8("lineEditSearchText"))
        self.verticalLayout.addWidget(self.lineEditSearchText)
        self.tableWidgetAllParts = QtGui.QTableWidget(dialogSpareParts)
        self.tableWidgetAllParts.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetAllParts.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetAllParts.setObjectName(_fromUtf8("tableWidgetAllParts"))
        self.tableWidgetAllParts.setColumnCount(5)
        self.tableWidgetAllParts.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllParts.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllParts.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllParts.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllParts.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllParts.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidgetAllParts)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBoxPrice = QtGui.QCheckBox(dialogSpareParts)
        self.checkBoxPrice.setObjectName(_fromUtf8("checkBoxPrice"))
        self.horizontalLayout.addWidget(self.checkBoxPrice)
        self.checkBoxQuantity = QtGui.QCheckBox(dialogSpareParts)
        self.checkBoxQuantity.setObjectName(_fromUtf8("checkBoxQuantity"))
        self.horizontalLayout.addWidget(self.checkBoxQuantity)
        self.checkBoxVendor = QtGui.QCheckBox(dialogSpareParts)
        self.checkBoxVendor.setObjectName(_fromUtf8("checkBoxVendor"))
        self.horizontalLayout.addWidget(self.checkBoxVendor)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(dialogSpareParts)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditQuantityUsed = QtGui.QLineEdit(dialogSpareParts)
        self.lineEditQuantityUsed.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditQuantityUsed.setBaseSize(QtCore.QSize(0, 0))
        self.lineEditQuantityUsed.setMaxLength(3)
        self.lineEditQuantityUsed.setObjectName(_fromUtf8("lineEditQuantityUsed"))
        self.horizontalLayout.addWidget(self.lineEditQuantityUsed)
        self.pushButtonDeduct = QtGui.QPushButton(dialogSpareParts)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDeduct.setFont(font)
        self.pushButtonDeduct.setObjectName(_fromUtf8("pushButtonDeduct"))
        self.horizontalLayout.addWidget(self.pushButtonDeduct)
        self.pushButtonCancel = QtGui.QPushButton(dialogSpareParts)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialogSpareParts)
        QtCore.QMetaObject.connectSlotsByName(dialogSpareParts)

    def retranslateUi(self, dialogSpareParts):
        dialogSpareParts.setWindowTitle(_translate("dialogSpareParts", "SPARES AND ACCESSORIES", None))
        item = self.tableWidgetAllParts.horizontalHeaderItem(0)
        item.setText(_translate("dialogSpareParts", "Id", None))
        item = self.tableWidgetAllParts.horizontalHeaderItem(1)
        item.setText(_translate("dialogSpareParts", "Name", None))
        item = self.tableWidgetAllParts.horizontalHeaderItem(2)
        item.setText(_translate("dialogSpareParts", "Unit Price", None))
        item = self.tableWidgetAllParts.horizontalHeaderItem(3)
        item.setText(_translate("dialogSpareParts", "Quantity", None))
        item = self.tableWidgetAllParts.horizontalHeaderItem(4)
        item.setText(_translate("dialogSpareParts", "Vendor", None))
        self.checkBoxPrice.setText(_translate("dialogSpareParts", "Price", None))
        self.checkBoxQuantity.setText(_translate("dialogSpareParts", "Quantity", None))
        self.checkBoxVendor.setText(_translate("dialogSpareParts", "Vendor", None))
        self.label.setText(_translate("dialogSpareParts", "Specify Quantity Used Up", None))
        self.pushButtonDeduct.setText(_translate("dialogSpareParts", "Deduct", None))
        self.pushButtonCancel.setText(_translate("dialogSpareParts", "Cancel", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogSpareParts = QtGui.QDialog()
    ui = Ui_dialogSpareParts()
    ui.setupUi(dialogSpareParts)
    dialogSpareParts.show()
    sys.exit(app.exec_())

