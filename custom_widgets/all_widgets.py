from PyQt4 import QtGui, QtCore
import webbrowser
import datetime


class MyImageLabel(QtGui.QLabel):
    url = ''
    modelName=''

    def __init__(self):
        QtGui.QLabel.__init__(self)

    def mouseReleaseEvent(self, QMouseEvent):
        import threading
        threading._start_new_thread(self.visitsite,())

    def visitsite(self):
        webbrowser.open(self.url)


    def enterEvent(self, *args, **kwargs):
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.PointingHandCursor)

    def leaveEvent(self, *args, **kwargs):
        QtGui.QApplication.restoreOverrideCursor()


    def setUrl(self, url):
        self.url = url
    def setModelName(self, modelName):
        self.modelName = modelName
