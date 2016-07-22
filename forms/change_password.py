# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_password_staff.ui'
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

class Ui_dialogChangePassStaff(object):
    def setupUi(self, dialogChangePassStaff):
        dialogChangePassStaff.setObjectName(_fromUtf8("dialogChangePassStaff"))
        dialogChangePassStaff.setWindowModality(QtCore.Qt.WindowModal)
        dialogChangePassStaff.resize(366, 165)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogChangePassStaff.setWindowIcon(icon)
        dialogChangePassStaff.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(dialogChangePassStaff)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox = QtGui.QComboBox(dialogChangePassStaff)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBox)
        self.lineEditPassword1 = QtGui.QLineEdit(dialogChangePassStaff)
        self.lineEditPassword1.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword1.setMaxLength(20)
        self.lineEditPassword1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword1.setObjectName(_fromUtf8("lineEditPassword1"))
        self.verticalLayout_2.addWidget(self.lineEditPassword1)
        self.lineEditPassword2 = QtGui.QLineEdit(dialogChangePassStaff)
        self.lineEditPassword2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword2.setMaxLength(20)
        self.lineEditPassword2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword2.setObjectName(_fromUtf8("lineEditPassword2"))
        self.verticalLayout_2.addWidget(self.lineEditPassword2)
        self.labelPasswordError = QtGui.QLabel(dialogChangePassStaff)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelPasswordError.setFont(font)
        self.labelPasswordError.setStyleSheet(_fromUtf8("#labelPasswordError{\n"
"color:#FF2525;\n"
"}"))
        self.labelPasswordError.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPasswordError.setObjectName(_fromUtf8("labelPasswordError"))
        self.verticalLayout_2.addWidget(self.labelPasswordError)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButtonSave = QtGui.QPushButton(dialogChangePassStaff)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout_3.addWidget(self.pushButtonSave)
        self.pushButtonClear = QtGui.QPushButton(dialogChangePassStaff)
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

        self.retranslateUi(dialogChangePassStaff)
        QtCore.QMetaObject.connectSlotsByName(dialogChangePassStaff)

    def retranslateUi(self, dialogChangePassStaff):
        dialogChangePassStaff.setWindowTitle(_translate("dialogChangePassStaff", "CHANGE PASSWORD", None))
        self.comboBox.setItemText(0, _translate("dialogChangePassStaff", "Select Staff", None))
        self.lineEditPassword1.setPlaceholderText(_translate("dialogChangePassStaff", "NEW PASSWORD", None))
        self.lineEditPassword2.setPlaceholderText(_translate("dialogChangePassStaff", "CONFIRM PASSWORD", None))
        self.labelPasswordError.setText(_translate("dialogChangePassStaff", "Passwords don\'t match!!", None))
        self.pushButtonSave.setText(_translate("dialogChangePassStaff", "Save", None))
        self.pushButtonClear.setText(_translate("dialogChangePassStaff", "Clear", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogChangePassStaff = QtGui.QDialog()
    ui = Ui_dialogChangePassStaff()
    ui.setupUi(dialogChangePassStaff)
    dialogChangePassStaff.show()
    sys.exit(app.exec_())

