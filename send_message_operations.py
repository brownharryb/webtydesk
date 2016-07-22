import csv,os
from misc import functions,allstrings
from forms.send_message import Ui_messageWindow
from staff_functions import StaffObject
from smsacc_functions import SmsAccount
from group_send_sms_add import GroupSms
from log.custom_log import LogObj
from log.logging_webty import LoggingWebty
from PyQt4 import QtGui,QtCore


class SendMessageFunctions():

    def __init__(self,parent,db):
        self.webtyLog = LoggingWebty(__name__)
        self.db = db
        self.parent = parent
        self.sendMessageWindow= QtGui.QMainWindow(self.parent)
        self.sendMessageUi = Ui_messageWindow()
        self.sendMessageUi.setupUi(self.sendMessageWindow)
        self.staffObj = StaffObject(self.sendMessageWindow,self.db)
        self.logObj = LogObj()
        self.smsAccObj = SmsAccount(self.db)
        self.successfulMessage = False
        self.currentRepairJobId = 0
        self.currentRepairJobStatus = ''


    def showForm(self):
        self.webtyLog.info('showing send message form')
        self.sendMessageWindow.show()
        self.sendMessageUi.lineEditSender.setText(self.smsAccObj.getActiveValue('sender_id'))
        self.sendMessageUi.progressBarSend.setVisible(False)
        self.formActions()
        self.setUpSearchCompleter()

    def formActions(self):
        self.sendMessageUi.pushButtonSenderId.clicked.connect(self.senderIdAction)
        self.sendMessageUi.lineEditSender.textChanged.connect(self.senderTextChangedAction)
        self.sendMessageUi.lineEditSearch.textChanged.connect(self.searchTextChangedAction)
        self.sendMessageUi.pushButtonAdd.clicked.connect(self.addButtonClickedAction)
        self.sendMessageUi.listWidgetAllRecipients.clicked.connect(self.recipientClickedAction)
        self.sendMessageUi.pushButtonClear.clicked.connect(self.clearButtonClickedAction)
        self.sendMessageUi.pushButtonDelete.clicked.connect(self.deleteButtonClickedAction)
        self.sendMessageUi.pushButtonPeopleAdd.clicked.connect(self.showGroupAddDialog)
        self.sendMessageUi.pushButtonRemoveDuplicates.clicked.connect(self.removeDuplicatesAction)


# ************************************REMOVE DUPLICATES****************************
    def removeDuplicatesAction(self):
        listWidget = self.sendMessageUi.listWidgetAllRecipients
        allnumbers = []
        countStep = 0

        while True:
            if listWidget.item(countStep) == None:
                break
            nameNumber = str(listWidget.item(countStep).text())
            eachNumber = nameNumber.strip().split(' ')[0]
            if eachNumber in allnumbers:
                listWidget.takeItem(countStep)
            else:
                allnumbers.append(eachNumber)
            countStep = countStep + 1
        self.sendMessageUi.labelNumberCount.setText(str(listWidget.count()))
# ************************************************************************************


    def setUpSearchCompleter(self):
        self.searchCompleter = QtGui.QCompleter()
        self.searchCompleter.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.searchCompleter.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        self.searchModel = QtGui.QStringListModel()
        self.searchCompleter.setModel(self.searchModel)
        self.sendMessageUi.lineEditSearch.setCompleter(self.searchCompleter)

        # self.searchModel.setStringList()

    def senderTextChangedAction(self):
        pass

