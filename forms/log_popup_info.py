# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_popup_info.ui'
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

class Ui_dialogLogPopUp(object):
    def setupUi(self, dialogLogPopUp):
        dialogLogPopUp.setObjectName(_fromUtf8("dialogLogPopUp"))
        dialogLogPopUp.setWindowModality(QtCore.Qt.WindowModal)
        dialogLogPopUp.resize(491, 325)
        self.verticalLayout = QtGui.QVBoxLayout(dialogLogPopUp)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelTime = QtGui.QLabel(dialogLogPopUp)
        self.labelTime.setObjectName(_fromUtf8("labelTime"))
        self.verticalLayout.addWidget(self.labelTime)
        self.labelStaff = QtGui.QLabel(dialogLogPopUp)
        self.labelStaff.setObjectName(_fromUtf8("labelStaff"))
        self.verticalLayout.addWidget(self.labelStaff)
        self.textBrowser = QtGui.QTextBrowser(dialogLogPopUp)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(dialogLogPopUp)
        QtCore.QMetaObject.connectSlotsByName(dialogLogPopUp)

    def retranslateUi(self, dialogLogPopUp):
        dialogLogPopUp.setWindowTitle(_translate("dialogLogPopUp", "LOG ITEM", None))
        self.labelTime.setText(_translate("dialogLogPopUp", "TextLabel", None))
        self.labelStaff.setText(_translate("dialogLogPopUp", "TextLabel", None))
        self.textBrowser.setHtml(_translate("dialogLogPopUp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogLogPopUp = QtGui.QDialog()
    ui = Ui_dialogLogPopUp()
    ui.setupUi(dialogLogPopUp)
    dialogLogPopUp.show()
    sys.exit(app.exec_())

