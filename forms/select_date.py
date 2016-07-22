# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_date_widget.ui'
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

class Ui_formDateWidget(object):
    def setupUi(self, formDateWidget):
        formDateWidget.setObjectName(_fromUtf8("formDateWidget"))
        formDateWidget.setWindowModality(QtCore.Qt.WindowModal)
        formDateWidget.resize(418, 271)
        self.verticalLayout = QtGui.QVBoxLayout(formDateWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.calendarWidget = QtGui.QCalendarWidget(formDateWidget)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.verticalLayout.addWidget(self.calendarWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonOk = QtGui.QPushButton(formDateWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOk.setFont(font)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtGui.QPushButton(formDateWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(formDateWidget)
        QtCore.QMetaObject.connectSlotsByName(formDateWidget)

    def retranslateUi(self, formDateWidget):
        formDateWidget.setWindowTitle(_translate("formDateWidget", "Select Date", None))
        self.pushButtonOk.setText(_translate("formDateWidget", "OK", None))
        self.pushButtonCancel.setText(_translate("formDateWidget", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    formDateWidget = QtGui.QDialog()
    ui = Ui_formDateWidget()
    ui.setupUi(formDateWidget)
    formDateWidget.show()
    sys.exit(app.exec_())

