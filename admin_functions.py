import webbrowser,requests,re,datetime
from log.custom_log import LogObj
from smsacc_functions import SmsAccount
from misc import allstrings,functions
from forms.admin_window import Ui_adminWindow
from forms.register_staff import Ui_dialogRegisterStaff
from forms.modify_staff import Ui_dialogModifyStaff
from forms.spareparts_add import Ui_dialogSparepartsAdd
from forms.spareparts_check import Ui_dialogSparepartsCheck
from forms.sms_check_admin import Ui_dialogSmsCredit
from forms.new_sms_account import Ui_dialogSmsNewAccount
from forms.check_log import Ui_logWindow
from forms.log_popup_info import Ui_dialogLogPopUp
from transaction_log import TransactionLog
from custom_widgets.select_date_functions import DateSelectFunctions
from spareparts_functions import SpareParts

from PyQt4 import QtGui,QtCore

class AdminObject():

    def __init__(self,parent,staffObj,db):
        self.db = db
        self.adminUi = Ui_adminWindow()
        self.adminWindow = QtGui.QMainWindow(parent)
        self.adminUi.setupUi(self.adminWindow)
        self.staffObj = staffObj
        self.parent = parent
        self.sparePartsObj = SpareParts(self.db)
        self.setUpCheckSmsDialog()
        self.smsAccObj = SmsAccount(self.db)
        self.t = CheckCreditThread(self.db,self.staffObj,self.smscheckObjUi,self.smsAccObj)
        self.t.start()
        self.logObj = LogObj()

    def setUpCheckSmsDialog(self):
        self.smscheckObjUi = Ui_dialogSmsCredit()
        self.smscheckObjDialog = QtGui.QDialog(self.adminWindow)
        self.smscheckObjUi.setupUi(self.smscheckObjDialog)


    def showForm(self):
        self.adminWindow.show()
        self.adminUi.pushButtonStaffNew.clicked.connect(self.showRegisterDialog)
        self.adminUi.pushButtonStaffModify.clicked.connect(self.showModifyStaffDialog)
        self.adminUi.pushButtonSparepartsAdd.clicked.connect(self.showSparePartsAddDialog)
        self.adminUi.pushButtonSparepartsCheck.clicked.connect(self.showSparePartsCheck)
        self.adminUi.pushButtonSmsPurchase.clicked.connect(self.smsPurchaseAction)
        self.adminUi.pushButtonSmsCheck.clicked.connect(self.smsCheckAction)
        self.adminUi.pushButtonSmsChangeAccount.clicked.connect(self.smsChangeAccount)
        self.adminUi.pushButtonLogCheck.clicked.connect(self.checkLogAction)
        self.adminUi.pushButtonTransactionLog.clicked.connect(self.transactionLogAction)


#*************************************TRANSACTION LOG *************************************************
    def transactionLogAction(self):
        self.transactionLog = TransactionLog(self.adminWindow,self.db)
        self.transactionLog.showWindow()

