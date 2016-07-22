# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_dialogLogin(object):
    def setupUi(self, dialogLogin):
        dialogLogin.setObjectName(_fromUtf8("dialogLogin"))
        dialogLogin.setWindowModality(QtCore.Qt.WindowModal)
        dialogLogin.resize(300, 150)
        dialogLogin.setMinimumSize(QtCore.QSize(300, 150))
        dialogLogin.setMaximumSize(QtCore.QSize(300, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogLogin.setWindowIcon(icon)
        dialogLogin.setStyleSheet(_fromUtf8(""))
        dialogLogin.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(dialogLogin)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEditLoginUsername = QtGui.QLineEdit(dialogLogin)
        self.lineEditLoginUsername.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditLoginUsername.setStatusTip(_fromUtf8(""))
        self.lineEditLoginUsername.setMaxLength(20)
        self.lineEditLoginUsername.setObjectName(_fromUtf8("lineEditLoginUsername"))
        self.verticalLayout.addWidget(self.lineEditLoginUsername)
        self.lineEditLoginPassword = QtGui.QLineEdit(dialogLogin)
        self.lineEditLoginPassword.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditLoginPassword.setMaxLength(30)
        self.lineEditLoginPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditLoginPassword.setObjectName(_fromUtf8("lineEditLoginPassword"))
        self.verticalLayout.addWidget(self.lineEditLoginPassword)
        self.labelInvalidLogin = QtGui.QLabel(dialogLogin)
        self.labelInvalidLogin.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.labelInvalidLogin.setFont(font)
        self.labelInvalidLogin.setStyleSheet(_fromUtf8("#labelInvalidLogin{\n"
"color:#FF2525;\n"
"}"))
        self.labelInvalidLogin.setObjectName(_fromUtf8("labelInvalidLogin"))
        self.verticalLayout.addWidget(self.labelInvalidLogin)
        self.progressBarLogin = QtGui.QProgressBar(dialogLogin)
        self.progressBarLogin.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBarLogin.setProperty("value", 24)
        self.progressBarLogin.setTextVisible(False)
        self.progressBarLogin.setObjectName(_fromUtf8("progressBarLogin"))
        self.verticalLayout.addWidget(self.progressBarLogin)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonLogin = QtGui.QPushButton(dialogLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLogin.sizePolicy().hasHeightForWidth())
        self.pushButtonLogin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))
        self.horizontalLayout_2.addWidget(self.pushButtonLogin)
        self.pushButtonClear = QtGui.QPushButton(dialogLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClear.sizePolicy().hasHeightForWidth())
        self.pushButtonClear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(dialogLogin)
        QtCore.QMetaObject.connectSlotsByName(dialogLogin)

    def retranslateUi(self, dialogLogin):
        dialogLogin.setWindowTitle(_translate("dialogLogin", "LOGIN", None))
        self.lineEditLoginUsername.setPlaceholderText(_translate("dialogLogin", "USERNAME", None))
        self.lineEditLoginPassword.setPlaceholderText(_translate("dialogLogin", "PASSWORD", None))
        self.labelInvalidLogin.setText(_translate("dialogLogin", "Invalid username or password!!", None))
        self.pushButtonLogin.setText(_translate("dialogLogin", "LOGIN", None))
        self.pushButtonClear.setText(_translate("dialogLogin", "CLEAR", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogLogin = QtGui.QDialog()
    ui = Ui_dialogLogin()
    ui.setupUi(dialogLogin)
    dialogLogin.show()
    sys.exit(app.exec_())

