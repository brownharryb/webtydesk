from PyQt4 import QtGui

class MainFormWindow(QtGui.QMainWindow):


    def __init__(self):
        QtGui.QMainWindow.__init__(self)

    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(QtGui.QMessageBox(),"Confirm Exit...",
                            "Are you sure you want to exit?",
                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            event.accept()




    # def show(self):
    #     QtGui.QMainWindow.show(self)
    #     self.showFullScreen()

