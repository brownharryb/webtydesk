import datetime
from misc import allstrings,functions
from forms.money_dialog import Ui_dialogMoney
from log.custom_log import LogObj
from staff_functions import StaffObject
from PyQt4 import QtGui




class MoneyObj():

    def __init__(self,parent,db, moneyId=0):
        self.db = db
        self.parent = parent
        self.setUpDialog()
        self.tableName = allstrings.moneyTableName
        self.moneyId = moneyId
        self.dataDict = {}
        self.logObj = LogObj()
        self.logmessage = ''

    def setId(self,moneyId):
        self.moneyId = moneyId
        self.setUpObjs()

    def setUpObjs(self):
        data = self.db.retrieveRecordUsingId(self.tableName,self.moneyId)
        self.dataDict = functions.dbListTupleToListDict(data,self.tableName)[0]

    def getAllItems(self):
        data = self.db.retrieveAllVals(self.tableName)
        data = functions.dbListTupleToListDict(data,self.tableName)
        return data

    def getItemVal(self,col):
        return self.dataDict[col]

    def setItemVal(self,itemCol,val):
        self.dataDict[itemCol] = str(val)


    def saveMoneyData(self):
        if int(self.moneyId) > 0:
            self.db.updateRecord(self.tableName,self.dataDict,self.moneyId)
        else:
            self.dataDict[allstrings.date_added_column] = datetime.datetime.now()
            self.db.insertNewRecord(self.tableName,self.dataDict)
        self.logObj.writeToLog(self.logmessage,str(self.staffObj.getStaffName()))
        return True

#*******************************************FORMS************************************************************
    def setUpDialog(self):
        self.moneyUi = Ui_dialogMoney()
        self.moneyDialog = QtGui.QDialog(self.parent)
        self.moneyUi.setupUi(self.moneyDialog)

    def showDialog(self):
        self.moneyUi.pushButtonCancel.clicked.connect(self.cancelButtonDialogAction)
        self.moneyDialog.show()



    def checkValidInputs(self,flag=None):
        textAmount = self.moneyUi.lineEditAmount.text()
        purpose = self.moneyUi.textEditPurpose.toPlainText()
        allOk = functions.checkTextInMessage(purpose)
        if not allOk == 'ok':
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Invalid Input',
                    allOk,QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            return False

        if purpose == '':
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Invalid Input',
                    'Your Message is empty!!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            return False

        if len(purpose) >160:
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Invalid Input',
                    'Please limit message to 160 characters!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            return False

        if textAmount == '':
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Invalid Input',
                    'You have an empty amount!!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            return False
        if not functions.isNumber(textAmount):
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Invalid Input',
                    'Please enter a valid number for amount!!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            return False
        self.setItemVal(allstrings.money_amount_column,textAmount)
        self.setItemVal(allstrings.money_other_info_column,purpose)
        return True

    def saveButtonDialogAction(self):
        if self.checkValidInputs():
            confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Save','Save Transaction?',
                                QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if confirm == QtGui.QMessageBox.Yes:
                self.loginStaff()

    def loginStaff(self):
        self.staffObj = StaffObject(self.moneyDialog,self.db)
        self.staffObj.showLoginDialog()
        self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(self.loginClickedAction)

    def loginClickedAction(self):
        if self.staffObj.loginClickedAction():
            self.saveMoneyTransaction()
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Saved',
                    'Amount Saved!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            self.staffObj.loginWindow.close()
            self.moneyDialog.close()

    def saveMoneyTransaction(self):
        if self.moneyUi.radioButtonCash.isChecked():
            self.dataDict[allstrings.money_medium_column] = 'Cash'
        elif self.moneyUi.radioButtonPos.isChecked():
            self.dataDict[allstrings.money_medium_column] = 'POS'
        if self.dataDict[allstrings.money_transact_type_column] == 'Received':
            self.logmessage = 'Money Received N'+str(self.dataDict[allstrings.money_amount_column])+\
                  ' \nPurpose: '+str(self.dataDict[allstrings.money_other_info_column])
        elif self.dataDict[allstrings.money_transact_type_column] == 'Spent':
            self.logmessage = 'Money Spent N'+str(self.dataDict[allstrings.money_amount_column])+\
                  ' \nPurpose: '+str(self.dataDict[allstrings.money_other_info_column])

        self.saveMoneyData()

    def cancelButtonDialogAction(self):
        self.moneyDialog.close()

#*************************************************************************************************************
    def setLogMessage(self,msg):
        self.logmessage = msg

    def getLogMessage(self):
        return self.logmessage

    def getLatestPaymentDateForRepairJobId(self, repairId):
        data = self.db.retrieveRecord(self.tableName,{allstrings.money_repairjob_id_column:str(repairId)})
        data = functions.dbListTupleToListDict(data,self.tableName)
        data = [x[allstrings.date_added_column] for x in data]
        if data == []:
            return ''
        maxData = max(data)
        return maxData




# if __name__=='__main__':
#     from misc.dbfunctions import WebtyDb
#     db2 = WebtyDb()
#     money = MoneyObj(None,db2)

