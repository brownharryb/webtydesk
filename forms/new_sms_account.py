# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_sms_account.ui'
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

class Ui_dialogSmsNewAccount(object):
    def setupUi(self, dialogSmsNewAccount):
        dialogSmsNewAccount.setObjectName(_fromUtf8("dialogSmsNewAccount"))
        dialogSmsNewAccount.setWindowModality(QtCore.Qt.WindowModal)
        dialogSmsNewAccount.resize(450, 299)
        dialogSmsNewAccount.setMinimumSize(QtCore.QSize(450, 0))
        dialogSmsNewAccount.setMaximumSize(QtCore.QSize(450, 299))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/envelope_plus2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogSmsNewAccount.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dialogSmsNewAccount)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(dialogSmsNewAccount)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonVistWebsite = QtGui.QPushButton(dialogSmsNewAccount)
        self.pushButtonVistWebsite.setMaximumSize(QtCore.QSize(200, 100))
        self.pushButtonVistWebsite.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonVistWebsite.setFont(font)
        self.pushButtonVistWebsite.setCheckable(False)
        self.pushButtonVistWebsite.setObjectName(_fromUtf8("pushButtonVistWebsite"))
        self.horizontalLayout.addWidget(self.pushButtonVistWebsite)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(dialogSmsNewAccount)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditUsername = QtGui.QLineEdit(dialogSmsNewAccount)
        self.lineEditUsername.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditUsername.setObjectName(_fromUtf8("lineEditUsername"))
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.lineEditPassword1 = QtGui.QLineEdit(dialogSmsNewAccount)
        self.lineEditPassword1.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword1.setObjectName(_fromUtf8("lineEditPassword1"))
        self.verticalLayout.addWidget(self.lineEditPassword1)
        self.lineEditPassword2 = QtGui.QLineEdit(dialogSmsNewAccount)
        self.lineEditPassword2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword2.setObjectName(_fromUtf8("lineEditPassword2"))
        self.verticalLayout.addWidget(self.lineEditPassword2)
        self.labelError = QtGui.QLabel(dialogSmsNewAccount)
        self.labelError.setStyleSheet(_fromUtf8("#labelError{color:#FF2525}"))
        self.labelError.setObjectName(_fromUtf8("labelError"))
        self.verticalLayout.addWidget(self.labelError)
        self.progressBarConfirming = QtGui.QProgressBar(dialogSmsNewAccount)
        self.progressBarConfirming.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBarConfirming.setProperty("value", 24)
        self.progressBarConfirming.setTextVisible(False)
        self.progressBarConfirming.setObjectName(_fromUtf8("progressBarConfirming"))
        self.verticalLayout.addWidget(self.progressBarConfirming)
        self.labelConfirming = QtGui.QLabel(dialogSmsNewAccount)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelConfirming.setFont(font)
        self.labelConfirming.setStyleSheet(_fromUtf8(""))
        self.labelConfirming.setObjectName(_fromUtf8("labelConfirming"))
        self.verticalLayout.addWidget(self.labelConfirming)
        self.senderIdLayout = QtGui.QHBoxLayout()
        self.senderIdLayout.setObjectName(_fromUtf8("senderIdLayout"))
        self.labelSenderId = QtGui.QLabel(dialogSmsNewAccount)
        self.labelSenderId.setObjectName(_fromUtf8("labelSenderId"))
        self.senderIdLayout.addWidget(self.labelSenderId)
        self.lineEditSenderId = QtGui.QLineEdit(dialogSmsNewAccount)
        self.lineEditSenderId.setStyleSheet(_fromUtf8(""))
        self.lineEditSenderId.setMaxLength(10)
        self.lineEditSenderId.setObjectName(_fromUtf8("lineEditSenderId"))
        self.senderIdLayout.addWidget(self.lineEditSenderId)
        self.verticalLayout.addLayout(self.senderIdLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonActivate = QtGui.QPushButton(dialogSmsNewAccount)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(7)
        self.pushButtonActivate.setFont(font)
        self.pushButtonActivate.setObjectName(_fromUtf8("pushButtonActivate"))
        self.horizontalLayout_2.addWidget(self.pushButtonActivate)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonSave = QtGui.QPushButton(dialogSmsNewAccount)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout_2.addWidget(self.pushButtonSave)
        self.pushButtonCancel = QtGui.QPushButton(dialogSmsNewAccount)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialogSmsNewAccount)
        QtCore.QMetaObject.connectSlotsByName(dialogSmsNewAccount)

    def retranslateUi(self, dialogSmsNewAccount):
        dialogSmsNewAccount.setWindowTitle(_translate("dialogSmsNewAccount", "NEW SMS ACCOUNT", None))
        self.label.setText(_translate("dialogSmsNewAccount", "PLEASE CLICK BELOW TO REGISTER NEW ACCOUNT.", None))
        self.pushButtonVistWebsite.setText(_translate("dialogSmsNewAccount", "Register on Website", None))
        self.label_2.setText(_translate("dialogSmsNewAccount", "AFTER REGISTRATION FILL THE FORM AND SAVE", None))
        self.lineEditUsername.setPlaceholderText(_translate("dialogSmsNewAccount", "USERNAME", None))
        self.lineEditPassword1.setPlaceholderText(_translate("dialogSmsNewAccount", "PASSWORD", None))
        self.lineEditPassword2.setPlaceholderText(_translate("dialogSmsNewAccount", "CONFIRM PASSWORD", None))
        self.labelError.setText(_translate("dialogSmsNewAccount", "TextLabel", None))
        self.labelConfirming.setText(_translate("dialogSmsNewAccount", "TextLabel", None))
        self.labelSenderId.setText(_translate("dialogSmsNewAccount", "Sender Id", None))
        self.lineEditSenderId.setText(_translate("dialogSmsNewAccount", "WEBTY .S", None))
        self.pushButtonActivate.setText(_translate("dialogSmsNewAccount", "ACTIVATE", None))
        self.pushButtonSave.setText(_translate("dialogSmsNewAccount", "SAVE", None))
        self.pushButtonCancel.setText(_translate("dialogSmsNewAccount", "CANCEL", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogSmsNewAccount = QtGui.QDialog()
    ui = Ui_dialogSmsNewAccount()
    ui.setupUi(dialogSmsNewAccount)
    dialogSmsNewAccount.show()
    sys.exit(app.exec_())