#********************************************************************************************************

    def showRegisterDialog(self):
        self.registerStaffWindow = QtGui.QDialog(self.parent)
        self.registerStaffUi = Ui_dialogRegisterStaff()
        self.registerStaffUi.setupUi(self.registerStaffWindow)
        self.registerStaffUi.labelError.setVisible(False)
        self.registerStaffWindow.show()
        self.registerStaffUi.pushButtonSave.clicked.connect(lambda: self.staffObj.saveStaffToDb(self.registerStaffUi,
                                                                                                self.registerStaffWindow))
        self.registerStaffUi.pushButtonClear.clicked.connect(lambda: self.staffObj.clearClickedRegAction(self.registerStaffUi))

    def showModifyStaffDialog(self):
        self.modifyStaffUi = Ui_dialogModifyStaff()
        self.modifyStaffDialog = QtGui.QDialog(self.parent)
        self.modifyStaffUi.setupUi(self.modifyStaffDialog)
        self.modifyStaffUi.labelError.setVisible(False)
        self.modifyStaffUi.labelDbId.setVisible(False)
        for i in self.staffObj.getAllUsernameList():
            self.modifyStaffUi.comboBoxAllStaffUsername.addItem(str(i).upper())
        self.modifyStaffUi.comboBoxAllStaffUsername.currentIndexChanged.connect(
                            lambda: self.staffObj.staffModifyComboChange(self.modifyStaffUi))
        self.modifyStaffUi.pushButtonSave.clicked.connect(
                            lambda: self.staffObj.staffModifyUpdate(self.modifyStaffUi,self.modifyStaffDialog))
        self.modifyStaffUi.pushButtonClear.clicked.connect(lambda: self.staffObj.initializeModifyDialog(self.modifyStaffUi))
        self.modifyStaffUi.pushButtonDelete.clicked.connect(
                            lambda: self.staffObj.staffModifyDelete(self.modifyStaffUi,self.modifyStaffDialog))
        self.modifyStaffDialog.show()

    def showSparePartsAddDialog(self):
        self.sparePartsAddUi = Ui_dialogSparepartsAdd()
        self.sparePartsAddDialog = QtGui.QDialog(self.parent)
        self.sparePartsAddUi.setupUi(self.sparePartsAddDialog)
        self.sparePartsAddUi.labelError.setVisible(False)
        self.sparePartsAddUi.pushButtonSave.clicked.connect(lambda: self.sparePartsObj.sparePartsAddSaveButtonClicked(
                                    self.sparePartsAddUi,self.sparePartsAddDialog))
        self.sparePartsAddUi.pushButtonClear.clicked.connect(lambda: self.sparePartsObj.sparePartsAddClearButtonClicked(
                                    self.sparePartsAddUi))
        self.sparePartsAddDialog.show()

    def showSparePartsCheck(self):
        self.sparePartsCheckUi = Ui_dialogSparepartsCheck()
        self.sparePartsCheckDialog = QtGui.QDialog(self.adminWindow)
        self.sparePartsCheckUi.setupUi(self.sparePartsCheckDialog)
        self.sparePartsCheckUi.labelError.setVisible(False)
        self.sparePartsCheckUi.labelDbId.setVisible(False)
        for i in self.sparePartsObj.getAllSparePartsName():
            self.sparePartsCheckUi.comboBoxSpareParts.addItem(str(i).upper())
        self.sparePartsCheckUi.comboBoxSpareParts.currentIndexChanged.connect(
                                lambda: self.sparePartsObj.sparePartsCheckComboChanged(self.sparePartsCheckUi))
        self.sparePartsCheckUi.pushButtonUpdate.clicked.connect(lambda:
                                                                self.sparePartsObj.sparePartsUpdateClickedAction(self.sparePartsCheckUi,
                                                                                                                 self.sparePartsCheckDialog))
        self.sparePartsCheckUi.pushButtonClear.clicked.connect(lambda:
                                                               self.sparePartsObj.sparePartsCheckClearButtonClicked(self.sparePartsCheckUi))
        self.sparePartsCheckDialog.show()

#*************************************************SMS CHECKING AND REGISTER*******************************************
    def smsPurchaseAction(self):
        url = 'https://www.quickteller.com/interbound'
        webbrowser.open(url)

    def smsCheckAction(self):
        self.smsAccObj = SmsAccount(self.db)
        self.t = CheckCreditThread(self.db,self.staffObj,self.smscheckObjUi,self.smsAccObj)
        self.setUpCheckSmsDialog()
        i = 0
        self.t.start()
        self.smscheckObjUi.labelCredit.setText(str(self.staffObj.getSmsCredits()))
        self.smscheckObjDialog.show()
        speed = 0.00001
        while i<100:
            self.smscheckObjUi.progressBar.setValue(i)
            i = i + speed
            if self.t.isFinished():
                speed = 0.0002
        self.smscheckObjUi.progressBar.setVisible(False)