# **********************************ADD GROUP SMS*****************************
    def showGroupAddDialog(self):
        self.groupSmsObj = GroupSms(self.sendMessageWindow,self.db)
        self.groupSmsObj.groupSmsUi.pushButtonUpdateToMain.clicked.connect(self.updateToMain)
        self.groupSmsObj.showForm()

    def updateToMain(self):
        table = self.groupSmsObj.groupSmsUi.tableWidgetNumbers
        listWidget = self.sendMessageUi.listWidgetAllRecipients
        rowCount = table.rowCount()
        allnum = []
        for i in xrange(rowCount):
            nameOfCust = str(table.item(i,0).text())
            number1 = str(table.item(i,1).text())
            number2 = ''
            numberName = number1+' '+nameOfCust
            if table.item(i,2):
                number2 = str(table.item(i,2).text())
            if not numberName in allnum:
                allnum.append(numberName)
            if not number2 == '':
                numberName2 = number2+' '+nameOfCust
                if not numberName2 in allnum:
                    allnum.append(numberName2)
        self.groupSmsObj.groupSmsDialog.close()
        numbersInListWidget =[]
        for h in xrange(listWidget.count()):
            numbersInListWidget.append(str(listWidget.item(h).text()))



        for j in allnum:
            if not j in numbersInListWidget:
                self.sendMessageUi.listWidgetAllRecipients.addItem(str(j))
        self.sendMessageUi.labelNumberCount.setText(str(listWidget.count()))






# ******************************************************************************

#********************************************ENABLING SENDER ID*********************************************
    def senderIdAction(self):
        if str(self.sendMessageUi.pushButtonSenderId.text()).lower() == 'Enable Sender'.lower():
            self.staffObj.showLoginDialog()
            self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(self.loginstaff2)
        elif str(self.sendMessageUi.pushButtonSenderId.text()).lower() == 'Disable Sender'.lower():
            self.sendMessageUi.lineEditSender.setEnabled(False)
            self.sendMessageUi.pushButtonSenderId.setText('Enable Sender')

    def loginstaff2(self):
        if self.staffObj.loginClickedAction():
            if not str(self.staffObj.getDesignation()).lower() == 'admin':
                self.sendMessageUi.lineEditSender.setEnabled(False)
                self.staffObj.loginDialogUi.labelInvalidLogin.setText('Only the admin is allowed here!')
                self.sendMessageUi.pushButtonSenderId.setText('Enable Sender')
                self.staffObj.loginDialogUi.labelInvalidLogin.setVisible(True)
            elif str(self.staffObj.getDesignation()).lower() == 'admin':
                self.sendMessageUi.lineEditSender.setEnabled(True)
                self.staffObj.loginDialogUi.labelInvalidLogin.setVisible(False)
                self.sendMessageUi.pushButtonSenderId.setText('Disable Sender')
                self.staffObj.loginWindow.close()


