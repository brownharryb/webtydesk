import datetime,logging

from misc import functions
from forms.updatecustform import Ui_updateForm
from addItem_operation import AddItemFunctions
from custom_widgets.select_date_functions import DateSelectFunctions
from staff_functions import StaffObject
from log.custom_log import LogObj
from modify_custom_operations import ModifyWindowCustom
from customer_operations import CustomerFunctions
from PyQt4 import QtGui, QtCore
from misc import allstrings


class ModifyOperations():

    def __init__(self,parent,db):
        self.logger = logging.getLogger(__name__)
        self.db = db
        self.parent = parent
        self.setupAllObj()
        self.setupCompleter()
        self.comboSearchAction()
        self.staffObj = StaffObject(self.updateMainWindow,self.db)
        self.logObj = LogObj()
        self.logMessage = ''

    def setUpLogging(self):
        pass


    def setupAllObj(self):
        self.updateMainWindow = ModifyWindowCustom(self.parent)
        self.custUpdateUi = Ui_updateForm()
        self.custUpdateUi.setupUi(self.updateMainWindow)
        self.searchChoiceList= ['name','number','item','date',]
        self.allValuesForSearch=[]
        self.firstDate=''
        self.secondDate=''
        self.idOnTableClicked={}






    def setupCompleter(self):
        self.completerModel = QtGui.QStringListModel()
        self.completerModel.setStringList(self.allValuesForSearch)
        self.completer = QtGui.QCompleter()
        self.completer.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        self.completer.setModel(self.completerModel)
        # self.custUpdateUi.lineEditSearchCustomer.setCompleter(self.completer)

    def disableAllButtons(self):
        self.custUpdateUi.pushButtonAdd.setEnabled(False)
        self.custUpdateUi.pushButtonDelete.setEnabled(False)
        self.custUpdateUi.pushButtonUpdate.setEnabled(False)
        self.custUpdateUi.pushButtonFixed.setEnabled(False)
        self.custUpdateUi.pushButtonUnfixed.setEnabled(False)
        self.custUpdateUi.pushButtonReturned.setEnabled(False)

    def enableCustButtons(self):
        self.custUpdateUi.pushButtonAdd.setEnabled(True)
        self.custUpdateUi.pushButtonDelete.setEnabled(True)
        self.custUpdateUi.pushButtonUpdate.setEnabled(True)


    def enableRepairButtons(self):
        self.custUpdateUi.pushButtonFixed.setEnabled(True)
        self.custUpdateUi.pushButtonUnfixed.setEnabled(True)
        self.custUpdateUi.pushButtonReturned.setEnabled(True)




    def showModifyForm(self):
        functions.centerWindow(self.updateMainWindow)
        self.disableAllButtons()
        self.custUpdateUi.lineEditSearchCustId.textChanged.connect(self.custIdTextChangedAction)
        self.custUpdateUi.comboBoxSearchChoice.currentIndexChanged.connect(self.comboSearchAction)
        self.custUpdateUi.lineEditSearchCustomer.textChanged.connect(self.searchCustAction)
        # self.custUpdateUi.lineEditSearchCustomer.returnPressed.connect(self.searchCustAction)
        self.custUpdateUi.tableWidgetCust.clicked.connect(self.custTableClickedAction)
        self.custUpdateUi.tableWidgetRepairJob.clicked.connect(self.repairTableClickedAction)
        self.custUpdateUi.tableWidgetRepairJob.doubleClicked.connect(self.repairTableDoubleClickedAction)
        self.custUpdateUi.pushButtonAdd.clicked.connect(self.addRepairJobAction)
        self.custUpdateUi.pushButtonUpdate.clicked.connect(self.updateButtonAction)
        self.custUpdateUi.pushButtonDelete.clicked.connect(self.deleteButtonAction)
        self.custUpdateUi.pushButtonFixed.clicked.connect(self.fixedButtonClickedAction)
        self.custUpdateUi.pushButtonUnfixed.clicked.connect(self.unfixedButtonClicked)
        self.custUpdateUi.pushButtonReturned.clicked.connect(self.returnedButtonClickedAction)
        self.updateMainWindow.show()
        self.custUpdateUi.tableWidgetCust.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.custUpdateUi.tableWidgetRepairJob.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.custUpdateUi.tableWidgetRepairJob.hideColumn(2)
        self.custUpdateUi.tableWidgetRepairJob.hideColumn(0)
        # self.custUpdateUi.tableWidgetCust.hideColumn(0)


    def searchCustAction(self):
        self.disableAllButtons()
        self.custUpdateUi.tableWidgetCust.clearContents()
        self.custUpdateUi.tableWidgetRepairJob.clearContents()
        self.custUpdateUi.tableWidgetCust.setRowCount(0)
        self.custUpdateUi.tableWidgetRepairJob.setRowCount(0)
        searchedText = str(self.custUpdateUi.lineEditSearchCustomer.text())
        if searchedText == '':
            return
        if self.searchChoice=='name':
            self.allValuesForSearch = self.db.retrieveSearchedRecords(allstrings.customersTableName,
                                                                      allstrings.customer_name_column, searchedText)
            self.updateCustTableWidget(self.allValuesForSearch)
        elif self.searchChoice=='number':
            self.allValuesForSearch = self.db.retrieveSearchedRecords(allstrings.customersTableName,
                                                                      allstrings.customer_phone_number_column, searchedText)
            self.updateCustTableWidget(self.allValuesForSearch)
        elif self.searchChoice=='item':
            self.itemSearchValues = self.db.retrieveSearchedRecords(allstrings.repairJobsTableName,
                                                                    allstrings.repair_job_item_name,searchedText)
            self.itemSearchAction(searchedText)


    def comboSearchAction(self):
        self.removeDatePushbuttons()
        self.custUpdateUi.lineEditSearchCustomer.setVisible(True)
        self.custUpdateUi.lineEditSearchCustomer.setText('')
        self.custUpdateUi.tableWidgetCust.clearContents()
        self.custUpdateUi.tableWidgetRepairJob.clearContents()
        self.custUpdateUi.tableWidgetCust.setRowCount(0)
        self.custUpdateUi.tableWidgetRepairJob.setRowCount(0)
        self.searchChoice  = self.searchChoiceList[self.custUpdateUi.comboBoxSearchChoice.currentIndex()]

        if self.searchChoice == 'date':
            self.dateSelectedAction()
            return
        if self.searchChoice=='item':
            self.custUpdateUi.lineEditSearchCustomer.setPlaceholderText('Search Repair Job')
        if self.searchChoice == 'name':
            self.custUpdateUi.lineEditSearchCustomer.setPlaceholderText('Search Customer Name')
        if self.searchChoice == 'number':
            self.custUpdateUi.lineEditSearchCustomer.setPlaceholderText('Search Customer Number')



        # self.allValuesForSearch = self.getAllValuesForSearch(self.searchChoice)
        #
        # # change this later to accommodate id
        # # self.tempAllValues = [x[1] for x in self.allValuesForSearch]
        # self.tempAllValues = self.allValuesForSearch
        # self.completerModel.setStringList(self.allValuesForSearch)
        # self.completer.setModel(self.completerModel)

    def itemSearchAction(self,searchedText):
        searchedText = str(searchedText)
        repairTable = self.custUpdateUi.tableWidgetRepairJob
        repairTable.setRowCount(0)
        if searchedText == '':
            return
        data = self.db.retrieveSearchedRecords(allstrings.repairJobsTableName,allstrings.repair_job_item_name,searchedText)
        data = functions.dbListTupleToListDict(data,allstrings.repairJobsTableName)
        repairTable.setRowCount(len(data))
        rowToAdd = 0
        for i in data:
            idItem = QtGui.QTableWidgetItem()
            idItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            nameItem = idItem.clone()
            custItem = idItem.clone()
            billItem = idItem.clone()
            infoItem = idItem.clone()
            paidItem = idItem.clone()
            statusItem = idItem.clone()
            dateReceivedItem = idItem.clone()
            dateReturened = idItem.clone()

            idItem.setText(str(i[allstrings.allid_column]))
            nameItem.setText(str(i[allstrings.repair_job_item_name]))
            custItem.setText(str(i[allstrings.repair_job_customer_id]))
            billItem.setText(str(i[allstrings.repair_job_bill]))
            infoItem.setText(str(i[allstrings.repair_job_other_info]))
            paidItem.setText(str(i[allstrings.repair_job_bill_paid]))
            statusItem.setText(str(i[allstrings.repair_job_status]))
            dateReceivedItem.setText(str(i[allstrings.date_added_column]))
            dateReturened.setText(str(i[allstrings.repair_job_date_returned]))

            repairTable.setItem(rowToAdd,0,idItem)
            repairTable.setItem(rowToAdd,1,nameItem)
            repairTable.setItem(rowToAdd,2,custItem)
            repairTable.setItem(rowToAdd,3,billItem)
            repairTable.setItem(rowToAdd,4,infoItem)
            repairTable.setItem(rowToAdd,5,paidItem)
            repairTable.setItem(rowToAdd,6,statusItem)
            repairTable.setItem(rowToAdd,7,dateReceivedItem)
            repairTable.setItem(rowToAdd,8,dateReturened)
            rowToAdd = rowToAdd + 1
