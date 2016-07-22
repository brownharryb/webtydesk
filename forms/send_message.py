# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_message.ui'
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

class Ui_messageWindow(object):
    def setupUi(self, messageWindow):
        messageWindow.setObjectName(_fromUtf8("messageWindow"))
        messageWindow.setWindowModality(QtCore.Qt.WindowModal)
        messageWindow.resize(659, 433)
        messageWindow.setMinimumSize(QtCore.QSize(659, 433))
        messageWindow.setMaximumSize(QtCore.QSize(659, 433))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/envelope2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        messageWindow.setWindowIcon(icon)
        messageWindow.setStyleSheet(_fromUtf8("#messageWindow{\n"
"border-image: url(:/backgrounds/images/backgounds/_8.jpg);\n"
"}"))
        self.centralwidget = QtGui.QWidget(messageWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditSender = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSender.setEnabled(False)
        self.lineEditSender.setMaxLength(11)
        self.lineEditSender.setObjectName(_fromUtf8("lineEditSender"))
        self.horizontalLayout_4.addWidget(self.lineEditSender)
        self.pushButtonSenderId = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSenderId.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonSenderId.setObjectName(_fromUtf8("pushButtonSenderId"))
        self.horizontalLayout_4.addWidget(self.pushButtonSenderId)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditSearch = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSearch.setObjectName(_fromUtf8("lineEditSearch"))
        self.horizontalLayout_3.addWidget(self.lineEditSearch)
        self.comboBoxPhoneNumber = QtGui.QComboBox(self.centralwidget)
        self.comboBoxPhoneNumber.setEnabled(False)
        self.comboBoxPhoneNumber.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxPhoneNumber.setObjectName(_fromUtf8("comboBoxPhoneNumber"))
        self.horizontalLayout_3.addWidget(self.comboBoxPhoneNumber)
        self.pushButtonAdd = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAdd.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/plus.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAdd.setIcon(icon1)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout_3.addWidget(self.pushButtonAdd)
        self.pushButtonPeopleAdd = QtGui.QPushButton(self.centralwidget)
        self.pushButtonPeopleAdd.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/people.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPeopleAdd.setIcon(icon2)
        self.pushButtonPeopleAdd.setObjectName(_fromUtf8("pushButtonPeopleAdd"))
        self.horizontalLayout_3.addWidget(self.pushButtonPeopleAdd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listWidgetAllRecipients = QtGui.QListWidget(self.centralwidget)
        self.listWidgetAllRecipients.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidgetAllRecipients.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidgetAllRecipients.setObjectName(_fromUtf8("listWidgetAllRecipients"))
        self.verticalLayout_3.addWidget(self.listWidgetAllRecipients)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labelNumberCount = QtGui.QLabel(self.centralwidget)
        self.labelNumberCount.setObjectName(_fromUtf8("labelNumberCount"))
        self.horizontalLayout_5.addWidget(self.labelNumberCount)
        self.pushButtonRemoveDuplicates = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRemoveDuplicates.setObjectName(_fromUtf8("pushButtonRemoveDuplicates"))
        self.horizontalLayout_5.addWidget(self.pushButtonRemoveDuplicates)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.textEditMessage = QtGui.QTextEdit(self.centralwidget)
        self.textEditMessage.setObjectName(_fromUtf8("textEditMessage"))
        self.horizontalLayout_2.addWidget(self.textEditMessage)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonDelete = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDelete.setEnabled(False)
        self.pushButtonDelete.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDelete.setIcon(icon3)
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.progressBarSend = QtGui.QProgressBar(self.centralwidget)
        self.progressBarSend.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBarSend.setStyleSheet(_fromUtf8("opacity:0;"))
        self.progressBarSend.setProperty("value", 24)
        self.progressBarSend.setTextVisible(False)
        self.progressBarSend.setObjectName(_fromUtf8("progressBarSend"))
        self.horizontalLayout.addWidget(self.progressBarSend)
        self.pushButtonSend = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.horizontalLayout.addWidget(self.pushButtonSend)
        self.pushButtonClear = QtGui.QPushButton(self.centralwidget)
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        messageWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(messageWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        messageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(messageWindow)
        QtCore.QMetaObject.connectSlotsByName(messageWindow)

    def retranslateUi(self, messageWindow):
        messageWindow.setWindowTitle(_translate("messageWindow", "Send Message", None))
        self.lineEditSender.setStatusTip(_translate("messageWindow", "Sender Id", None))
        self.lineEditSender.setPlaceholderText(_translate("messageWindow", "FROM", None))
        self.pushButtonSenderId.setText(_translate("messageWindow", "Enable Sender", None))
        self.lineEditSearch.setStatusTip(_translate("messageWindow", "Search", None))
        self.lineEditSearch.setPlaceholderText(_translate("messageWindow", "TO", None))
        self.pushButtonAdd.setStatusTip(_translate("messageWindow", "Add", None))
        self.pushButtonPeopleAdd.setStatusTip(_translate("messageWindow", "Add Group(CSV)", None))
        self.labelNumberCount.setText(_translate("messageWindow", "0", None))
        self.pushButtonRemoveDuplicates.setText(_translate("messageWindow", "Remove Duplicates", None))
        self.textEditMessage.setStatusTip(_translate("messageWindow", "Message", None))
        self.pushButtonDelete.setStatusTip(_translate("messageWindow", "Delete", None))
        self.pushButtonSend.setStatusTip(_translate("messageWindow", "Send Message", None))
        self.pushButtonSend.setText(_translate("messageWindow", "Send", None))
        self.pushButtonClear.setStatusTip(_translate("messageWindow", "Cancel", None))
        self.pushButtonClear.setText(_translate("messageWindow", "Clear", None))

import custom_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    messageWindow = QtGui.QMainWindow()
    ui = Ui_messageWindow()
    ui.setupUi(messageWindow)
    messageWindow.show()
    sys.exit(app.exec_())