#***************************************************************************************************************


    def searchTextChangedAction(self):
        self.sendMessageUi.comboBoxPhoneNumber.setEnabled(False)
        self.sendMessageUi.comboBoxPhoneNumber.clear()
        searchedText = str(self.sendMessageUi.lineEditSearch.text())
        if functions.isNumber(searchedText) and not ' ' in searchedText:
            self.sendMessageUi.comboBoxPhoneNumber.addItem(searchedText)
        searchedList = functions.getAllSearchedNamesNumbers(self.db,searchedText)
        stringList = [x[1] for x in searchedList]
        self.searchModel.setStringList(stringList)
        for i in searchedList:
            if searchedText == i[1]:
                self.sendMessageUi.comboBoxPhoneNumber.addItem(i[2])
                if not i[3] == '':
                    self.sendMessageUi.comboBoxPhoneNumber.addItem(i[3])
                    self.sendMessageUi.comboBoxPhoneNumber.setEnabled(True)


    def addButtonClickedAction(self):
        listObj = self.sendMessageUi.listWidgetAllRecipients
        mobileNumber = self.sendMessageUi.comboBoxPhoneNumber.currentText()
        allItems = []
        for i in xrange(listObj.count()):
            allItems.append(str(listObj.item(i).text()))

        if not mobileNumber in allItems and not mobileNumber=='':
            self.sendMessageUi.listWidgetAllRecipients.addItem(mobileNumber)
            cnt = int(self.sendMessageUi.labelNumberCount.text())
            self.sendMessageUi.labelNumberCount.setText(str(cnt+1))

    def recipientClickedAction(self):
        self.sendMessageUi.pushButtonDelete.setEnabled(True)

    def clearButtonClickedAction(self):
        self.sendMessageUi.listWidgetAllRecipients.clear()
        self.sendMessageUi.lineEditSearch.clear()
        self.sendMessageUi.textEditMessage.clear()
        self.sendMessageUi.labelNumberCount.setText('0')
        self.sendMessageUi.pushButtonDelete.setEnabled(False)

    def deleteButtonClickedAction(self):
        itemSelected = self.sendMessageUi.listWidgetAllRecipients.selectedIndexes()
        itemSelected = [x.row() for x in itemSelected]
        for i in xrange(len(itemSelected)):
            itemToBeDeleted = int(max(itemSelected))
            self.sendMessageUi.listWidgetAllRecipients.takeItem(itemToBeDeleted)
            itemSelected.remove(itemToBeDeleted)

        self.sendMessageUi.labelNumberCount.setText(str(self.sendMessageUi.listWidgetAllRecipients.count()))
        if self.sendMessageUi.listWidgetAllRecipients.count() == 0:
            self.sendMessageUi.pushButtonDelete.setEnabled(False)

    def getNumbersFromListWidget(self,listWdget):
        allNum = []
        for i in xrange(listWdget.count()):
            eachNumberName = str(listWdget.item(i).text()).strip().split(' ')
            eachNumber = str(eachNumberName[0])
            if not  eachNumber in allNum and not eachNumber=='':
                allNum.append(eachNumber)
        return allNum

    def sendButtonClickedAction(self):
        listObj = self.sendMessageUi.listWidgetAllRecipients
        sender = self.sendMessageUi.lineEditSender.text()
        message = self.sendMessageUi.textEditMessage.toPlainText()
        self.allNumbers = self.getNumbersFromListWidget(listObj)

        # for i in xrange(listObj.count()):
        #     self.allNumbers.append(str(listObj.item(i).text()))
        if any([self.allNumbers == [], sender=='',message=='']):
            self.sendMessageUi.statusbar.showMessage('One or more inputs are invalid!!')
            return
        check = functions.checkTextInMessage(message)
        if not check =='ok':
            self.sendMessageUi.statusbar.showMessage(check)
            return
        if len(message)>500:
            self.sendMessageUi.statusbar.showMessage('Please Limit your mesage to 150 characters!!')
            return


        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Message','Send Message?',
                                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if confirm == QtGui.QMessageBox.No:
            return
        self.loginStaff(self.allNumbers,sender,message)


#************************************************LOGIN STAFF*********************************************************
    def loginStaff(self,allNumbers,senderId,message):
        self.staffObj.showLoginDialog()
        self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(lambda: self.confirmLogin(allNumbers,senderId,message))
    # TODO CONFIRM STAFF CREDIT BEFORE SENDING
    def confirmLogin(self,allNumbers,sender,message):
        if self.staffObj.loginClickedAction():
            self.staffObj.loginWindow.close()
            self.smsCredits = self.staffObj.getSmsCredits()
            self.stepCount = 0
            self.send(allNumbers[self.stepCount],sender,message)


