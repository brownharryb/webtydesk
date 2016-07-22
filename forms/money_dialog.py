# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'money_dialog.ui'
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

class Ui_dialogMoney(object):
    def setupUi(self, dialogMoney):
        dialogMoney.setObjectName(_fromUtf8("dialogMoney"))
        dialogMoney.resize(367, 288)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/naira.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogMoney.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dialogMoney)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(dialogMoney)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEditAmount = QtGui.QLineEdit(dialogMoney)
        self.lineEditAmount.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditAmount.setObjectName(_fromUtf8("lineEditAmount"))
        self.verticalLayout.addWidget(self.lineEditAmount)
        self.groupBox = QtGui.QGroupBox(dialogMoney)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textEditPurpose = QtGui.QTextEdit(self.groupBox)
        self.textEditPurpose.setObjectName(_fromUtf8("textEditPurpose"))
        self.horizontalLayout_2.addWidget(self.textEditPurpose)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, 0, 50, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButtonCash = QtGui.QRadioButton(dialogMoney)
        self.radioButtonCash.setChecked(True)
        self.radioButtonCash.setObjectName(_fromUtf8("radioButtonCash"))
        self.horizontalLayout_3.addWidget(self.radioButtonCash)
        self.radioButtonPos = QtGui.QRadioButton(dialogMoney)
        self.radioButtonPos.setObjectName(_fromUtf8("radioButtonPos"))
        self.horizontalLayout_3.addWidget(self.radioButtonPos)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonSave = QtGui.QPushButton(dialogMoney)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonCancel = QtGui.QPushButton(dialogMoney)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialogMoney)
        QtCore.QMetaObject.connectSlotsByName(dialogMoney)

    def retranslateUi(self, dialogMoney):
        dialogMoney.setWindowTitle(_translate("dialogMoney", "Dialog", None))
        self.label.setText(_translate("dialogMoney", "Amount (Number Only)", None))
        self.lineEditAmount.setPlaceholderText(_translate("dialogMoney", "AMOUNT (NUMBER ONLY)", None))
        self.groupBox.setTitle(_translate("dialogMoney", "Purpose", None))
        self.radioButtonCash.setText(_translate("dialogMoney", "CASH", None))
        self.radioButtonPos.setText(_translate("dialogMoney", "POS", None))
        self.pushButtonSave.setText(_translate("dialogMoney", "Save", None))
        self.pushButtonCancel.setText(_translate("dialogMoney", "Cancel", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogMoney = QtGui.QDialog()
    ui = Ui_dialogMoney()
    ui.setupUi(dialogMoney)
    dialogMoney.show()
    sys.exit(app.exec_())

