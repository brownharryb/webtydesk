# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sms_check_admin.ui'
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

class Ui_dialogSmsCredit(object):
    def setupUi(self, dialogSmsCredit):
        dialogSmsCredit.setObjectName(_fromUtf8("dialogSmsCredit"))
        dialogSmsCredit.setWindowModality(QtCore.Qt.WindowModal)
        dialogSmsCredit.resize(298, 100)
        dialogSmsCredit.setMinimumSize(QtCore.QSize(200, 100))
        dialogSmsCredit.setMaximumSize(QtCore.QSize(500, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/envelope2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogSmsCredit.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dialogSmsCredit)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelCredit = QtGui.QLabel(dialogSmsCredit)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelCredit.setFont(font)
        self.labelCredit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredit.setObjectName(_fromUtf8("labelCredit"))
        self.verticalLayout.addWidget(self.labelCredit)
        self.progressBar = QtGui.QProgressBar(dialogSmsCredit)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(dialogSmsCredit)
        QtCore.QMetaObject.connectSlotsByName(dialogSmsCredit)

    def retranslateUi(self, dialogSmsCredit):
        dialogSmsCredit.setWindowTitle(_translate("dialogSmsCredit", "Sms Credit Admin", None))
        self.labelCredit.setText(_translate("dialogSmsCredit", "credit", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogSmsCredit = QtGui.QDialog()
    ui = Ui_dialogSmsCredit()
    ui.setupUi(dialogSmsCredit)
    dialogSmsCredit.show()
    sys.exit(app.exec_())