#*************************************** FOR SMS ACCOUNT CHANGE************************************
    def smsChangeAccount(self):
        self.smsChangeAccountUi = Ui_dialogSmsNewAccount()
        self.smsChangeAccountDialog = QtGui.QDialog(self.parent)
        self.smsChangeAccountUi.setupUi(self.smsChangeAccountDialog)
        self.smsChangeAccountUi.labelError.setVisible(False)
        self.smsChangeAccountUi.progressBarConfirming.setVisible(False)
        self.smsChangeAccountUi.labelConfirming.setVisible(False)
        self.smsChangeAccountUi.pushButtonActivate.setVisible(False)
        self.smsChangeAccountUi.labelSenderId.setVisible(False)
        self.smsChangeAccountUi.lineEditSenderId.setVisible(False)
        self.smsChangeAccountUi.pushButtonVistWebsite.clicked.connect(self.smsAccountVisitWebsite)
        self.smsChangeAccountUi.pushButtonSave.clicked.connect(self.smsAccountSaveAction)
        self.smsChangeAccountUi.pushButtonCancel.clicked.connect(self.smsAccountClearAction)
        self.smsChangeAccountDialog.show()

    def smsAccountVisitWebsite(self):
        url = 'http://www.nigerianbulksms.com/register-free'
        webbrowser.open(url)

    def smsAccountSaveAction(self):
        self.smsChangeAccountUi.labelError.setVisible(False)
        username = str(self.smsChangeAccountUi.lineEditUsername.text())
        password1 = str(self.smsChangeAccountUi.lineEditPassword1.text())
        password2 = str(self.smsChangeAccountUi.lineEditPassword2.text())
        self.smsChangeAccountUi.progressBarConfirming.setValue(0)
        retn = ''

        if any([username=='', password1=='', password2=='']):
            self.smsChangeAccountUi.labelError.setText('Some inputs are empty!!')
            self.smsChangeAccountUi.labelError.setVisible(True)
            return
        if not password1 == password2:
            self.smsChangeAccountUi.labelError.setText('Passwords don\'t match')
            self.smsChangeAccountUi.labelError.setVisible(True)
            return
        self.smsChangeAccountUi.labelConfirming.setText('Verifying account....')
        self.smsChangeAccountUi.labelConfirming.setVisible(True)
        self.smsChangeAccountUi.progressBarConfirming.setVisible(True)
        i = 0
        speed = 0.000005
        self.confirmAccThread = ConfirmAccountThread(username,password1,self.smsChangeAccountUi)
        self.confirmAccThread.start()
        saved = False
        while i<100:
            i = i + speed
            self.smsChangeAccountUi.progressBarConfirming.setValue(i)
            if self.confirmAccThread.isFinished() and saved==False:
                retn = self.confirmAccThread.retn
                if retn == '':
                    self.smsChangeAccountUi.labelConfirming.setVisible(False)
                    self.smsChangeAccountUi.progressBarConfirming.setVisible(False)
                    self.smsChangeAccountUi.progressBarConfirming.setValue(0)
                    self.smsChangeAccountUi.labelError.setText('Unable to connect to website, Please check internet')
                    QtGui.QMessageBox.information(QtGui.QMessageBox(),'Check Internet','Please check your internet connection',
                                                QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                    break
                elif retn == '2905':
                    self.smsChangeAccountUi.labelConfirming.setVisible(False)
                    self.smsChangeAccountUi.progressBarConfirming.setVisible(False)
                    self.smsChangeAccountUi.progressBarConfirming.setValue(0)
                    self.smsChangeAccountUi.labelError.setText('Invalid Account, Please check if account is active!!')
                    self.smsChangeAccountUi.labelError.setVisible(True)
                    break
                else:
                    self.smsChangeAccountUi.labelConfirming.setStyleSheet('#labelConfirming{color:#00CD00}')
                    self.smsChangeAccountUi.labelConfirming.setText('Account verified... Saving..')
                    if self.smsAccObj.saveData(username,password1):
                        saved = True
                speed = 0.0001
        if i>= 100:
            self.smsChangeAccountUi.labelConfirming.setText('Account saved..You can change the Sender id and activate this account below')
            self.smsChangeAccountUi.pushButtonActivate.setVisible(True)
            self.smsChangeAccountUi.lineEditSenderId.setVisible(True)
            self.smsChangeAccountUi.labelSenderId.setVisible(True)

            self.smsChangeAccountUi.pushButtonActivate.clicked.connect(lambda: self.activateAccountAction(username))

    def closeSmsDialog(self):
        self.smsChangeAccountDialog.close()

    def activateAccountAction(self,username):
        senderId = self.smsChangeAccountUi.lineEditSenderId.text()
        senderId = str(senderId).replace('  ',' ')
        senderId = senderId.strip()
        if senderId.strip() == '':
            self.smsChangeAccountUi.lineEditSenderId.setStyleSheet('#lineEditSenderId{background-color: rgb(255, 0, 0);'
                                                                   'color: rgb(255, 255, 255);}')
            return
        if self.smsAccObj.activateAcc(username,senderId):
            self.smsChangeAccountUi.labelConfirming.setText('Account Activated.....Closing')
            QtCore.QTimer.singleShot(500, self.closeSmsDialog)

    def smsAccountClearAction(self):
        self.closeSmsDialog()
#***************************************************************************************************

#***********************************FOR LOG ACTIONS***************************************************
    def checkLogAction(self):
        self.checkLogUi = Ui_logWindow()
        self.checkLogWindow = QtGui.QMainWindow(self.adminWindow)
        self.checkLogUi.setupUi(self.checkLogWindow)
        self.checkLogUi.tableWidgetLogItems.hideColumn(0)
        self.checkLogUi.tableWidgetLogItems.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.checkLogUi.tableWidgetLogItems.doubleClicked.connect(self.tableItemDoubleClickedAction)
        self.checkLogUi.pushButtonSelectDate.clicked.connect(self.showCalendar)
        self.checkLogWindow.show()

    def showCalendar(self):
        self.dateObj = DateSelectFunctions(self.checkLogWindow)
        self.dateObj.dateUi.pushButtonOk.clicked.connect(self.dateOkClickedAction)
        self.dateObj.dateUi.pushButtonCancel.clicked.connect(self.dateCancelClickedAction)

    def dateCancelClickedAction(self):
        self.dateObj.dateWindow.close()

    def dateOkClickedAction(self):
        self.checkLogUi.tableWidgetLogItems.clearContents()
        self.checkLogUi.tableWidgetLogItems.setRowCount(0)
        try:
            dateSelected = self.dateObj.dateUi.calendarWidget.selectedDate().toPyDate()
            self.checkLogUi.pushButtonSelectDate.setText(str(dateSelected.strftime('%Y-%m-%d')))
            logDict = self.logObj.readFromLog(dateSelected)
            self.populateLogTable(logDict)
        except IOError as e:
            self.checkLogUi.statusbar.showMessage('No log file available for this date!!')
        finally:
            self.dateObj.dateWindow.close()

    def populateLogTable(self, dataDict):
        self.checkLogUi.tableWidgetLogItems.showColumn(0)
        i = 0
        table = self.checkLogUi.tableWidgetLogItems
        rowSize = len(dataDict)
        table.setRowCount(rowSize)
        for i in xrange(rowSize):
            snItem = QtGui.QTableWidgetItem()
            snItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            snItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            timeItem  = snItem.clone()
            staffItem = snItem.clone()
            infoItem = snItem.clone()

            table.setItem(i,0,snItem)
            table.setItem(i,1,timeItem)
            table.setItem(i,2,staffItem)
            table.setItem(i,3,infoItem)

            snItem.setText(str(dataDict[i][allstrings.allid_column]))
            timeItem.setText(str(dataDict[i][allstrings.date_added_column]))
            staffItem.setText(str(dataDict[i][allstrings.activity_staff_column]))
            infoItem.setText(str(dataDict[i][allstrings.activity_info_column]))

        self.checkLogUi.tableWidgetLogItems.hideColumn(0)


    def tableItemDoubleClickedAction(self):
        table = self.checkLogUi.tableWidgetLogItems
        itemRow  = table.currentRow()
        timeT = str(table.item(itemRow,1).text())
        staffName = str(table.item(itemRow,2).text())
        activity = str(table.item(itemRow,3).text())
        self.logPopUpUi = Ui_dialogLogPopUp()
        self.logPopUpDialog = QtGui.QDialog(self.checkLogWindow)
        self.logPopUpUi.setupUi(self.logPopUpDialog)
        self.logPopUpUi.labelTime.setText('Time: '+str(timeT))
        self.logPopUpUi.labelStaff.setText('Staff: '+str(staffName))
        self.logPopUpUi.textBrowser.setText('ACTIVITY: '+str(activity))
        self.logPopUpDialog.show()
#****************************************************************************************************



class CheckCreditThread(QtCore.QThread):


    pattern = re.compile(r'[0-9]+[.]+[0-9]{2}')

    def __init__(self,db,staffObj,smsUi,smsAccObj):
        QtCore.QThread.__init__(self)
        self.db2 = db
        self.adminStaff = staffObj
        self.smsUi = smsUi
        self.smsAccObj = smsAccObj

    # TODO MAKE THIS FETCH NEW CREDIT EVERYTIME
    def run(self):
        self.creditOperation()

    def creditOperation(self):
        try:
            url = str(self.smsAccObj.getActiveCheckBalanceUrl())
            r = requests.get(url)
            creditVal = r.content
            if self.pattern.match(str(creditVal)):
                self.db2.updateRecord(allstrings.staffTableName,{allstrings.staff_smscredit_column:str(creditVal)},
                                      self.adminStaff.getStaffId())
                self.db2.updateRecord(allstrings.smsAccTableName,{allstrings.sms_balance_column:str(creditVal)},
                                      str(self.smsAccObj.getActiveValue('_id')))
                self.adminStaff.setSmsCredits(str(creditVal))
                self.smsUi.labelCredit.setText(str(creditVal))
        except:
            pass


class ConfirmAccountThread(QtCore.QThread):

    def __init__(self, username, password,newAccUi):
        QtCore.QThread.__init__(self)
        self.username = username
        self.password = password
        self.newAccUi = newAccUi
        self.retn = ''

    def run(self):
        try:
            self.checkAccountValid()
        except:
            self.retn = ''


    def checkAccountValid(self):
        url = 'http://www.nigerianbulksms.com/components/com_spc/smsapi.php?username='+\
              str(self.username)+'&password='+str(self.password)+'&balance=true&'
        r = requests.get(url)
        returnVal = r.content
        self.retn = str(returnVal)

