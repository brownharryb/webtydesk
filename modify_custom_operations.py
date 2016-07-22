
from PyQt4 import QtGui

class ModifyWindowCustom(QtGui.QMainWindow):

    def __init__(self,parent):
        QtGui.QMainWindow.__init__(self,parent)


    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(QtGui.QMessageBox(),"Save Changes",
                            "Have you saved/updated your changes? \nif you have saved all your changes , you can click Yes",
                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            event.accept()
