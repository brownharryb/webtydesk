# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup_db.ui'
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

class Ui_dialogBackupDb(object):
    def setupUi(self, dialogBackupDb):
        dialogBackupDb.setObjectName(_fromUtf8("dialogBackupDb"))
        dialogBackupDb.setWindowModality(QtCore.Qt.WindowModal)
        dialogBackupDb.resize(800, 400)
        dialogBackupDb.setMinimumSize(QtCore.QSize(800, 400))
        dialogBackupDb.setMaximumSize(QtCore.QSize(800, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/database.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogBackupDb.setWindowIcon(icon)
        dialogBackupDb.setStyleSheet(_fromUtf8("#dialogBackupDb{border-image: url(:/backgrounds/images/backgounds/_8.jpg);}"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(dialogBackupDb)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBoxChooseFunction = QtGui.QComboBox(dialogBackupDb)
        self.comboBoxChooseFunction.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxChooseFunction.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxChooseFunction.setFont(font)
        self.comboBoxChooseFunction.setObjectName(_fromUtf8("comboBoxChooseFunction"))
        self.comboBoxChooseFunction.addItem(_fromUtf8(""))
        self.comboBoxChooseFunction.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxChooseFunction)
        self.pushButtonSelectFolder = QtGui.QPushButton(dialogBackupDb)
        self.pushButtonSelectFolder.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButtonSelectFolder.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonSelectFolder.setFont(font)
        self.pushButtonSelectFolder.setObjectName(_fromUtf8("pushButtonSelectFolder"))
        self.verticalLayout.addWidget(self.pushButtonSelectFolder)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidgetAllFiles = QtGui.QTableWidget(dialogBackupDb)
        self.tableWidgetAllFiles.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetAllFiles.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetAllFiles.setObjectName(_fromUtf8("tableWidgetAllFiles"))
        self.tableWidgetAllFiles.setColumnCount(3)
        self.tableWidgetAllFiles.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllFiles.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllFiles.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAllFiles.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableWidgetAllFiles)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.progressBarUpdate = QtGui.QProgressBar(dialogBackupDb)
        self.progressBarUpdate.setMinimumSize(QtCore.QSize(0, 5))
        self.progressBarUpdate.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBarUpdate.setProperty("value", 24)
        self.progressBarUpdate.setTextVisible(False)
        self.progressBarUpdate.setObjectName(_fromUtf8("progressBarUpdate"))
        self.verticalLayout_2.addWidget(self.progressBarUpdate)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelFolderlPath = QtGui.QLabel(dialogBackupDb)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelFolderlPath.setFont(font)
        self.labelFolderlPath.setObjectName(_fromUtf8("labelFolderlPath"))
        self.horizontalLayout_2.addWidget(self.labelFolderlPath)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonOk = QtGui.QPushButton(dialogBackupDb)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOk.setFont(font)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout_2.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtGui.QPushButton(dialogBackupDb)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialogBackupDb)
        QtCore.QMetaObject.connectSlotsByName(dialogBackupDb)

    def retranslateUi(self, dialogBackupDb):
        dialogBackupDb.setWindowTitle(_translate("dialogBackupDb", "DATABASE", None))
        self.comboBoxChooseFunction.setItemText(0, _translate("dialogBackupDb", "BACKUP", None))
        self.comboBoxChooseFunction.setItemText(1, _translate("dialogBackupDb", "RESTORE", None))
        self.pushButtonSelectFolder.setText(_translate("dialogBackupDb", "Select Folder", None))
        self.tableWidgetAllFiles.setSortingEnabled(True)
        item = self.tableWidgetAllFiles.horizontalHeaderItem(0)
        item.setText(_translate("dialogBackupDb", "Name", None))
        item = self.tableWidgetAllFiles.horizontalHeaderItem(1)
        item.setText(_translate("dialogBackupDb", "Date", None))
        item = self.tableWidgetAllFiles.horizontalHeaderItem(2)
        item.setText(_translate("dialogBackupDb", "Time", None))
        self.labelFolderlPath.setText(_translate("dialogBackupDb", "path", None))
        self.pushButtonOk.setText(_translate("dialogBackupDb", "OK", None))
        self.pushButtonCancel.setText(_translate("dialogBackupDb", "CANCEL", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogBackupDb = QtGui.QDialog()
    ui = Ui_dialogBackupDb()
    ui.setupUi(dialogBackupDb)
    dialogBackupDb.show()
    sys.exit(app.exec_())