#**************************************SEARCH CUST ID *********************************
    def custIdTextChangedAction(self):
        self.custUpdateUi.tableWidgetCust.setRowCount(0)
        self.custUpdateUi.tableWidgetRepairJob.setRowCount(0)
        statusBar = self.custUpdateUi.statusbar
        statusBar.showMessage('')
        searchText = str(self.custUpdateUi.lineEditSearchCustId.text())
        if not functions.isNumber(searchText):
            statusBar.showMessage('Please enter enter a valid id number')
        if searchText == '':
            statusBar.showMessage('')
        if functions.isNumber(searchText):
            allOk = self.updateCustTableUsingIdSearched(searchText)
            if not allOk:
                statusBar.showMessage('Sorry that id does not exist')

    def updateCustTableUsingIdSearched(self,searchedId):
        dbCustTableName = allstrings.customersTableName
        db = self.db
        custTable = self.custUpdateUi.tableWidgetCust
        custTable.clearContents()
        data = db.retrieveRecordUsingId(dbCustTableName,int(searchedId))
        if data==[] or data == None:
            return False
        data = functions.dbListTupleToListDict(data,dbCustTableName)
        data = data[0]
        custTable.setRowCount(1)
        idItem = QtGui.QTableWidgetItem(str(data[allstrings.allid_column]))
        idItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        nameItem = QtGui.QTableWidgetItem(str(data[allstrings.customer_name_column]))
        mobile1 = QtGui.QTableWidgetItem(str(data[allstrings.customer_phone_number_column]))
        mobile2 = QtGui.QTableWidgetItem(str(data[allstrings.customer_other_number_column]))
        dateAddedItem = QtGui.QTableWidgetItem(str(data[allstrings.date_added_column]))
        dateAddedItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)

        custTable.setItem(0,0,idItem)
        custTable.setItem(0,1,nameItem)
        custTable.setItem(0,2,mobile1)
        custTable.setItem(0,3,mobile2)
        custTable.setItem(0,4,dateAddedItem)
        return True