#*******************************************************************************************************************

    def send(self,number,sender,message):
        if float(self.smsCredits) < len(self.allNumbers):
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Low Credit','You have '
                                            +str(self.smsCredits)+' sms units \nwhich is not enough for this operation!!',
                                            QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return
        totalnumbers = len(self.allNumbers)-1
        i = 0
        progress = self.sendMessageUi.progressBarSend
        progress.setVisible(True)
        self.t = CustomThread(self.stepCount,sender,number,message,
                              self.sendMessageUi,self.logObj,self.smsAccObj,self.staffObj,self.smsCredits,self.db)
        self.t.setRepairJobid(self.getRepairJobId())
        self.t.setRepairJobSatus(self.getRepairJobStatus())
        self.t.start()
        speed = 0.00001
        while i<100:
            i = i +speed
            progress.setValue(i)
            if self.t.isFinished():
                self.successfulMessage = self.t.messageSuccessful
                if self.t.internetProbs:
                    QtGui.QMessageBox.information(QtGui.QMessageBox(),'Error','Nothing sent, \nThere might be a problem with your '
                                                                              'internet connection or an sms account is not present!!',
                                                                    QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                    self.t.internetProbs = False
                speed = 0.0005
        progress.setVisible(False)
        self.stepCount = self.stepCount + 1
        if not self.stepCount > totalnumbers:
            self.send(self.allNumbers[self.stepCount],sender,message)

    def setRepairJobId(self,jobId):
        self.currentRepairJobId = jobId

    def getRepairJobId(self):
        return self.currentRepairJobId

    def setRepairJobStatus(self,status):
        self.currentRepairJobStatus = status

    def getRepairJobStatus(self):
        return self.currentRepairJobStatus





    def fadeWidget(self,flag='out',duration=500):
        self.effect = QtGui.QGraphicsOpacityEffect()
        self.sendMessageUi.progressBarSend.setGraphicsEffect(self.effect)
        self.opacityAnimation = QtCore.QPropertyAnimation(self.effect, 'opacity')
        self.opacityAnimation.setDuration(duration)
        if flag=='in':
            self.opacityAnimation.setStartValue(0)
            self.opacityAnimation.setEndValue(1)
        elif flag=='out':
            self.opacityAnimation.setStartValue(1)
            self.opacityAnimation.setEndValue(0)
        self.opacityAnimation.start(QtCore.QPropertyAnimation.DeleteWhenStopped)


class CustomThread(QtCore.QThread):

    successgreen = '#57B76E'
    failred = '#FF2525'

    def __init__(self,step,sender,number,message, widget,logObj,smsObj,staffObj,smsCredits,db):
        QtCore.QThread.__init__(self)
        self.widget = widget
        self.senderid = sender
        self.messagetext = message
        self.number = number
        self.step = step
        self.logObj = logObj
        self.smsAccObj = smsObj
        self.staffObj = staffObj
        self.smsCredits = smsCredits
        self.internetProbs = False
        self.messageSuccessful = False
        self.repairJobId = 0
        self.repairJobStatus = ''
        self.db2 = db


    def setRepairJobid(self,repairJobId):
        self.repairJobId = int(repairJobId)

    def setRepairJobSatus(self,status):
        self.repairJobStatus = status

    def updateRepairJobAlert(self):
        if int(self.repairJobId)>0:
            self.db2.updateRecord(allstrings.repairJobsTableName,{allstrings.repair_job_customer_notified:'1'},
                                  str(self.repairJobId))


    def run(self):
        item = self.widget.listWidgetAllRecipients.item(self.step)
        msg = ''
        try:
            returnVal = self.smsAccObj.sendSms(self.senderid,self.number,self.messagetext)
            if returnVal=='OK 1 ':
                item.setTextColor(QtGui.QColor(self.successgreen))
                self.smsCredits = self.smsCredits - 1
                msg = '\nSent Message Successfully \nNumber: '+str(self.number)+'\nMessage: '+str(self.messagetext)
                self.updateRepairJobAlert()
            else:
                item.setTextColor(QtGui.QColor(self.failred))
                msg = '\nSent Message Failed \nNumber: '+str(self.number)+'\nMessage: '+str(self.messagetext)
        except Exception:
            item.setTextColor(QtGui.QColor(self.failred))
            msg = '\nSent Message Failed \nNumber: '+str(self.number)+'\nMessage: '+str(self.messagetext)
            self.internetProbs = True

        finally:
            self.logObj.writeToLog(msg,self.staffObj.getStaffName())
            self.staffObj.setSmsCredits(self.smsCredits)
            self.staffObj.updateStaffDataToDb()















