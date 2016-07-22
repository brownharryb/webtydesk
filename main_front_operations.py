import allpaths,time
from PyQt4 import QtGui,QtCore
from misc import functions
from main_front_custom_window import MainFormWindow
from forms.main_front import Ui_MainWindow
from customer_operations import CustomerFunctions
from search_operations import SearchFormFunctions
from modify_operations import ModifyOperations
from send_message_operations import SendMessageFunctions
from transaction_options_functions import TrasanctionObj
from staff_functions import StaffObject
from admin_functions import AdminObject
from spareparts_functions import SpareParts
from db_backup.db_backup_functions import DbBackup
from fresh.setup_internet_fetch import StartUp
from fresh import *
from fixeditems_functions import FixedItem




class MainFrontFunctions():

    def __init__(self, db):
        self.db = db
        self.startUpObj = StartUp()
        self.setupAllObj()


    def setupAllObj(self):
        self.mainFormWindow = MainFormWindow()
        self.mainFormUi = Ui_MainWindow()
        self.mainFormUi.setupUi(self.mainFormWindow)
        self.shouldFetchNewData = False




    def showMainFrontForm(self):
        functions.centerWindow(self.mainFormWindow)
        self.mainFormWindow.show()
        self.mainFormUi.labelFetchingInfo.setVisible(False)
        self.mainFormUi.pushButtonAddRepairs.clicked.connect(self.showCustAddRepairForm)
        self.mainFormUi.pushButtonModifyRepairs.clicked.connect(lambda: self.showSearchForm())
        # self.mainFormUi.pushButtonModifyRepairs.clicked.connect(self.showModifyForm)
        self.mainFormUi.pushButtonMessageCust.clicked.connect(self.showSendMessageForm)
        self.mainFormUi.pushButtonAdminFront.clicked.connect(self.showLoginForm)
        self.mainFormUi.pushButtonTransaction.clicked.connect(self.showTransactionOptionsDialog)
        self.mainFormUi.pushButtonPartsFront.clicked.connect(lambda: self.showSparePartsDialog())
        self.mainFormUi.pushButtonDatabase.clicked.connect(lambda: self.showBackUpForm())
        self.mainFormUi.pushButtonNewData.clicked.connect(self.fetchNewData)
        self.mainFormUi.checkBoxFullscreen.stateChanged.connect(self.toggleFullscreenAction)



    def showCustAddRepairForm(self):
        self.custFormObj = CustomerFunctions(self.mainFormWindow,self.db)
        self.custFormObj.showCustForm()
        self.custFormObj.custui.pushButtonSave.clicked.connect(self.saveCustToDb)

    def showSearchForm(self):
        self.searchForm = SearchFormFunctions(self.mainFormWindow,self.db)
        self.searchForm.showForm()


    # def showModifyForm(self):
    #     self.modifyFormObj = ModifyOperations(self.mainFormWindow,self.db)
    #     self.modifyFormObj.showModifyForm()

    def saveCustToDb(self):
        self.custFormObj.saveButtonAction()

    def showSendMessageForm(self):
        self.sendMessage = SendMessageFunctions(self.mainFormWindow,self.db)
        self.sendMessage.sendMessageUi.pushButtonSend.clicked.connect(self.sendMessage.sendButtonClickedAction)
        self.sendMessage.showForm()


    def showAdminForm(self,staffObj):
        self.adminObj = AdminObject(self.mainFormWindow,staffObj,self.db)
        self.adminObj.showForm()

    def showLoginForm(self):
        self.staffObj = StaffObject(self.mainFormWindow,self.db)
        self.staffObj.showLoginDialog()
        self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(self.validateLogin)

    def validateLogin(self):
        if self.staffObj.loginClickedAction():
            if not self.staffObj.getDesignation().lower() == 'admin':
                self.staffObj.loginDialogUi.labelInvalidLogin.setVisible(True)
                self.staffObj.loginDialogUi.labelInvalidLogin.setText('Only the admin is allowed here!!')
                return
            self.staffObj.loginWindow.close()
            self.showAdminForm(self.staffObj)


    def showTransactionOptionsDialog(self):
        self.transactionObj = TrasanctionObj(self.mainFormWindow,self.db)
        self.transactionObj.showDialog()

    def showSparePartsDialog(self):
        self.sparePartsObj = SpareParts(self.db)
        self.sparePartsObj.showPartsForm(self.mainFormWindow)


    def showBackUpForm(self):
        self.backupObj = DbBackup(self.mainFormWindow,self.db)
        self.backupObj.showForm()

    def fetchNewData(self):
        self.shouldFetchNewData = not self.shouldFetchNewData
        if self.shouldFetchNewData:
            self.mainFormUi.labelFetchingInfo.setVisible(True)
            self.setLoader(self.mainFormUi.loadingLayout)
            self.updateInternetData()
        else:
            self.mainFormUi.labelFetchingInfo.setVisible(False)
            self.stopUpdatingInternetData()



    def setLoader(self,layout):
        loaderSize = QtCore.QSize(30,10)
        self.movieLoader = QtGui.QMovie(allpaths.getAnimatedLoaderPath('loader.gif'),QtCore.QByteArray(),self.mainFormWindow)
        self.labelLoader = QtGui.QLabel()
        self.labelLoader.setFixedSize(loaderSize)
        self.labelLoader.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        self.labelLoader.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.labelLoader)

        self.movieLoader.setCacheMode(QtGui.QMovie.CacheAll)
        self.movieLoader.setSpeed(60)
        self.movieLoader.setScaledSize(self.labelLoader.size())
        self.labelLoader.setMovie(self.movieLoader)
        self.movieLoader.start()

    def removeLoader(self):
        self.mainFormUi.labelFetchingInfo.setVisible(False)
        self.mainFormUi.labelFetchingInfo.setText('Fetching new data from internet...')
        if self.labelLoader:
            self.labelLoader.clear()
            self.labelLoader.setVisible(False)

# ********************************* GET DATA FROM INTERNET ****************************
    def updateInternetData(self):
        try:
            self.startUpObj.setUpThread(self.mainFormUi.labelFetchingInfo,self)
            self.startUpObj.threadToUse.start()
        except:
            self.mainFormUi.labelFetchingInfo.setText('There might be a problem with your internet!!... exiting')
            time.sleep(1)
            self.stopUpdatingInternetData()

    def stopUpdatingInternetData(self):
        if self.startUpObj.threadToUse.isRunning():
            self.startUpObj.threadToUse.quit()
        self.removeLoader()


# *************************************************************************************

# ***************************TOGGLE FULLSCREEN*****************************
    def toggleFullscreenAction(self):
        if self.mainFormUi.checkBoxFullscreen.isChecked():
            self.mainFormWindow.showFullScreen()
        else:
            self.mainFormWindow.showNormal()
# ***********************************************************************






#
# if __name__=='__main__':
#     import sys
#     from misc.dbfunctions import WebtyDb
#     d = WebtyDb()
#     app = QtGui.QApplication(sys.argv)
#     form = MainFrontFunctions(d)
#     sys.exit(app.exec_())
