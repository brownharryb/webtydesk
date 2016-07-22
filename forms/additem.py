# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'additem.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(600, 325)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 325))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/plus.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("#MainWindow{\n"
"border-image: url(:/backgrounds/images/backgounds/_8.jpg);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lineEditPhoneBrand = QtGui.QLineEdit(self.centralwidget)
        self.lineEditPhoneBrand.setObjectName(_fromUtf8("lineEditPhoneBrand"))
        self.horizontalLayout_6.addWidget(self.lineEditPhoneBrand)
        self.lineEditPhoneModel = QtGui.QLineEdit(self.centralwidget)
        self.lineEditPhoneModel.setEnabled(False)
        self.lineEditPhoneModel.setObjectName(_fromUtf8("lineEditPhoneModel"))
        self.horizontalLayout_6.addWidget(self.lineEditPhoneModel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.lineEditItemName = QtGui.QLineEdit(self.centralwidget)
        self.lineEditItemName.setObjectName(_fromUtf8("lineEditItemName"))
        self.verticalLayout.addWidget(self.lineEditItemName)
        self.lineEditImeiNumber = QtGui.QLineEdit(self.centralwidget)
        self.lineEditImeiNumber.setObjectName(_fromUtf8("lineEditImeiNumber"))
        self.verticalLayout.addWidget(self.lineEditImeiNumber)
        self.lineEditKnownFaults = QtGui.QLineEdit(self.centralwidget)
        self.lineEditKnownFaults.setObjectName(_fromUtf8("lineEditKnownFaults"))
        self.verticalLayout.addWidget(self.lineEditKnownFaults)
        self.textEditAdditionalDetails = QtGui.QTextEdit(self.centralwidget)
        self.textEditAdditionalDetails.setObjectName(_fromUtf8("textEditAdditionalDetails"))
        self.verticalLayout.addWidget(self.textEditAdditionalDetails)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditBill = QtGui.QLineEdit(self.centralwidget)
        self.lineEditBill.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditBill.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditBill.setObjectName(_fromUtf8("lineEditBill"))
        self.horizontalLayout_2.addWidget(self.lineEditBill)
        self.checkBoxPendBill = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxPendBill.setObjectName(_fromUtf8("checkBoxPendBill"))
        self.horizontalLayout_2.addWidget(self.checkBoxPendBill)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEditPaid = QtGui.QLineEdit(self.centralwidget)
        self.lineEditPaid.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditPaid.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditPaid.setObjectName(_fromUtf8("lineEditPaid"))
        self.verticalLayout.addWidget(self.lineEditPaid)
        self.comboBoxStatus = QtGui.QComboBox(self.centralwidget)
        self.comboBoxStatus.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBoxStatus.setObjectName(_fromUtf8("comboBoxStatus"))
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxStatus)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.framePic = QtGui.QFrame(self.centralwidget)
        self.framePic.setMinimumSize(QtCore.QSize(200, 0))
        self.framePic.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framePic.setFrameShadow(QtGui.QFrame.Raised)
        self.framePic.setObjectName(_fromUtf8("framePic"))
        self.horizontalLayout.addWidget(self.framePic)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButtonOk = QtGui.QPushButton(self.centralwidget)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout_5.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_5.addWidget(self.pushButtonCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ADD ITEM FOR REPAIRS", None))
        self.lineEditPhoneBrand.setStatusTip(_translate("MainWindow", "Phone Make", None))
        self.lineEditPhoneBrand.setPlaceholderText(_translate("MainWindow", "Phone Make (optional)", None))
        self.lineEditPhoneModel.setStatusTip(_translate("MainWindow", "Phone Model", None))
        self.lineEditPhoneModel.setPlaceholderText(_translate("MainWindow", "Phone Model (optional)", None))
        self.lineEditItemName.setStatusTip(_translate("MainWindow", "Item Name (If make and model are not available)", None))
        self.lineEditItemName.setPlaceholderText(_translate("MainWindow", "Item Name", None))
        self.lineEditImeiNumber.setStatusTip(_translate("MainWindow", "Imei Number or Serial Number", None))
        self.lineEditImeiNumber.setPlaceholderText(_translate("MainWindow", "Imei Number", None))
        self.lineEditKnownFaults.setStatusTip(_translate("MainWindow", "Known Faults", None))
        self.lineEditKnownFaults.setPlaceholderText(_translate("MainWindow", "Known Faults", None))
        self.textEditAdditionalDetails.setStatusTip(_translate("MainWindow", "Additional Details", None))
        self.lineEditBill.setStatusTip(_translate("MainWindow", "Bill for this item", None))
        self.lineEditBill.setPlaceholderText(_translate("MainWindow", "Bill (Number only)", None))
        self.checkBoxPendBill.setStatusTip(_translate("MainWindow", "Pend this bill", None))
        self.checkBoxPendBill.setText(_translate("MainWindow", "Pend Bill", None))
        self.lineEditPaid.setStatusTip(_translate("MainWindow", "Amount already paid for item", None))
        self.lineEditPaid.setPlaceholderText(_translate("MainWindow", "Amount Paid (Number Only)", None))
        self.comboBoxStatus.setStatusTip(_translate("MainWindow", "Status", None))
        self.comboBoxStatus.setItemText(0, _translate("MainWindow", "PENDING", None))
        self.comboBoxStatus.setItemText(1, _translate("MainWindow", "WORK IN PROGRESS", None))
        self.comboBoxStatus.setItemText(2, _translate("MainWindow", "FIXED", None))
        self.comboBoxStatus.setItemText(3, _translate("MainWindow", "COMPLETED", None))
        self.comboBoxStatus.setItemText(4, _translate("MainWindow", "RETURNED", None))
        self.framePic.setStatusTip(_translate("MainWindow", "Visit Website", None))
        self.pushButtonOk.setText(_translate("MainWindow", "OK", None))
        self.pushButtonCancel.setText(_translate("MainWindow", "Cancel", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

