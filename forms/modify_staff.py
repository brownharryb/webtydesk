# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_staff.ui'
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

class Ui_dialogModifyStaff(object):
    def setupUi(self, dialogModifyStaff):
        dialogModifyStaff.setObjectName(_fromUtf8("dialogModifyStaff"))
        dialogModifyStaff.setWindowModality(QtCore.Qt.WindowModal)
        dialogModifyStaff.resize(420, 330)
        dialogModifyStaff.setMinimumSize(QtCore.QSize(420, 330))
        dialogModifyStaff.setMaximumSize(QtCore.QSize(420, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/edit_staff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogModifyStaff.setWindowIcon(icon)
        dialogModifyStaff.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(dialogModifyStaff)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, 50, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBoxAllStaffUsername = QtGui.QComboBox(dialogModifyStaff)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxAllStaffUsername.setFont(font)
        self.comboBoxAllStaffUsername.setObjectName(_fromUtf8("comboBoxAllStaffUsername"))
        self.comboBoxAllStaffUsername.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBoxAllStaffUsername)
        self.labelDbId = QtGui.QLabel(dialogModifyStaff)
        self.labelDbId.setObjectName(_fromUtf8("labelDbId"))
        self.verticalLayout_2.addWidget(self.labelDbId)
        self.lineEditName = QtGui.QLineEdit(dialogModifyStaff)
        self.lineEditName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditName.setAutoFillBackground(False)
        self.lineEditName.setMaxLength(20)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.lineEditDesignation = QtGui.QLineEdit(dialogModifyStaff)
        self.lineEditDesignation.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditDesignation.setObjectName(_fromUtf8("lineEditDesignation"))
        self.verticalLayout_2.addWidget(self.lineEditDesignation)
        self.lineEditUsername = QtGui.QLineEdit(dialogModifyStaff)
        self.lineEditUsername.setEnabled(False)
        self.lineEditUsername.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditUsername.setMaxLength(20)
        self.lineEditUsername.setObjectName(_fromUtf8("lineEditUsername"))
        self.verticalLayout_2.addWidget(self.lineEditUsername)
        self.lineEditPassword1 = QtGui.QLineEdit(dialogModifyStaff)
        self.lineEditPassword1.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword1.setMaxLength(20)
        self.lineEditPassword1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword1.setObjectName(_fromUtf8("lineEditPassword1"))
        self.verticalLayout_2.addWidget(self.lineEditPassword1)
        self.lineEditPassword2 = QtGui.QLineEdit(dialogModifyStaff)
        self.lineEditPassword2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword2.setMaxLength(20)
        self.lineEditPassword2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword2.setObjectName(_fromUtf8("lineEditPassword2"))
        self.verticalLayout_2.addWidget(self.lineEditPassword2)
        self.lineEditSmsCredits = QtGui.QLineEdit(dialogModifyStaff)
        self.lineEditSmsCredits.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditSmsCredits.setObjectName(_fromUtf8("lineEditSmsCredits"))
        self.verticalLayout_2.addWidget(self.lineEditSmsCredits)
        self.labelError = QtGui.QLabel(dialogModifyStaff)
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
        self.pushButtonDelete = QtGui.QPushButton(dialogModifyStaff)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.horizontalLayout_3.addWidget(self.pushButtonDelete)
        self.pushButtonSave = QtGui.QPushButton(dialogModifyStaff)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout_3.addWidget(self.pushButtonSave)
        self.pushButtonClear = QtGui.QPushButton(dialogModifyStaff)
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

        self.retranslateUi(dialogModifyStaff)
        QtCore.QMetaObject.connectSlotsByName(dialogModifyStaff)

    def retranslateUi(self, dialogModifyStaff):
        dialogModifyStaff.setWindowTitle(_translate("dialogModifyStaff", "MODIFY STAFF", None))
        self.comboBoxAllStaffUsername.setItemText(0, _translate("dialogModifyStaff", "Select Staff", None))
        self.labelDbId.setText(_translate("dialogModifyStaff", "TextLabel", None))
        self.lineEditName.setWhatsThis(_translate("dialogModifyStaff", "First Name", None))
        self.lineEditName.setPlaceholderText(_translate("dialogModifyStaff", "NAME", None))
        self.lineEditDesignation.setPlaceholderText(_translate("dialogModifyStaff", "DESIGNATION", None))
        self.lineEditUsername.setPlaceholderText(_translate("dialogModifyStaff", "USERNAME", None))
        self.lineEditPassword1.setPlaceholderText(_translate("dialogModifyStaff", "PASSWORD", None))
        self.lineEditPassword2.setPlaceholderText(_translate("dialogModifyStaff", "CONFIRM PASSWORD", None))
        self.lineEditSmsCredits.setPlaceholderText(_translate("dialogModifyStaff", "SMS CREDIT (NUMBER ONLY)", None))
        self.labelError.setText(_translate("dialogModifyStaff", "Error", None))
        self.pushButtonDelete.setText(_translate("dialogModifyStaff", "Delete", None))
        self.pushButtonSave.setText(_translate("dialogModifyStaff", "Update", None))
        self.pushButtonClear.setText(_translate("dialogModifyStaff", "Clear", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogModifyStaff = QtGui.QDialog()
    ui = Ui_dialogModifyStaff()
    ui.setupUi(dialogModifyStaff)
    dialogModifyStaff.show()
    sys.exit(app.exec_())