#***************************************************************************************


    def updateCustTableWidget(self, searchedResults):
        table = self.custUpdateUi.tableWidgetCust
        table.showColumn(0)
        count = 0
        # TODO FINISH THIS
        rowCount = len(searchedResults)
        if not rowCount>0:
            return
        table.setRowCount(rowCount)
        for i in searchedResults:
            for j in xrange(table.columnCount()):
                itemToSave = QtGui.QTableWidgetItem(str(i[j]))
                if any([j==0, j==4]):
                    itemToSave.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                table.setItem(count,j,itemToSave)
            count= count+1
        count = 0
        # table.hideColumn(0)


    def repairTableClickedAction(self):
        if str(self.custUpdateUi.comboBoxSearchChoice.currentText()).lower() == 'item name':
            tableRep = self.custUpdateUi.tableWidgetRepairJob
            selectedCustomerId = tableRep.item(tableRep.currentRow(),2).text()
            self.updateCustTableFromRepairTable(str(selectedCustomerId))
            self.repairId = int(tableRep.item(tableRep.currentRow(),0).text())
            return
        self.enableRepairButtons()
        self.custUpdateUi.tableWidgetRepairJob.showColumn(0)
        self.idOnTableClicked={}
        self.repairId = int(self.custUpdateUi.tableWidgetRepairJob.selectedItems()[0].text())
        self.idOnTableClicked['repair'] = self.repairId
        self.custUpdateUi.tableWidgetRepairJob.hideColumn(0)

    def updateCustTableFromRepairTable(self,custid):
        custTable = self.custUpdateUi.tableWidgetCust
        data = self.db.retrieveRecordUsingId(allstrings.customersTableName,custid)
        data = functions.dbListTupleToListDict(data,allstrings.customersTableName)
        data = data[0]
        custTable.setRowCount(1)

        idItem = QtGui.QTableWidgetItem()
        nameItem = idItem.clone()
        mobileItem1 = idItem.clone()
        mobileItem2 = idItem.clone()
        dateAddedItem = idItem.clone()

        idItem.setText(str(data[allstrings.allid_column]))
        nameItem.setText(str(data[allstrings.customer_name_column]))
        mobileItem1.setText(str(data[allstrings.customer_phone_number_column]))
        mobileItem2.setText(str(data[allstrings.customer_other_number_column]))
        dateAddedItem.setText(str(data[allstrings.date_added_column]))

        custTable.setItem(0,0,idItem)
        custTable.setItem(0,1,nameItem)
        custTable.setItem(0,2,mobileItem1)
        custTable.setItem(0,3,mobileItem2)
        custTable.setItem(0,4,dateAddedItem)





    def custTableClickedAction(self):
        if str(self.custUpdateUi.comboBoxSearchChoice.currentText()).lower() == 'item name':
            self.enableCustButtons()
            custtable = self.custUpdateUi.tableWidgetCust
            self.customerId = int(custtable.item(custtable.currentRow(),0).text())
            self.idOnTableClicked['customer'] = self.customerId
            #TODO FINISH THIS
            return
        self.custUpdateUi.tableWidgetCust.showColumn(0)
        self.idOnTableClicked = {}
        self.custUpdateUi.tableWidgetRepairJob.clearContents()
        self.customerId = int(self.custUpdateUi.tableWidgetCust.selectedItems()[0].text())
        self.idOnTableClicked['customer'] = self.customerId
        repairVals = self.db.retrieveRecord(allstrings.repairJobsTableName,{allstrings.repair_job_customer_id:self.customerId})
        self.updateRepairTableWidget(repairVals)
        self.enableCustButtons()
        # self.custUpdateUi.tableWidgetCust.hideColumn(0)


    def updateRepairTableWidget(self,vals):
        table = self.custUpdateUi.tableWidgetRepairJob
        table.showColumn(0)
        table.showColumn(2)
        rowCount = len(vals)
        count = 0
        table.setRowCount(rowCount)
        for i in vals:
            for j in xrange(table.columnCount()):
                itemToSave = QtGui.QTableWidgetItem(str(i[j]))
                itemToSave.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                table.setItem(count,j,itemToSave)
            count = count+1
        count = 0
        table.hideColumn(2)
        table.hideColumn(0)

    def getAllValuesForSearch(self, choice):
        tableName = allstrings.customersTableName
        allValues = self.db.retrieveAllVals(tableName)
        if choice == 'name':
            allValues = [x[1] for x in allValues]
            return allValues
        elif choice == 'number':
            allValues = [x[2] for x in allValues]
            return allValues

        if not allValues == []:
            pass

    def addRepairJobAction(self):
        self.addRepairObj = AddItemFunctions(self.updateMainWindow,self.db)
        self.addRepairObj.showAddItemForm()
        self.addRepairObj.addItemUi.pushButtonOk.clicked.connect(self.addRepairOkButtonAction)

    def addRepairOkButtonAction(self):
        data = self.addRepairObj.pushButtonOkAction()
        if data == {}:
            self.addRepairObj.addItemWindow.statusBar().showMessage('Please check your inputs and try again!')
            return
        self.addDataToUpdateForm(data)

    def addDataToUpdateForm(self,data):
        repairTable = self.custUpdateUi.tableWidgetRepairJob
        repairTable.showColumn(0)
        rowCount = repairTable.rowCount()
        repairTable.setRowCount(rowCount+1)

        itemTempId = functions.getLockedTableItem('0')
        itemName = functions.getLockedTableItem(str(data['name']))
        fault = functions.getLockedTableItem(str(data['fault']))
        bill = functions.getLockedTableItem(str(data['bill']))
        paid = functions.getLockedTableItem(str(data['paid']))
        custid = functions.getLockedTableItem('0')
        status = functions.getLockedTableItem('BROKEN')
        datereceived = functions.getLockedTableItem(data['today'])
        datereturned = QtGui.QTableWidgetItem('NOT YET')

        repairTable.setItem(rowCount,0,itemTempId)
        repairTable.setItem(rowCount,1,itemName)
        repairTable.setItem(rowCount,2,custid)
        repairTable.setItem(rowCount,3,bill)
        repairTable.setItem(rowCount,4,fault)
        repairTable.setItem(rowCount,5, paid)
        repairTable.setItem(rowCount,6, status)
        repairTable.setItem(rowCount,7,datereceived)
        repairTable.setItem(rowCount,8,datereturned)

        self.addRepairObj.addItemWindow.close()
        self.addRepairObj = ''
        repairTable.hideColumn(0)


    def addDatePushButtons(self):
        self.firstDate = QtGui.QPushButton('Select From Date')
        self.secondDate = QtGui.QPushButton('Select To Date (Optional)')
        self.custUpdateUi.horizontalLayout.insertWidget(2,self.firstDate)
        self.custUpdateUi.horizontalLayout.insertWidget(3,self.secondDate)
        self.secondDate.setEnabled(False)
        self.firstDate.clicked.connect(lambda: self.showDateDialog('first'))
        self.secondDate.clicked.connect(lambda: self.showDateDialog('second'))

    def removeDatePushbuttons(self):
        if self.firstDate:
            self.firstDate.setVisible(False)
        if self.secondDate:
            self.secondDate.setVisible(False)

    def showDateDialog(self, btn):
        self.dateDialogObj = DateSelectFunctions(self.updateMainWindow)
        self.dateDialogObj.dateUi.pushButtonOk.clicked.connect(lambda: self.okButtonDateAction(btn))
        self.dateDialogObj.dateUi.pushButtonCancel.clicked.connect(self.cancelButtonDateAction)

    def okButtonDateAction(self, btn):
        self.custUpdateUi.tableWidgetCust.clearContents()
        self.custUpdateUi.tableWidgetCust.setRowCount(0)
        dateChosen = self.dateDialogObj.dateUi.calendarWidget.selectedDate()
        year = dateChosen.year()
        month = dateChosen.month()
        day = dateChosen.day()
        # dateStr = str(year)+'-'+str(month)+'-'+str(day)
        self.dateStrSelected = str(datetime.date(year,month,day))
        if btn=='first':
            self.firstDate.setText(self.dateStrSelected)
            self.secondDate.setEnabled(True)
        elif btn=='second':
            self.secondDate.setText(self.dateStrSelected)
        self.populateTableUsingDate(btn)
        self.dateDialogObj.dateWindow.close()

    def cancelButtonDateAction(self):
        self.dateDialogObj.dateWindow.close()



    def populateTableUsingDate(self, btn):
        if btn=='first':
            firstDate = str(self.firstDate.text())
            d = self.db.retrieveSearchedRecords(allstrings.customersTableName,
                                                allstrings.customer_date_receieved_column,firstDate)
            self.updateCustTableWidget(d)
        elif btn=='second':
            firstDate = str(self.firstDate.text())
            secondDate = str(self.secondDate.text())
            d = self.db.retrieveSearchedRecordsBetweenDates(allstrings.customersTableName,
                                                        allstrings.customer_date_receieved_column,
                                                        firstDate, secondDate)
            self.updateCustTableWidget(d)





    def dateSelectedAction(self):
        self.custUpdateUi.lineEditSearchCustomer.setVisible(False)
        self.addDatePushButtons()


    # TODO
    def deleteButtonAction(self):
        whichTable = self.idOnTableClicked.keys()[0]
        if whichTable == 'customer':
            confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Delete Customer',
                                'Do you really want to delete this customer (cannot be undone!!)?',
                                QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if confirm == QtGui.QMessageBox.No:
                return

            self.loginStaff('deleteCustomer')


        elif whichTable=='repair':
            confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Delete Repair Item',
                                'Do you really want to delete this Job (cannot be undone!!)?',
                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if confirm== QtGui.QMessageBox.No:
                return
            self.loginStaff('deleteJob')



