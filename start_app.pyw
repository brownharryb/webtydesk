import sys
from PyQt4 import QtGui,QtCore
from main_window import MainApp



app = QtGui.QApplication(sys.argv)
    # m = singleton.SingleInstance()
app.setStyle("plastique")
mainApp = MainApp()
sys.exit(app.exec_())