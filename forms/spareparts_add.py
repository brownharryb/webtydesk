# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spareparts_add.ui'
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

class Ui_dialogSparepartsAdd(object):
    def setupUi(self, dialogSparepartsAdd):
        dialogSparepartsAdd.setObjectName(_fromUtf8("dialogSparepartsAdd"))
        dialogSparepartsAdd.setWindowModality(QtCore.Qt.WindowModal)
        dialogSparepartsAdd.resize(400, 256)
        dialogSparepartsAdd.setMinimumSize(QtCore.QSize(400, 256))
        dialogSparepartsAdd.setMaximumSize(QtCore.QSize(400, 256))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/headphone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogSparepartsAdd.setWindowIcon(icon)
        dialogSparepartsAdd.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(dialogSparepartsAdd)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, 50, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEditName = QtGui.QLineEdit(dialogSparepartsAdd)
        self.lineEditName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditName.setAutoFillBackground(False)
        self.lineEditName.setMaxLength(20)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.lineEditQuantity = QtGui.QLineEdit(dialogSparepartsAdd)
        self.lineEditQuantity.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditQuantity.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditQuantity.setObjectName(_fromUtf8("lineEditQuantity"))
        self.verticalLayout_2.addWidget(self.lineEditQuantity)
        self.lineEditUnitPrice = QtGui.QLineEdit(dialogSparepartsAdd)
        self.lineEditUnitPrice.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditUnitPrice.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditUnitPrice.setMaxLength(20)
        self.lineEditUnitPrice.setObjectName(_fromUtf8("lineEditUnitPrice"))
        self.verticalLayout_2.addWidget(self.lineEditUnitPrice)
        self.lineEditVendor = QtGui.QLineEdit(dialogSparepartsAdd)
        self.lineEditVendor.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditVendor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditVendor.setMaxLength(20)
        self.lineEditVendor.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEditVendor.setObjectName(_fromUtf8("lineEditVendor"))
        self.verticalLayout_2.addWidget(self.lineEditVendor)
        self.labelError = QtGui.QLabel(dialogSparepartsAdd)
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
        self.pushButtonSave = QtGui.QPushButton(dialogSparepartsAdd)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout_3.addWidget(self.pushButtonSave)
        self.pushButtonClear = QtGui.QPushButton(dialogSparepartsAdd)
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

        self.retranslateUi(dialogSparepartsAdd)
        QtCore.QMetaObject.connectSlotsByName(dialogSparepartsAdd)

    def retranslateUi(self, dialogSparepartsAdd):
        dialogSparepartsAdd.setWindowTitle(_translate("dialogSparepartsAdd", "ADD SPARE PARTS", None))
        self.lineEditName.setWhatsThis(_translate("dialogSparepartsAdd", "First Name", None))
        self.lineEditName.setPlaceholderText(_translate("dialogSparepartsAdd", "NAME", None))
        self.lineEditQuantity.setPlaceholderText(_translate("dialogSparepartsAdd", "QUANTITY(NUMBER ONLY) ", None))
        self.lineEditUnitPrice.setPlaceholderText(_translate("dialogSparepartsAdd", "UNIT PRICE (NUMBER ONLY)", None))
        self.lineEditVendor.setPlaceholderText(_translate("dialogSparepartsAdd", "VENDOR (OPTIONAL)", None))
        self.labelError.setText(_translate("dialogSparepartsAdd", "Error", None))
        self.pushButtonSave.setText(_translate("dialogSparepartsAdd", "Save", None))
        self.pushButtonClear.setText(_translate("dialogSparepartsAdd", "Clear", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogSparepartsAdd = QtGui.QDialog()
    ui = Ui_dialogSparepartsAdd()
    ui.setupUi(dialogSparepartsAdd)
    dialogSparepartsAdd.show()
    sys.exit(app.exec_())

