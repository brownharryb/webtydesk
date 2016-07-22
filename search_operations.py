from forms.searchform import Ui_searchForm
from PyQt4 import QtGui,QtCore
from addItem_operation import AddItemFunctions
from staff_functions import StaffObject
from misc import allstrings,functions
from log.logging_webty import LoggingWebty
from log.custom_log import LogObj


class SeachFormWindow(QtGui.QMainWindow):
    pass

class SearchFormFunctions():

    def __init__(self,parent, db):
        self.webtyLog = LoggingWebty(__name__)
        self.activityLog = LogObj()
        self.db = db
        self.parent = parent
        self.setUp()

    def setUp(self):
        self.setUpSearchOptions()
        self.searchFormUi = Ui_searchForm()
        self.searchFormWindow = SeachFormWindow(self.parent)
        self.searchFormUi.setupUi(self.searchFormWindow)
        self.searchFormUi.tableWidgetItemSearch.hideColumn(0)
        self.searchFormUi.tableWidgetItemSearch.hideColumn(10)
        self.setUpContextMenuActions()
        self.searchFormUi.tableWidgetItemSearch.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.searchFormUi.tableWidgetCustomerSearch.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.searchFormUi.lineEditItemSearch.setPlaceholderText('Search %s'%str(self.searchFormUi.
                                                                comboBoxItemSearch.currentText()).lower())
        self.searchFormUi.lineEditItemSearch.setStatusTip('Search %s'%str(self.searchFormUi.
                                                                comboBoxItemSearch.currentText()).lower())
        self.searchFormUi.lineEditCustomerSearch.setPlaceholderText('Search %s'%str(self.searchFormUi.
                                                                comboBoxCustomerSearch.currentText()).lower())
        self.searchFormUi.lineEditCustomerSearch.setStatusTip('Search %s'%str(self.searchFormUi.
                                                                comboBoxCustomerSearch.currentText()).lower())
        self.dbCustTableName = allstrings.customersTableName
        self.dbRepairJobTableName = allstrings.repairJobsTableName

#**********************************DELETING ITEMS THROUGH RIGHT CLICKING**********

    def loginRequired(func):
        def innerfunc(self,*args,**kwargs):
            self.staffObj = StaffObject(self.searchFormWindow,self.db)
            self.staffObj.showLoginDialog()
            def confirmLogin():
                if self.staffObj.loginClickedAction():
                    self.staffObj.loginWindow.close()
                    msg = func(self,*args,**kwargs)
                    msg = str(msg).strip()
                    if msg != '':
                        self.activityLog.writeToLog('\n'+msg,self.staffObj.getStaffName())
            self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(confirmLogin)
        return innerfunc



    def setUpContextMenuActions(self):

        self.searchFormUi.tableWidgetItemSearch.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.searchFormUi.tableWidgetCustomerSearch.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.deleteItemAction = QtGui.QAction('Delete this job',None)
        self.deleteCustAction = QtGui.QAction('Delete this customer',None)
        self.deleteItemAction.triggered.connect(self.confirmDeleteItemRow)
        self.deleteCustAction.triggered.connect(self.confirmDeleteCustRow)
        self.searchFormUi.tableWidgetItemSearch.addAction(self.deleteItemAction)
        self.searchFormUi.tableWidgetCustomerSearch.addAction(self.deleteCustAction)

    def confirmDeleteItemRow(self):
        row = self.searchFormUi.tableWidgetItemSearch.currentRow()
        if  row == -1:
            self.searchFormUi.statusbar.showMessage('No Job Selected!!')
            return
        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Delete Job',
            'Do you really want to delete this job? \nThis operation cannot be undone!!',
            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if confirm == QtGui.QMessageBox.Yes:
            self.deleteItemRow(row)


    def confirmDeleteCustRow(self):
        row = self.searchFormUi.tableWidgetCustomerSearch.currentRow()
        if row == -1:
            self.searchFormUi.statusbar.showMessage('No Customer Selected!!')
            return
        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Delete Customer',
            'Do you really want to delete this customer? \nThis operation cannot be undone!!',
            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if confirm == QtGui.QMessageBox.Yes:
            self.deleteCustRow(row)

    @loginRequired
    def deleteItemRow(self,row):
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        itemId = tableWidget.item(row,0)
        itemName = str(tableWidget.item(row,1).text())
        custId = str(tableWidget.item(row,10).text())
        if itemId != None:
            itemId = itemId.text()
            self.db.deleteRecord(self.dbRepairJobTableName, itemId)
        tableWidget.removeRow(row)
        QtGui.QMessageBox.information(QtGui.QMessageBox(),'Deleted','Job Deleted!!',QtGui.QMessageBox.Ok,
        QtGui.QMessageBox.Ok)
        return 'Deleted Job \nName: '+str(itemName)+'\nCustomer Id: '+str(custId)


    @loginRequired
    def deleteCustRow(self,row):
        tableWidget = self.searchFormUi.tableWidgetCustomerSearch
        custId = tableWidget.item(row,0).text()
        custName = tableWidget.item(row,1).text()
        self.db.deleteRecord(self.dbCustTableName,custId)
        self.db.deleteRecordUsingValue(self.dbRepairJobTableName, allstrings.repair_job_customer_id, str(custId))
        self.searchFormUi.tableWidgetItemSearch.clearContents()
        self.searchFormUi.tableWidgetItemSearch.setRowCount(0)
        tableWidget.removeRow(row)
        QtGui.QMessageBox.information(QtGui.QMessageBox(),'Deleted','Customer Deleted!!',QtGui.QMessageBox.Ok,
        QtGui.QMessageBox.Ok)
        return 'Deleted Customer \nName: '+str(custName)