#**************************************************LOGIN STAFF *************************************************
    def loginStaff(self,flag):
        self.staffObj.showLoginDialog()
        self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(lambda: self.confirmLogin(flag))

    def confirmLogin(self,flag):
        if self.staffObj.loginClickedAction():
            self.staffObj.loginWindow.close()
            if flag=='deleteJob':

                jobName = str(self.custUpdateUi.tableWidgetRepairJob.item(self.custUpdateUi.tableWidgetRepairJob.currentRow(),1).text())
                custnm = str(self.custUpdateUi.tableWidgetCust.item(self.custUpdateUi.tableWidgetCust.currentRow(),1).text())

                self.db.deleteRecord(allstrings.repairJobsTableName,self.idOnTableClicked['repair'])
                self.custUpdateUi.tableWidgetRepairJob.removeRow(self.custUpdateUi.tableWidgetRepairJob.currentRow())
                QtGui.QMessageBox.information(QtGui.QMessageBox(),'Deleted',
                                                    'Deleted',QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)



                self.logObj.writeToLog('\nDeleted repair job \nJob Name: '+jobName+'\nCustomer: '+custnm,self.staffObj.getStaffName())
            if flag=='deleteCustomer':
                custnm = str(self.custUpdateUi.tableWidgetCust.item(self.custUpdateUi.tableWidgetCust.currentRow(),1).text())
                self.db.deleteRecord(allstrings.customersTableName,self.idOnTableClicked['customer'])
                self.db.deleteRecordUsingValue(allstrings.repairJobsTableName,
                                               allstrings.repair_job_customer_id,self.idOnTableClicked['customer'])
                self.custUpdateUi.tableWidgetCust.removeRow(self.custUpdateUi.tableWidgetCust.currentRow())
                self.custUpdateUi.tableWidgetRepairJob.clearContents()
                self.custUpdateUi.tableWidgetRepairJob.setRowCount(0)

                QtGui.QMessageBox.information(QtGui.QMessageBox(),'Deleted',
                                    'Deleted',QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

                self.logObj.writeToLog('\nDeleted Customer \nCustomer Name: '+custnm,self.staffObj.getStaffName())
            if flag=='update':
                custnm = str(self.custUpdateUi.tableWidgetCust.item(self.custUpdateUi.tableWidgetCust.currentRow(),1).text())
                self.custUpdateUi.tableWidgetRepairJob.showColumn(0)
                self.custUpdateUi.tableWidgetRepairJob.showColumn(2)
                self.custUpdateUi.tableWidgetCust.showColumn(0)
                custTable = self.custUpdateUi.tableWidgetCust
                table = self.custUpdateUi.tableWidgetRepairJob
                repairRow = table.rowCount()
                tempr = []
                r = [str(y.text()) for y in custTable.selectedItems()]
                customerId = r[0]
                custName = r[1]
                custPhone = r[2]
                custPhone2 = r[3]
                custDateAdded = r[4]

                d = [str(x.text()) for x in table.selectedItems()]

                for i in xrange(repairRow):
                    table.selectRow(i)
                    t = [str(x.text()) for x in table.selectedItems()]
                    tempr.append(t)
                for j in tempr:
                    id = j[0]
                    itemName = j[1]
                    custId = customerId
                    bill = j[3]
                    fault = j[4]
                    paid = j[5]
                    status = j[6]
                    dateReceived = j[7]
                    dateReturned = j[8]

                    custDict = {allstrings.customer_name_column:custName, allstrings.customer_phone_number_column:custPhone,
                                allstrings.customer_other_number_column:custPhone2,
                                allstrings.customer_date_receieved_column:custDateAdded}

                    repairJobDict = {allstrings.repair_job_item_name:itemName, allstrings.repair_job_customer_id:custId,
                                     allstrings.repair_job_bill:bill, allstrings.repair_job_other_info:fault,
                                     allstrings.repair_job_bill_paid:paid, allstrings.repair_job_status:status,
                                     allstrings.repair_job_date_received:dateReceived,
                                     allstrings.repair_job_date_returned:dateReturned}

                    self.db.modifyCustomers(custDict, id=int(customerId))

                    if id=='0':
                        self.db.modifyRepairJobs(repairJobDict, status='add')
                    else:
                        self.db.modifyRepairJobs(repairJobDict, id=id)


                self.custUpdateUi.tableWidgetRepairJob.hideColumn(0)
                self.custUpdateUi.tableWidgetRepairJob.hideColumn(2)
                # self.custUpdateUi.tableWidgetCust.hideColumn(0)
                QtGui.QMessageBox.information(QtGui.QMessageBox(),'Updated','Customer Updated!',
                                                        QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                self.logObj.writeToLog('\nUpdated Customer \nCustomer Name: '+custnm,self.staffObj.getStaffName())

#***************************************************************************************************************



    def updateButtonAction(self):
        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Update Item','Do you want to update this customer?',
                                                QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if confirm == QtGui.QMessageBox.No:
            return
        self.loginStaff('update')





    def repairTableDoubleClickedAction(self):
        if str(self.custUpdateUi.comboBoxSearchChoice.currentText()).lower() == 'item name':
            customerid = self.custUpdateUi.tableWidgetRepairJob.item(self.custUpdateUi.tableWidgetRepairJob.currentRow(),2)
            jobid = self.custUpdateUi.tableWidgetRepairJob.item(self.custUpdateUi.tableWidgetRepairJob.currentRow(),0)
            self.repairDoubleClickForItem(customerid,jobid)
            return
        self.addRepairObj2 = AddItemFunctions(self.updateMainWindow,self.db)
        self.custUpdateUi.tableWidgetCust.showColumn(0)
        self.custUpdateUi.tableWidgetRepairJob.showColumn(0)
        self.custUpdateUi.tableWidgetRepairJob.showColumn(2)
        custrw = self.custUpdateUi.tableWidgetCust.currentRow()
        self.reprow = self.custUpdateUi.tableWidgetRepairJob.currentRow()
        custid = self.custUpdateUi.tableWidgetCust.item(custrw,0).text()
        custname = self.custUpdateUi.tableWidgetCust.item(custrw,1).text()
        itemName = self.custUpdateUi.tableWidgetRepairJob.item(self.reprow,1).text()
        itemFault = self.custUpdateUi.tableWidgetRepairJob.item(self.reprow,4).text()
        imeiNumber = ''
        # GET OUT IMEI
        if '|' in str(itemFault):
            l = str(itemFault).split('|')
            imeiNumber = l[1].strip()
            itemFault = l[0].strip()
        itemBill = self.custUpdateUi.tableWidgetRepairJob.item(self.reprow,3).text()
        itemPaid = self.custUpdateUi.tableWidgetRepairJob.item(self.reprow,5).text()
        self.addRepairObj2.showAddItemForm()
        self.addRepairObj2.addItemWindow.setWindowTitle('UPDATE CUSTOMER ['+str(custname).upper()+']')
        self.addRepairObj2.addItemUi.pushButtonOk.setText('Update')
        self.addRepairObj2.addItemUi.pushButtonOk.clicked.connect(self.pushButtonUpdateOnAddRepaiForm)
        self.addRepairObj2.addItemUi.lineEditItemName.setText(itemName)
        self.addRepairObj2.addItemUi.textEditFault.setText(itemFault)
        self.addRepairObj2.addItemUi.lineEditBill.setText(itemBill)
        self.addRepairObj2.addItemUi.lineEditPaid.setText(itemPaid)
        self.addRepairObj2.addItemUi.lineEditImeiNumber.setText(imeiNumber)
        # self.custUpdateUi.tableWidgetCust.hideColumn(0)
        self.custUpdateUi.tableWidgetRepairJob.hideColumn(0)
        self.custUpdateUi.tableWidgetRepairJob.hideColumn(2)


    def pushButtonUpdateOnAddRepaiForm(self):
        itemName = self.addRepairObj2.addItemUi.lineEditItemName.text()
        fault = self.addRepairObj2.addItemUi.textEditFault.toPlainText()
        bill = self.addRepairObj2.addItemUi.lineEditBill.text()
        paid = self.addRepairObj2.addItemUi.lineEditPaid.text()
        imei = str(self.addRepairObj2.addItemUi.lineEditImeiNumber.text())

        if not imei=='':
            if not functions.isNumber(imei):
                self.addRepairObj2.addItemUi.statusbar.showMessage('Please check your inputs and try again!!')
                return
            else:
                fault= str(fault)+' | '+str(imei)


        if any([itemName=='',fault=='',bill=='', not functions.isNumber(bill),paid=='',not functions.isNumber(paid)]):
            self.addRepairObj2.addItemUi.statusbar.showMessage('Please check your inputs and try again!!')
            return


        itemName = QtGui.QTableWidgetItem(itemName)
        itemName.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        fault = QtGui.QTableWidgetItem(fault)
        fault.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        bill = QtGui.QTableWidgetItem(str(bill))
        bill.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        paid = QtGui.QTableWidgetItem(str(paid))
        paid.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)



        self.custUpdateUi.tableWidgetRepairJob.setItem(self.reprow, 1, itemName)
        self.custUpdateUi.tableWidgetRepairJob.setItem(self.reprow, 3, bill)
        self.custUpdateUi.tableWidgetRepairJob.setItem(self.reprow, 4, fault)
        self.custUpdateUi.tableWidgetRepairJob.setItem(self.reprow, 5, paid)
        self.addRepairObj2.addItemWindow.close()


#**********************************************FIXED, UNFIXED AND RETURN FUNCTIONS*********************************
    def fixedButtonClickedAction(self):
        table = self.custUpdateUi.tableWidgetRepairJob
        itemStatus = table.item(table.currentRow(),6).text()
        itemStatus = str(itemStatus).lower()
        if 'fixed' in itemStatus:
            return
        if 'broken' in itemStatus:
            itemStatus = itemStatus.replace('broken','fixed')
        elif itemStatus == '':
            itemStatus = 'fixed'
        else:
            itemStatus = itemStatus+' | fixed'
        itemStatus = itemStatus.upper()

        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        item.setText(itemStatus)
        table.setItem(table.currentRow(),6,item)

    def unfixedButtonClicked(self):
        table = self.custUpdateUi.tableWidgetRepairJob
        itemStatus = table.item(table.currentRow(),6).text()
        itemStatus = str(itemStatus).lower()

        if 'broken' in itemStatus:
            return
        if 'fixed' in itemStatus:
            itemStatus = itemStatus.replace('fixed','broken')
        elif itemStatus == '':
            itemStatus = 'broken'
        else:
            itemStatus = itemStatus+' | broken'
        itemStatus = itemStatus.upper()

        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        item.setText(itemStatus)
        table.setItem(table.currentRow(),6,item)


    def returnedButtonClickedAction(self):
        table = self.custUpdateUi.tableWidgetRepairJob
        itemStatus = table.item(table.currentRow(),6).text()
        itemStatus = str(itemStatus).lower()

        if 'returned' in itemStatus:
            return
        if itemStatus == '':
            itemStatus = 'returned'
        else:
            itemStatus = itemStatus+' | returned'
        itemStatus = itemStatus.upper()

        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        itemDate = item.clone()

        itemDate.setText(str(datetime.datetime.now()))
        item.setText(itemStatus)
        table.setItem(table.currentRow(),6,item)
        table.setItem(table.currentRow(),8,itemDate)

#************************************************************************************************************************







#
# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     updateOp = ModifyOperations()
#     updateOp.showModifyForm()
#     sys.exit(app.exec_())