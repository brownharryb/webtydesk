# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spareparts_check.ui'
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

class Ui_dialogSparepartsCheck(object):
    def setupUi(self, dialogSparepartsCheck):
        dialogSparepartsCheck.setObjectName(_fromUtf8("dialogSparepartsCheck"))
        dialogSparepartsCheck.setWindowModality(QtCore.Qt.WindowModal)
        dialogSparepartsCheck.resize(400, 256)
        dialogSparepartsCheck.setMinimumSize(QtCore.QSize(400, 256))
        dialogSparepartsCheck.setMaximumSize(QtCore.QSize(400, 256))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/headphone_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogSparepartsCheck.setWindowIcon(icon)
        dialogSparepartsCheck.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(dialogSparepartsCheck)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, 50, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBoxSpareParts = QtGui.QComboBox(dialogSparepartsCheck)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxSpareParts.setFont(font)
        self.comboBoxSpareParts.setObjectName(_fromUtf8("comboBoxSpareParts"))
        self.comboBoxSpareParts.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBoxSpareParts)
        self.labelDbId = QtGui.QLabel(dialogSparepartsCheck)
        self.labelDbId.setObjectName(_fromUtf8("labelDbId"))
        self.verticalLayout_2.addWidget(self.labelDbId)
        self.lineEditQtyRemaining = QtGui.QLineEdit(dialogSparepartsCheck)
        self.lineEditQtyRemaining.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditQtyRemaining.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditQtyRemaining.setObjectName(_fromUtf8("lineEditQtyRemaining"))
        self.verticalLayout_2.addWidget(self.lineEditQtyRemaining)
        self.lineEditUnitPrice = QtGui.QLineEdit(dialogSparepartsCheck)
        self.lineEditUnitPrice.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditUnitPrice.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditUnitPrice.setMaxLength(20)
        self.lineEditUnitPrice.setObjectName(_fromUtf8("lineEditUnitPrice"))
        self.verticalLayout_2.addWidget(self.lineEditUnitPrice)
        self.lineEditVendor = QtGui.QLineEdit(dialogSparepartsCheck)
        self.lineEditVendor.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditVendor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditVendor.setMaxLength(20)
        self.lineEditVendor.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEditVendor.setObjectName(_fromUtf8("lineEditVendor"))
        self.verticalLayout_2.addWidget(self.lineEditVendor)
        self.labelError = QtGui.QLabel(dialogSparepartsCheck)
        self.labelError.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet(_fromUtf8("#labelError{color:#FF2525;}"))
        self.labelError.setObjectName(_fromUtf8("labelError"))
        self.verticalLayout_2.addWidget(self.labelError)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButtonUpdate = QtGui.QPushButton(dialogSparepartsCheck)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdate.setFont(font)
        self.pushButtonUpdate.setObjectName(_fromUtf8("pushButtonUpdate"))
        self.horizontalLayout_3.addWidget(self.pushButtonUpdate)
        self.pushButtonClear = QtGui.QPushButton(dialogSparepartsCheck)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.horizontalLayout_3.addWidget(self.pushButtonClear)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(dialogSparepartsCheck)
        QtCore.QMetaObject.connectSlotsByName(dialogSparepartsCheck)

    def retranslateUi(self, dialogSparepartsCheck):
        dialogSparepartsCheck.setWindowTitle(_translate("dialogSparepartsCheck", "CHECK SPARE PARTS", None))
        self.comboBoxSpareParts.setItemText(0, _translate("dialogSparepartsCheck", "Select", None))
        self.labelDbId.setText(_translate("dialogSparepartsCheck", "TextLabel", None))
        self.lineEditQtyRemaining.setPlaceholderText(_translate("dialogSparepartsCheck", "QUANTITY REMAINING", None))
        self.lineEditUnitPrice.setPlaceholderText(_translate("dialogSparepartsCheck", "UNIT PRICE", None))
        self.lineEditVendor.setPlaceholderText(_translate("dialogSparepartsCheck", "VENDOR", None))
        self.labelError.setText(_translate("dialogSparepartsCheck", "Error", None))
        self.pushButtonUpdate.setText(_translate("dialogSparepartsCheck", "Update", None))
        self.pushButtonClear.setText(_translate("dialogSparepartsCheck", "Clear", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogSparepartsCheck = QtGui.QDialog()
    ui = Ui_dialogSparepartsCheck()
    ui.setupUi(dialogSparepartsCheck)
    dialogSparepartsCheck.show()
    sys.exit(app.exec_())

