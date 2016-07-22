# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_login.ui'
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

class Ui_dialogDbLogin(object):
    def setupUi(self, dialogDbLogin):
        dialogDbLogin.setObjectName(_fromUtf8("dialogDbLogin"))
        dialogDbLogin.setWindowModality(QtCore.Qt.WindowModal)
        dialogDbLogin.resize(368, 120)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/database.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogDbLogin.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dialogDbLogin)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEditUsername = QtGui.QLineEdit(dialogDbLogin)
        self.lineEditUsername.setObjectName(_fromUtf8("lineEditUsername"))
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.lineEditPassword = QtGui.QLineEdit(dialogDbLogin)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.labelError = QtGui.QLabel(dialogDbLogin)
        self.labelError.setStyleSheet(_fromUtf8("#labelError{color: rgb(255, 0, 0);}"))
        self.labelError.setObjectName(_fromUtf8("labelError"))
        self.verticalLayout.addWidget(self.labelError)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonLogin = QtGui.QPushButton(dialogDbLogin)
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonCancel = QtGui.QPushButton(dialogDbLogin)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialogDbLogin)
        QtCore.QMetaObject.connectSlotsByName(dialogDbLogin)

    def retranslateUi(self, dialogDbLogin):
        dialogDbLogin.setWindowTitle(_translate("dialogDbLogin", "DATABASE LOGIN", None))
        self.lineEditUsername.setPlaceholderText(_translate("dialogDbLogin", "Database Username", None))
        self.lineEditPassword.setPlaceholderText(_translate("dialogDbLogin", "Database Password", None))
        self.labelError.setText(_translate("dialogDbLogin", "Invalid Username or Password", None))
        self.pushButtonLogin.setText(_translate("dialogDbLogin", "Login", None))
        self.pushButtonCancel.setText(_translate("dialogDbLogin", "Cancel", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogDbLogin = QtGui.QDialog()
    ui = Ui_dialogDbLogin()
    ui.setupUi(dialogDbLogin)
    dialogDbLogin.show()
    sys.exit(app.exec_())