#******************************** UPDATING TABLE ITEMS TO DATABASE***************************
    def saveButtonClickedAction(self):
        tableItem = self.searchFormUi.tableWidgetItemSearch
        tableCust = self.searchFormUi.tableWidgetCustomerSearch
        if  tableItem.rowCount() == 0 and tableCust.rowCount() == 0:
            return
        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Save Changes',
            'Save All Changes?',QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if confirm == QtGui.QMessageBox.Yes:
            self.saveAllChanges()

    @loginRequired
    def saveAllChanges(self):
        msg = ''
        msgSaveRepairJobs = self.saveRepairJobs()
        msgSaveCust = self.saveCustomers()
        QtGui.QMessageBox.information(QtGui.QMessageBox(),'Saved','Any change made has been saved!',
            QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
        if msgSaveCust:
            msg = msg+' '+msgSaveCust
        if msgSaveRepairJobs:
            msg = msg+' '+msgSaveRepairJobs
        return msg


    def saveRepairJobs(self):
        msg = ''
        a = []
        u = []
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        if tableWidget.rowCount() == 0:
            return msg
        data = self.getAllDataFromRepairTableAsList()
        for i in data:
            if not i.has_key(allstrings.allid_column):
                self.db.insertNewRecord(self.dbRepairJobTableName, i)
                a.append(i[allstrings.repair_job_item_name])
            elif i.has_key(allstrings.allid_column):
                self.db.updateRecord(self.dbRepairJobTableName,i,i[allstrings.allid_column])
                u.append(i[allstrings.repair_job_item_name])
        if a !=[]:
            msg = msg+' Added Job(s) \nJobs: '+str(a)
        if u !=[]:
            msg = msg + ' Updated Job(s) \nJobs: '+str(u)
        return msg

    # TODO SAVE CUSTOMERS
    def saveCustomers(self):
        msg = ''
        a = []
        tableWidget = self.searchFormUi.tableWidgetCustomerSearch

        if tableWidget.rowCount() == 0:
            return msg
        data = self.getAllDataFromCustTableAsList()
        for i in data:
            self.db.updateRecord(self.dbCustTableName,i,i[allstrings.allid_column])
            a.append(i[allstrings.customer_name_column])
        if a != []:
            msg = 'Updated Customer(s) \nName(s): '+str(a)
        return msg




    def getAllDataFromRepairTableAsList(self):

        returnList = []
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        count = tableWidget.rowCount()
        if count == 0:
            return []
        for i in xrange(count):
            data = {}
            if tableWidget.item(i,0):
                data[allstrings.allid_column] = str(tableWidget.item(i,0).text())
            data[allstrings.repair_job_item_name] = str(tableWidget.item(i,1).text())
            data[allstrings.repair_job_imei_serial] = str(tableWidget.item(i,2).text())
            data[allstrings.repair_job_knownfaults] = str(tableWidget.item(i,3).text())
            data[allstrings.repair_job_other_info] = str(tableWidget.item(i,4).text())
            data[allstrings.repair_job_bill] = str(tableWidget.item(i,5).text())
            data[allstrings.repair_job_bill_paid] = str(tableWidget.item(i,6).text())
            data[allstrings.repair_job_status] = str(tableWidget.item(i,7).text())
            data[allstrings.repair_job_date_received] = str(tableWidget.item(i,8).text())
            data[allstrings.repair_job_date_returned] = str(tableWidget.item(i,9).text())
            data[allstrings.repair_job_customer_id] = str(tableWidget.item(i,10).text())

            returnList.append(data)
        return returnList

    def getAllDataFromCustTableAsList(self):
        returnList = []
        tableWidget = self.searchFormUi.tableWidgetCustomerSearch
        count = tableWidget.rowCount()
        if count == 0:
            return []
        for i in xrange(count):
            data = {}
            data[allstrings.allid_column] = str(tableWidget.item(i,0).text())
            data[allstrings.customer_name_column] = str(tableWidget.item(i,1).text())

            if functions.isNumber(str(tableWidget.item(i,2).text())):
                data[allstrings.customer_phone_number_column] = str(tableWidget.item(i,2).text())
            if tableWidget.item(i,3):
                if functions.isNumber(str(tableWidget.item(i,3).text())):
                    data[allstrings.customer_other_number_column] = str(tableWidget.item(i,3).text())
            data[allstrings.date_added_column] = str(tableWidget.item(i,4).text())

            returnList.append(data)
        return returnList

#********************************************************************************************


    def setUpSearchOptions(self):
        self.searchRepairDict={}
        self.searchCustDict = {}

        self.searchRepairDict['make & model'] = allstrings.repair_job_item_name
        self.searchRepairDict['imei/s.no'] = allstrings.repair_job_imei_serial
        self.searchRepairDict['known faults'] = allstrings.repair_job_knownfaults
        self.searchRepairDict['additional details'] = allstrings.repair_job_other_info
        self.searchRepairDict['bill'] = allstrings.repair_job_bill
        self.searchRepairDict['amount paid'] = allstrings.repair_job_bill_paid
        self.searchRepairDict['status'] = allstrings.repair_job_status
        self.searchRepairDict['date in'] = allstrings.repair_job_date_received
        self.searchRepairDict['date out'] = allstrings.repair_job_date_returned
        self.searchRepairDict['_id'] = allstrings.allid_column

        self.searchCustDict['id'] = [allstrings.allid_column]
        self.searchCustDict['name'] = [allstrings.customer_name_column]
        self.searchCustDict['mobile'] = [allstrings.phone_name_column,allstrings.customer_other_number_column]
        self.searchCustDict['date added'] = [allstrings.date_added_column]

    def showForm(self):
        self.searchFormWindow.show()
        self.setActions()

    def setActions(self):
        self.searchFormUi.comboBoxItemSearch.currentIndexChanged.connect(self.comboItemChangedAction)
        self.searchFormUi.comboBoxCustomerSearch.currentIndexChanged.connect(self.comboCustomerChangedAction)
        self.searchFormUi.lineEditItemSearch.textChanged.connect(self.itemSearchingAction)
        self.searchFormUi.lineEditCustomerSearch.textChanged.connect(self.custSearchingAction)
        self.searchFormUi.tableWidgetCustomerSearch.clicked.connect(self.custTableClickedAction)
        # self.searchFormUi.tableWidgetItemSearch.clicked.connect(self.itemTableClickedAction)
        self.searchFormUi.tableWidgetItemSearch.doubleClicked.connect(self.doubleClickItemTableAction)
        self.searchFormUi.pushButtonAddItem.clicked.connect(self.addButtonClickedAction)
        self.searchFormUi.pushButtonSave.clicked.connect(self.saveButtonClickedAction)

    def itemSearchingAction(self):
        self.clearBothTables()
        searchedText = str(self.searchFormUi.lineEditItemSearch.text()).lower()
        searchedText = searchedText.strip()
        if searchedText == '':
            return

        if str(self.searchFormUi.comboBoxItemSearch.currentText()).lower() == 'id':

            data = self.db.retrieveSearchedRecords(self.dbRepairJobTableName,
                                               self.searchRepairDict['_id'],
                                               searchedText)
        else:
            data = self.db.retrieveSearchedRecords(self.dbRepairJobTableName,
                                               self.searchRepairDict[
                                                   str(self.searchFormUi.comboBoxItemSearch.currentText()).lower()
                                               ],
                                               searchedText)
        data = functions.dbListTupleToListDict(data,self.dbRepairJobTableName)
        self.populateItemTable(data)


    def custSearchingAction(self):
        self.clearBothTables()
        searchedText = str(self.searchFormUi.lineEditCustomerSearch.text()).lower()
        searchedText = searchedText.strip()
        if searchedText == '':
            return
        data = self.db.retrieveSearchedRecords(self.dbCustTableName,
                                               self.searchCustDict[
                                                   str(self.searchFormUi.comboBoxCustomerSearch.currentText()).lower()
                                               ][0],
                                               searchedText)

        if str(self.searchFormUi.comboBoxCustomerSearch.currentText()).lower() == 'mobile' and data==[]:
            data = self.db.retrieveSearchedRecords(self.dbCustTableName,
                                               self.searchCustDict[
                                                   str(self.searchFormUi.comboBoxCustomerSearch.currentText()).lower()
                                               ][1],
                                               searchedText)
        data = functions.dbListTupleToListDict(data,self.dbCustTableName)
        self.populateCustTable(data)


    def comboItemChangedAction(self):
        self.clearBothTables()
        self.searchedItemColumnName = self.searchFormUi.comboBoxItemSearch.currentText()
        self.searchFormUi.lineEditItemSearch.setPlaceholderText('Search %s'%str(self.searchedItemColumnName).lower())
        self.searchFormUi.lineEditItemSearch.setStatusTip('Search %s'%str(self.searchedItemColumnName).lower())


    def comboCustomerChangedAction(self):
        self.clearBothTables()
        self.searchedCustColumnName = self.searchFormUi.comboBoxCustomerSearch.currentText()
        self.searchFormUi.lineEditCustomerSearch.setPlaceholderText('Search %s'%str(self.searchedCustColumnName).lower())
        self.searchFormUi.lineEditCustomerSearch.setStatusTip('Search %s'%str(self.searchedCustColumnName).lower())

    def clearBothTables(self):
        self.searchFormUi.tableWidgetCustomerSearch.clearContents()
        self.searchFormUi.tableWidgetItemSearch.clearContents()
        self.searchFormUi.tableWidgetCustomerSearch.setRowCount(0)
        self.searchFormUi.tableWidgetItemSearch.setRowCount(0)


    def populateItemTable(self,data):
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        rowCount = len(data)
        tableWidget.setRowCount(rowCount)
        currentRow = 0

        for i in data:
            itemId = QtGui.QTableWidgetItem()
            itemId.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
            itemMakeModel = itemId.clone()
            itemImeiSrNo = itemId.clone()
            itemKnownFaults = itemId.clone()
            itemAdditionalDetails = itemId.clone()
            itemBill = itemId.clone()
            itemAmountPaid = itemId.clone()
            itemStatus = itemId.clone()
            itemDateIn = itemId.clone()
            itemDateOut = itemId.clone()
            itemCustId = itemId.clone()

            allItems = {0:[itemId,str(i[allstrings.allid_column])],1:[itemMakeModel,i[allstrings.repair_job_item_name]],
                        2:[itemImeiSrNo,i[allstrings.repair_job_imei_serial]],
                        3:[itemKnownFaults,i[allstrings.repair_job_knownfaults]],
                        4:[itemAdditionalDetails,i[allstrings.repair_job_other_info]],
                        5:[itemBill,i[allstrings.repair_job_bill]],
                        6:[itemAmountPaid,i[allstrings.repair_job_bill_paid]],
                        7:[itemStatus,i[allstrings.repair_job_status]],
                        8:[itemDateIn,str(i[allstrings.date_added_column])],
                        9:[itemDateOut,'---'],
                        10:[itemCustId,str(i[allstrings.repair_job_customer_id])]
                        }
            for i in allItems.keys():
                v = allItems[i]
                eachWidgetItem = v[0]
                eachWidgetValue = v[1]
                eachWidgetItem.setText(eachWidgetValue)
                eachWidgetItem.setToolTip(eachWidgetValue)
                tableWidget.setItem(currentRow,i,eachWidgetItem)
            currentRow = currentRow + 1

    def populateCustTable(self,data):
        if data == []:
            return
        tableWidget = self.searchFormUi.tableWidgetCustomerSearch
        rowCount = len(data)
        tableWidget.setRowCount(rowCount)
        currentRow = 0

        for i in data:
            custId = QtGui.QTableWidgetItem()

            custName = custId.clone()
            custMobile1 = custId.clone()
            custMobile2 = custId.clone()
            custDateAdded = custId.clone()

            custId.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
            custDateAdded.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)

            allCust = {0:[custId,str(i[allstrings.allid_column])],
                       1:[custName,str(i[allstrings.customer_name_column])],
                       2:[custMobile1,str(i[allstrings.customer_phone_number_column])],
                       3:[custMobile2,str(i[allstrings.customer_other_number_column])],
                       4:[custDateAdded,str(i[allstrings.date_added_column])]
                       }
            for j in allCust.keys():
                k = allCust[j]
                eachItemWidget = k[0]
                eachValue = k[1]
                eachItemWidget.setText(eachValue)
                eachItemWidget.setToolTip(eachValue)
                tableWidget.setItem(currentRow,j,eachItemWidget)
            currentRow = currentRow + 1


    def doubleClickItemTableAction(self):
        self.addItemObj = AddItemFunctions(self.searchFormWindow,self.db)
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        currentRow = tableWidget.currentRow()
        # itemId = tableWidget.item(currentRow,0).text()
        itemMakeModel = tableWidget.item(currentRow,1).text()
        itemImeiSr = tableWidget.item(currentRow,2).text()
        itemKnowFaults = tableWidget.item(currentRow,3).text()
        itemAdditionalDetails = tableWidget.item(currentRow,4).text()
        itemBill = tableWidget.item(currentRow,5).text()
        itemAmountPaid = tableWidget.item(currentRow,6).text()
        itemStatus = tableWidget.item(currentRow,7).text()
        itemDateIn = tableWidget.item(currentRow,8).text()
        itemDateOut = tableWidget.item(currentRow,9).text()
        self.addItemObj.showAddItemForm()
        self.addItemObj.addItemUi.lineEditItemName.setText(itemMakeModel)
        self.addItemObj.addItemUi.lineEditImeiNumber.setText(itemImeiSr)
        self.addItemObj.addItemUi.lineEditKnownFaults.setText(itemKnowFaults)
        self.addItemObj.addItemUi.textEditAdditionalDetails.setText(itemAdditionalDetails)
        self.addItemObj.addItemUi.lineEditBill.setText(itemBill)
        self.addItemObj.addItemUi.lineEditPaid.setText(itemAmountPaid)
        allStatus = self.addItemObj.getAllStatusAsDict()
        for i in allStatus.keys():
            if str(allStatus[i]).lower() == itemStatus:
                self.addItemObj.addItemUi.comboBoxStatus.setCurrentIndex(i)
                break
        self.addItemObj.addItemUi.pushButtonOk.clicked.connect(lambda: self.addItemOkAction(currentRow))



    def addItemOkAction(self,currentRow):
        if not self.addItemObj.cleanAllData():
            self.addItemObj.addItemUi.statusbar.showMessage('Please check your inputs and try again!!')
            return
        data = self.addItemObj.getAllDataAsDict()
        self.insertDataIntoItemTable(data,currentRow,flag=1)
        self.addItemObj.addItemWindow.close()



    def getAllItemsFromAddItemObj(self):
        itemName = str(self.addItemObj.addItemUi.lineEditItemName.text())
        itemImei = str(self.addItemObj.addItemUi.lineEditImeiNumber.text())
        itemKnownFaults = str(self.addItemObj.addItemUi.lineEditKnownFaults.text())
        itemAdditionalDetails = str(self.addItemObj.addItemUi.textEditAdditionalDetails.toPlainText())
        itemBill = str(self.addItemObj.addItemUi.lineEditBill.text())
        itemPaid = str(self.addItemObj.addItemUi.lineEditPaid.text())
        itemStatus = str(self.addItemObj.addItemUi.comboBoxStatus.currentText()).lower()

        d = {1:itemName,2:itemImei,3:itemKnownFaults,4:itemAdditionalDetails,5:itemBill,6:itemPaid,7:itemStatus}
        return d

    def insertDataIntoItemTable(self,data,row,flag=0,addDateIn=False):
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        itemName = QtGui.QTableWidgetItem()
        itemName.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        itemId = itemName.clone()
        itemImei = itemName.clone()
        itemKnownFaults = itemName.clone()
        itemAdditionalInfo = itemName.clone()
        itemBill = itemName.clone()
        itemPaid = itemName.clone()
        itemStatus = itemName.clone()
        itemDateIn = itemName.clone()
        itemDateOut = itemName.clone()
        itemCustID = itemName.clone()

        if flag==1:
            itemName.setText(data['name'])
            itemName.setToolTip(data['name'])

            itemImei.setText(data['imei_serial'])
            itemImei.setToolTip(data['imei_serial'])

            itemKnownFaults.setText(data['knownFaults'])
            itemKnownFaults.setToolTip(data['knownFaults'])

            itemAdditionalInfo.setText(data['additionalInfo'])
            itemAdditionalInfo.setToolTip(data['additionalInfo'])

            itemBill.setText(str(data['bill']))
            itemBill.setToolTip(str(data['bill']))

            itemPaid.setText(str(data['paid']))
            itemPaid.setToolTip(str(data['paid']))

            itemStatus.setText(data['status'])
            itemStatus.setToolTip(data['status'])

            if addDateIn:
                itemDateIn.setText(data['today'])
                itemDateIn.setToolTip(data['today'])
                tableWidget.setItem(row,8,itemDateIn)

            if data['status'] == 'completed':
                itemDateOut.setText(data['today'])
                itemDateOut.setToolTip(data['today'])
            else:
                itemDateOut.setText('---')
                itemDateOut.setToolTip('---')

            if data.has_key('custId'):
                itemCustID.setText(str(data['custId']))
                itemCustID.setToolTip(str(data['custId']))
                tableWidget.setItem(row,10,itemCustID)
        elif flag==2:
            itemName.setText(data[allstrings.repair_job_item_name])
            itemName.setToolTip(data[allstrings.repair_job_item_name])

            itemImei.setText(data[allstrings.repair_job_imei_serial])
            itemImei.setToolTip(data[allstrings.repair_job_imei_serial])

            itemKnownFaults.setText(data[allstrings.repair_job_knownfaults])
            itemKnownFaults.setToolTip(data[allstrings.repair_job_knownfaults])

            itemAdditionalInfo.setText(data[allstrings.repair_job_other_info])
            itemAdditionalInfo.setToolTip(data[allstrings.repair_job_other_info])

            itemBill.setText(str(data[allstrings.repair_job_bill]))
            itemBill.setToolTip(str(data[allstrings.repair_job_bill]))

            itemPaid.setText(str(data[allstrings.repair_job_bill_paid]))
            itemPaid.setToolTip(str(data[allstrings.repair_job_bill_paid]))

            itemStatus.setText(data[allstrings.repair_job_status])
            itemStatus.setToolTip(data[allstrings.repair_job_status])

            itemDateIn.setText(str(data[allstrings.date_added_column]))
            itemDateIn.setToolTip(str(data[allstrings.date_added_column]))
            tableWidget.setItem(row,8,itemDateIn)

            itemId.setText(str(data[allstrings.allid_column]))
            itemId.setToolTip(str(data[allstrings.allid_column]))
            tableWidget.setItem(row,0,itemId)

            itemCustID.setText(str(data[allstrings.repair_job_customer_id]))
            itemCustID.setToolTip(str(data[allstrings.repair_job_customer_id]))
            tableWidget.setItem(row,10,itemCustID)
            if data[allstrings.repair_job_status] == 'completed':
                itemDateOut.setText(str(data[allstrings.repair_job_date_returned]))
                itemDateOut.setToolTip(str(data[allstrings.repair_job_date_returned]))
            else:
                itemDateOut.setText('---')
                itemDateOut.setToolTip('---')


        tableWidget.setItem(row,1,itemName)
        tableWidget.setItem(row,2,itemImei)
        tableWidget.setItem(row,3,itemKnownFaults)
        tableWidget.setItem(row,4,itemAdditionalInfo)
        tableWidget.setItem(row,5,itemBill)
        tableWidget.setItem(row,6,itemPaid)
        tableWidget.setItem(row,7,itemStatus)
        tableWidget.setItem(row,9,itemDateOut)

    def addDataToItemTable(self,data):
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        row = tableWidget.rowCount()+1
        tableWidget.setRowCount(row)
        self.insertDataIntoItemTable(data,row-1,flag=1,addDateIn=True)
        return True


