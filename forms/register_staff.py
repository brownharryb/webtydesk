# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_staff.ui'
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

class Ui_dialogRegisterStaff(object):
    def setupUi(self, dialogRegisterStaff):
        dialogRegisterStaff.setObjectName(_fromUtf8("dialogRegisterStaff"))
        dialogRegisterStaff.setWindowModality(QtCore.Qt.WindowModal)
        dialogRegisterStaff.resize(414, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/staff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogRegisterStaff.setWindowIcon(icon)
        dialogRegisterStaff.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(dialogRegisterStaff)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, 50, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEditName = QtGui.QLineEdit(dialogRegisterStaff)
        self.lineEditName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditName.setAutoFillBackground(False)
        self.lineEditName.setMaxLength(20)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.lineEditDesignation = QtGui.QLineEdit(dialogRegisterStaff)
        self.lineEditDesignation.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditDesignation.setObjectName(_fromUtf8("lineEditDesignation"))
        self.verticalLayout_2.addWidget(self.lineEditDesignation)
        self.lineEditUsername = QtGui.QLineEdit(dialogRegisterStaff)
        self.lineEditUsername.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditUsername.setMaxLength(20)
        self.lineEditUsername.setObjectName(_fromUtf8("lineEditUsername"))
        self.verticalLayout_2.addWidget(self.lineEditUsername)
        self.lineEditPassword1 = QtGui.QLineEdit(dialogRegisterStaff)
        self.lineEditPassword1.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword1.setMaxLength(20)
        self.lineEditPassword1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword1.setObjectName(_fromUtf8("lineEditPassword1"))
        self.verticalLayout_2.addWidget(self.lineEditPassword1)
        self.lineEditPassword2 = QtGui.QLineEdit(dialogRegisterStaff)
        self.lineEditPassword2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword2.setMaxLength(20)
        self.lineEditPassword2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword2.setObjectName(_fromUtf8("lineEditPassword2"))
        self.verticalLayout_2.addWidget(self.lineEditPassword2)
        self.labelError = QtGui.QLabel(dialogRegisterStaff)
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
        self.pushButtonSave = QtGui.QPushButton(dialogRegisterStaff)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout_3.addWidget(self.pushButtonSave)
        self.pushButtonClear = QtGui.QPushButton(dialogRegisterStaff)
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

        self.retranslateUi(dialogRegisterStaff)
        QtCore.QMetaObject.connectSlotsByName(dialogRegisterStaff)

    def retranslateUi(self, dialogRegisterStaff):
        dialogRegisterStaff.setWindowTitle(_translate("dialogRegisterStaff", "NEW STAFF", None))
        self.lineEditName.setWhatsThis(_translate("dialogRegisterStaff", "First Name", None))
        self.lineEditName.setPlaceholderText(_translate("dialogRegisterStaff", "NAME", None))
        self.lineEditDesignation.setPlaceholderText(_translate("dialogRegisterStaff", "DESIGNATION", None))
        self.lineEditUsername.setPlaceholderText(_translate("dialogRegisterStaff", "USERNAME", None))
        self.lineEditPassword1.setPlaceholderText(_translate("dialogRegisterStaff", "PASSWORD", None))
        self.lineEditPassword2.setPlaceholderText(_translate("dialogRegisterStaff", "CONFIRM PASSWORD", None))
        self.labelError.setText(_translate("dialogRegisterStaff", "Error", None))
        self.pushButtonSave.setText(_translate("dialogRegisterStaff", "Save", None))
        self.pushButtonClear.setText(_translate("dialogRegisterStaff", "Clear", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogRegisterStaff = QtGui.QDialog()
    ui = Ui_dialogRegisterStaff()
    ui.setupUi(dialogRegisterStaff)
    dialogRegisterStaff.show()
    sys.exit(app.exec_())

