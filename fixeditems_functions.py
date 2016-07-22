
from misc import allstrings,functions
from forms.fixed_items import Ui_fixedWindow
from send_message_operations import SendMessageFunctions
from money_functions import MoneyObj
from webtyprefs_functions import WebtyPrefs
from PyQt4 import QtGui,QtCore


class FixedItem():

    # TODO RECODE TO ALERT CUSTOMER
    def __init__(self,parent,db,itemId =0):
        self.db = db
        self.parent = parent
        self.repairJobsTableName = allstrings.repairJobsTableName
        self.customerTableName = allstrings.customersTableName
        self.itemId = itemId
        self.webtyPrefs = WebtyPrefs(self.db)

        if itemId > 0:
            self.setUpObj()

    def setUpObj(self):
        self.gettersdict = {}
        self.custgettersdict = {}
        data = self.getDataDict()
        self.gettersdict[allstrings.repair_job_item_name] =  data[allstrings.repair_job_item_name]
        self.gettersdict[allstrings.repair_job_bill] =  data[allstrings.repair_job_bill]
        self.gettersdict[allstrings.repair_job_bill_paid] = data[allstrings.repair_job_bill_paid]
        self.gettersdict[allstrings.repair_job_status] = data[allstrings.repair_job_status]
        self.gettersdict[allstrings.repair_job_other_info] = data[allstrings.repair_job_other_info]
        self.gettersdict[allstrings.repair_job_customer_id] = data[allstrings.repair_job_customer_id]
        self.gettersdict[allstrings.repair_job_date_received] =  data[allstrings.date_added_column]
        self.gettersdict[allstrings.repair_job_date_returned] =  data[allstrings.repair_job_date_returned]
        self.gettersdict[allstrings.repair_job_customer_notified] = data[allstrings.repair_job_customer_notified]
        custData = self.getCustomerDataDict()
        self.custgettersdict[allstrings.customer_name_column] = custData[allstrings.customer_name_column]
        self.custgettersdict[allstrings.customer_phone_number_column] = custData[allstrings.customer_phone_number_column]
        self.custgettersdict[allstrings.customer_other_number_column] = custData[allstrings.customer_other_number_column]
        self.custgettersdict[allstrings.date_added_column] = custData[allstrings.date_added_column]




    def showFixedDialog(self):
        self.fixedItemUi = Ui_fixedWindow()
        self.fixedItemWindow = QtGui.QMainWindow(self.parent)
        self.fixedItemUi.setupUi(self.fixedItemWindow)
        self.fixedItemUi.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.populateTable()
        self.fixedItemUi.tableWidget.hideColumn(0)
        self.disbleButtons()
        self.fixedItemUi.pushButtonSendSms.clicked.connect(self.sendSmsButtonAction)
        self.fixedItemUi.tableWidget.clicked.connect(self.tableItemSelected)
        self.fixedItemUi.pushButtonReceiveMoney.clicked.connect(self.moneyReceivedAction)
        self.fixedItemWindow.show()

    def sendSmsButtonAction(self):
        table = self.fixedItemUi.tableWidget
        self.smsObj = SendMessageFunctions(self.fixedItemWindow,self.db)
        custName = self.getItemValue(self.customerTableName,allstrings.customer_name_column)
        itemName = self.getItemValue(self.repairJobsTableName, allstrings.repair_job_item_name)
        msg = self.webtyPrefs.getFixedItemsSms(custName,itemName)
        number = self.getItemValue(self.customerTableName, allstrings.customer_phone_number_column)
        number2 = self.getItemValue(self.customerTableName,allstrings.customer_other_number_column)
        self.smsObj.sendMessageUi.textEditMessage.setText(str(msg))
        self.smsObj.sendMessageUi.listWidgetAllRecipients.addItem(str(number))
        self.smsObj.sendMessageUi.lineEditSearch.setText(custName)
        self.smsObj.sendMessageUi.lineEditSearch.setEnabled(False)
        self.smsObj.sendMessageUi.pushButtonPeopleAdd.setEnabled(False)
        if not number2 == '':
            self.smsObj.sendMessageUi.comboBoxPhoneNumber.addItem(number2)
        self.smsObj.sendMessageUi.comboBoxPhoneNumber.addItem(number)
        self.smsObj.sendMessageUi.comboBoxPhoneNumber.setEnabled(True)
        self.smsObj.sendMessageUi.pushButtonSend.clicked.connect(self.alertCustomerAction)
        self.smsObj.setRepairJobId(self.itemId)
        self.smsObj.setRepairJobStatus(self.getItemValue(self.repairJobsTableName,allstrings.repair_job_status))
        self.smsObj.showForm()

    def alertCustomerAction(self):
        self.smsObj.sendButtonClickedAction()


    def moneyReceivedAction(self):
        self.moneyObj = MoneyObj(self.fixedItemWindow,self.db)
        self.moneyObj.moneyDialog.setWindowTitle('FIXED ITEM PAYMENT')
        self.moneyObj.moneyUi.textEditPurpose.setEnabled(False)
        msg = 'Payment for '+self.getItemValue(self.repairJobsTableName,allstrings.repair_job_item_name)\
              +'\nBill '+self.getItemValue(self.repairJobsTableName,allstrings.repair_job_bill)\
              +'\nCustomer Name '+self.getItemValue(self.customerTableName,allstrings.customer_name_column)
        self.moneyObj.moneyUi.textEditPurpose.setText(msg)
        self.moneyObj.moneyUi.pushButtonSave.clicked.connect(self.moneySaveAction)
        self.moneyObj.showDialog()

    def moneySaveAction(self):
        oldAmountPaid = self.getItemValue(self.repairJobsTableName,allstrings.repair_job_bill_paid)
        self.moneyObj.dataDict[allstrings.money_transact_type_column]= 'Received'
        self.moneyObj.setItemVal(allstrings.money_repairjob_id_column,str(self.itemId))
        self.moneyObj.saveButtonDialogAction()
        newAmountPaid = self.moneyObj.getItemVal(allstrings.money_amount_column)
        newAmountPaid = float(oldAmountPaid) + float(newAmountPaid)
        self.setItemVal(self.repairJobsTableName,allstrings.repair_job_bill_paid,str(newAmountPaid))
        self.updateRepairVal()

    def getPaymentDate(self,itemId):
        self.moneyObj2 = MoneyObj(self.fixedItemWindow,self.db)
        return self.moneyObj2.getLatestPaymentDateForRepairJobId(itemId)


    def tableItemSelected(self):
        table = self.fixedItemUi.tableWidget
        selId = str(table.item(table.currentRow(),0).text())
        self.setId(int(selId))
        self.enableButtons()


    def disbleButtons(self):
        self.fixedItemUi.pushButtonSendSms.setEnabled(False)
        self.fixedItemUi.pushButtonReceiveMoney.setEnabled(False)
    def enableButtons(self):
        self.fixedItemUi.pushButtonReceiveMoney.setEnabled(True)
        self.fixedItemUi.pushButtonSendSms.setEnabled(True)


    def populateTable(self):
        table = self.fixedItemUi.tableWidget
        allids = self.getAllIds()
        if allids == []:
            return
        data = self.getAllFixedItemsFromDb()
        count  = len(allids)
        table.setRowCount(count)
        for i in xrange(count):
            newId = int(allids[i])
            self.setId(newId)
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            informed = 'No'
            if str(self.getItemValue(self.repairJobsTableName,allstrings.repair_job_customer_notified))==str(1):
                informed = 'Yes'
            #
            # if '0' in str(self.getItemValue(self.repairJobsTableName,
            #                                                 allstrings.repair_job_other_info)).lower():
            #     informed = 'Yes'


            itemName = item.clone()
            itemCustName = item.clone()
            itemBill = item.clone()
            itemCustInformed = item.clone()
            itemPaid = item.clone()
            itemPaymentDate = item.clone()
            itemReturnedDate = item.clone()
            itemReceivedDate = item.clone()
            table.setItem(i,0,item)
            table.setItem(i,1,itemName)
            table.setItem(i,2,itemCustName)
            table.setItem(i,3,itemBill)
            table.setItem(i,4,itemCustInformed)
            table.setItem(i,5,itemPaid)
            table.setItem(i,6,itemPaymentDate)
            table.setItem(i,7,itemReturnedDate)
            table.setItem(i,8,itemReceivedDate)


            item.setText(str(newId))
            itemName.setText(self.getItemValue(self.repairJobsTableName,allstrings.repair_job_item_name))
            itemCustName.setText(self.getItemValue(self.customerTableName,allstrings.customer_name_column))
            itemBill.setText(self.getItemValue(self.repairJobsTableName,allstrings.repair_job_bill))
            itemCustInformed.setText(informed)
            itemPaid.setText(self.getItemValue(self.repairJobsTableName,allstrings.repair_job_bill_paid))
            if not str(self.getPaymentDate(newId)) == '':
                itemPaymentDate.setText(functions.getShortDate(self.getPaymentDate(newId)))
            itemReturnedDate.setText(functions.getShortDate(self.getItemValue(self.repairJobsTableName,allstrings.repair_job_date_returned)))
            itemReceivedDate.setText(functions.getShortDate(self.getItemValue(self.repairJobsTableName, allstrings.repair_job_date_received)))



    def setId(self,itemId):
        if not itemId in self.getAllIds():
            return
        self.itemId = itemId
        if not itemId <1:
            self.setUpObj()

    def getAllFixedItemsFromDb(self):
        records = self.db.retrieveSearchedRecords(self.repairJobsTableName,allstrings.repair_job_status,'fixed')
        records = functions.dbListTupleToListDict(records,self.repairJobsTableName)
        return records

    def getAllIds(self):
        record = self.getAllFixedItemsFromDb()
        ids = [x[allstrings.allid_column] for x in record]
        return ids

    def getDataDict(self):
        returnData = {}
        allrecords = self.getAllFixedItemsFromDb()
        for i in allrecords:
            if i[allstrings.allid_column] == int(self.itemId):
                returnData = i
        return returnData

    def getCustomerDataDict(self):
        data = self.db.retrieveRecordUsingId(self.customerTableName,self.gettersdict[allstrings.repair_job_customer_id])
        data = functions.dbListTupleToListDict(data,self.customerTableName)[0]
        return data

    def getItemValue(self,tableName,val):
        if tableName == self.repairJobsTableName:
            return self.gettersdict[val]
        elif tableName == self.customerTableName:
            return self.custgettersdict[val]


    def setItemVal(self,tableName,itemkey,val):
        if tableName == self.repairJobsTableName:
            self.gettersdict[itemkey] = val
        elif tableName == self.customerTableName:
            self.custgettersdict[itemkey] = val

    def updateRepairVal(self):
        self.db.updateRecord(self.repairJobsTableName,self.gettersdict,int(self.itemId))


# if __name__ == '__main__':
#     from misc.dbfunctions import WebtyDb
#     db = WebtyDb()
#     fixed = FixedItem(None,db)
#     fixed.setId(2)