#*******************************BUTTONS ACTION****************************
    def addButtonClickedAction(self):
        row = self.searchFormUi.tableWidgetCustomerSearch.currentRow()
        if row == -1:
            self.searchFormUi.statusbar.showMessage('Please select a customer first!!')
            return
        addItemObj = AddItemFunctions(self.searchFormWindow,self.db)
        addItemObj.showAddItemForm()
        def innerfunc():
            if not addItemObj.cleanAllData():
                addItemObj.addItemUi.statusbar.showMessage('Please check your inputs!!')
                return
            data = addItemObj.getAllDataAsDict()
            data['custId'] = str(self.searchFormUi.tableWidgetCustomerSearch.item(
                                    self.searchFormUi.tableWidgetCustomerSearch.currentRow(),0).text())

            if self.addDataToItemTable(data):
                addItemObj.addItemWindow.close()

        addItemObj.addItemUi.pushButtonOk.clicked.connect(innerfunc)


#**********************************************************

#********************************TABLE CLICKED ONCE*******************
    def itemTableClickedAction(self):
        self.searchFormUi.tableWidgetCustomerSearch.clearContents()
        tableWidget = self.searchFormUi.tableWidgetItemSearch
        # TODO DOUBLECLICKING NOT WORKING
        custId = tableWidget.item(tableWidget.currentRow(),0).text()
        data = self.db.retrieveSearchedRecords(self.dbCustTableName,
                                               allstrings.allid_column, str(custId))
        data = functions.dbListTupleToListDict(data,self.dbCustTableName)

    def custTableClickedAction(self):
        self.searchFormUi.tableWidgetItemSearch.clearContents()
        tableWidget = self.searchFormUi.tableWidgetCustomerSearch

        custId = tableWidget.item(tableWidget.currentRow(),0).text()
        data = self.db.retrieveSearchedRecords(self.dbRepairJobTableName,
                                               allstrings.repair_job_customer_id, str(custId))
        data = functions.dbListTupleToListDict(data,self.dbRepairJobTableName)
        j = 0
        self.searchFormUi.tableWidgetItemSearch.setRowCount(len(data))
        for eachData in data:
            self.insertDataIntoItemTable(eachData,j,flag=2)
            j = j+1


#*********************************************************************