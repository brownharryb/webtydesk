# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transact_options.ui'
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

class Ui_dialogTransaction(object):
    def setupUi(self, dialogTransaction):
        dialogTransaction.setObjectName(_fromUtf8("dialogTransaction"))
        dialogTransaction.setWindowModality(QtCore.Qt.WindowModal)
        dialogTransaction.resize(510, 132)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/naira.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogTransaction.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dialogTransaction)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSpend = QtGui.QPushButton(dialogTransaction)
        self.pushButtonSpend.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSpend.setFont(font)
        self.pushButtonSpend.setObjectName(_fromUtf8("pushButtonSpend"))
        self.horizontalLayout.addWidget(self.pushButtonSpend)
        self.pushButtonReceive = QtGui.QPushButton(dialogTransaction)
        self.pushButtonReceive.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonReceive.setFont(font)
        self.pushButtonReceive.setObjectName(_fromUtf8("pushButtonReceive"))
        self.horizontalLayout.addWidget(self.pushButtonReceive)
        self.pushButtonFixed = QtGui.QPushButton(dialogTransaction)
        self.pushButtonFixed.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFixed.setFont(font)
        self.pushButtonFixed.setObjectName(_fromUtf8("pushButtonFixed"))
        self.horizontalLayout.addWidget(self.pushButtonFixed)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialogTransaction)
        QtCore.QMetaObject.connectSlotsByName(dialogTransaction)

    def retranslateUi(self, dialogTransaction):
        dialogTransaction.setWindowTitle(_translate("dialogTransaction", "TRANSACTION", None))
        self.pushButtonSpend.setText(_translate("dialogTransaction", "SPEND", None))
        self.pushButtonReceive.setText(_translate("dialogTransaction", "RECEIVE", None))
        self.pushButtonFixed.setText(_translate("dialogTransaction", "FIXED ITEMS", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogTransaction = QtGui.QDialog()
    ui = Ui_dialogTransaction()
    ui.setupUi(dialogTransaction)
    dialogTransaction.show()
    sys.exit(app.exec_())

