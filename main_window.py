import sys,logging,allpaths, os
import logging.handlers
from misc import functions
from log.logging_webty import LoggingWebty
from misc.dbfunctions import WebtyDb
from PyQt4 import QtGui,QtCore
from main_front_operations import MainFrontFunctions
from customer_operations import CustomerFunctions
from repair_jobs_operation import RepairJobFunctions
from staff_functions import StaffObject
from log.custom_log import LogObj
from tendo import singleton


class MainApp():

    def __init__(self):
        self.webtyLog = LoggingWebty(__name__)
        self.webtyLog.info('Initializing application')
        self.startApp()


    def startApp(self):
        self.keepChecking = True
        self.webtyLog.info('Starting application')
        self.startUpDatabase()
        self.showSplash()
        self.timeLine = QtCore.QTimeLine(10000)
        self.timeLine.valueChanged.connect(self.checkForDb)
        self.timeLine.start()
        self.timeLine.finished.connect(self.removeSplash)
        return True




    def checkForDb(self):
        if self.timeLine.currentValue() > 0.5 and self.keepChecking==True:
            try:
                self.db = WebtyDb()
                self.startMain()
                self.keepChecking = False
            except Exception as e:
                # print "error message = "+str(e.message)
                if self.timeLine.currentValue() > 0.9:
                    self.webtyLog.warn('Database not started.. closing application')
                    self.labelChecking.setText('Please start database and restart app!')
                    self.keepChecking = False
        return True


#****************************START UP DATABASE**************************
    def startUpDatabase(self):
        mainDrive = os.environ['SYSTEMDRIVE']
        wampExePath = os.path.join(mainDrive,'wamp','wampmanager.exe')
        if os.path.exists(wampExePath):
            os.startfile(wampExePath)
#**********************************************************************


    def removeSplash(self):
        self.splashWindow.close()

    @functions.checkTime
    def startMain(self):
        self.mainFrontObj = MainFrontFunctions(self.db)
        self.customerObj = CustomerFunctions(None,self.db)
        self.repairObj = RepairJobFunctions()
        self.mainFrontObj.showMainFrontForm()
        self.staffObj = StaffObject(None,self.db)
        self.logObj = LogObj()
        self.createAdminIfNotExists()
        self.timeLine.stop()
        self.splashWindow.close()


    def createAdminIfNotExists(self):
        self.staffObj.createAdminIfNotPresent()



#******************************************SPLASH******************************
    def showSplash(self):
        self.webtyLog.info('Starting splash')
        self.splashWindow = QtGui.QDialog()
        self.splashWindow.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        self.splashWindow.setMinimumWidth(300)
        self.splashWindow.setWindowTitle('Start Up')
        self.vBox = QtGui.QVBoxLayout(self.splashWindow)
        self.labelChecking = QtGui.QLabel()
        self.splashFontLabel = QtGui.QFont()
        self.splashFontLabel.setBold(True)
        self.labelChecking.setFont(self.splashFontLabel)
        self.labelChecking.setAlignment(QtCore.Qt.AlignCenter)
        self.labelChecking.setText('Checking Database..')


        self.animMovie = QtGui.QMovie('pulse.gif',QtCore.QByteArray(),self.splashWindow)
        self.animLabel = QtGui.QLabel()
        self.animLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.animLabel.setMovie(self.animMovie)
        self.animMovie.setCacheMode(QtGui.QMovie.CacheAll)
        self.animMovie.setSpeed(150)
        self.animMovie.start()
        self.vBox.addWidget(self.labelChecking)
        self.vBox.addWidget(self.animLabel)
        self.splashWindow.setLayout(self.vBox)
        self.splashWindow.show()
#*********************************************************************************




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    # m = singleton.SingleInstance()
    app.setStyle("plastique")
    mainApp = MainApp()

    sys.exit(app.exec_())