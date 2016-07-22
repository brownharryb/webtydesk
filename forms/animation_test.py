# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'animationTest.ui'
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

class Ui_animationTest(object):
    def setupUi(self, animationTest):
        animationTest.setObjectName(_fromUtf8("animationTest"))
        animationTest.resize(626, 459)
        self.centralwidget = QtGui.QWidget(animationTest)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        animationTest.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(animationTest)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        animationTest.setStatusBar(self.statusbar)

        self.retranslateUi(animationTest)
        QtCore.QMetaObject.connectSlotsByName(animationTest)

    def retranslateUi(self, animationTest):
        animationTest.setWindowTitle(_translate("animationTest", "Animation", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    animationTest = QtGui.QMainWindow()
    ui = Ui_animationTest()
    ui.setupUi(animationTest)
    animationTest.show()
    sys.exit(app.exec_())

