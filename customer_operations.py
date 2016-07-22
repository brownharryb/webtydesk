import datetime

from PyQt4 import QtGui,QtCore
from forms.custinfo import Ui_custInfoWindow
from addItem_operation import AddItemFunctions
from staff_functions import StaffObject
from log.custom_log import LogObj
from misc import allstrings, functions

from repair_jobs_operation import RepairJobFunctions





class CustomerFunctions():

    def __init__(self,parent,db):
        self.db = db
        self.parent = parent
        self.setupAllObj()
        self.staffObj = StaffObject(self.custInfoWindow,self.db)
        self.logObj = LogObj()


    def setupAllObj(self):
        self.custui = Ui_custInfoWindow()
        self.custInfoWindow = QtGui.QMainWindow(self.parent)
        self.repairJobObj = RepairJobFunctions()
        self.addItemObj = AddItemFunctions(self.custInfoWindow,self.db)
        self.dbIdForCustUpdate = 0



    def showCustForm(self):
        self.custui.setupUi(self.custInfoWindow)
        functions.centerWindow(self.custInfoWindow)
        self.custInfoWindow.show()
        self.custui.tableWidgetAddedItems.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.custui.pushButtonAddnew.clicked.connect(self.showAddItemWindow)
        # self.custui.pushButtonSave.clicked.connect(self.saveButtonAction)
        self.custui.pushButtonDeleteItem.clicked.connect(self.deleteButtonAction)


    def allInputsValid(self):

        try:
            self.customerName = functions.cleanCustomerName(str(self.custui.lineEditName.text()))
            self.customerMobileNumber = functions.cleanCustomerMobileNumber(str(self.custui.lineEditMobileNumber.text()))
            self.customerMobileNumber2 = ''
            if not str(self.custui.lineEditMobileNumber_2.text()) == '':
                self.customerMobileNumber2 = functions.cleanCustomerMobileNumber(str(self.custui.lineEditMobileNumber_2.text()))
            self.dbIdForCustUpdate = self.checkIfCustomerInDb(self.customerName,[self.customerMobileNumber,
                                                                                 self.customerMobileNumber2])
            return True
        except ValueError:
            return False

    def showAddItemWindow(self):
        self.addItemObj = AddItemFunctions(self.custInfoWindow,self.db)
        if self.allInputsValid():
            if self.dbIdForCustUpdate>0:
                reply = QtGui.QMessageBox.information(QtGui.QMessageBox(),
                                                    'Customer Exists',"Sorry I can't do that,this Customer Already exists, "
                                                                      "\nPlease modify jobs instead to update!!",
                                                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                return
            self.addItemObj.showAddItemForm(customerName=self.customerName)
            self.addItemObj.addItemUi.pushButtonOk.clicked.connect(self.okButtonClickedOnAddItem)
        else:
            self.custInfoWindow.statusBar().showMessage('One or more inputs are empty or invalid!!')

    def okButtonClickedOnAddItem(self):
        data = self.addItemObj.pushButtonOkAction()
        if data == {}:
            self.addItemObj.addItemWindow.statusBar().showMessage('Please check your inputs and try again!')
            return
        self.addDataToTableInCustomerForm(data)

    def deleteButtonAction(self):
        if not self.custui.comboBoxNumberToDelete.isEnabled():
            return
        numberToDelete = int(self.custui.comboBoxNumberToDelete.currentText())
        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Delete',
                    'Do you really want to delete item at '+str(numberToDelete)+'?',
                    QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if confirm==QtGui.QMessageBox.Yes:
            self.custui.tableWidgetAddedItems.removeRow(numberToDelete-1)
            c = self.custui.comboBoxNumberToDelete.count()
            self.custui.comboBoxNumberToDelete.removeItem(c-1)
            if self.custui.comboBoxNumberToDelete.count() == 0:
                self.custui.comboBoxNumberToDelete.setEnabled(False)

    def saveButtonAction(self):
        if not self.allInputsValid():
            self.custInfoWindow.statusBar().showMessage('Please check your inputs and try again!')
            return
        if not self.custui.tableWidgetAddedItems.rowCount()>0:
            self.custInfoWindow.statusBar().showMessage('No Repair Items Added!')
            return
        self.addDataToDb()



    def checkIfCustomerInDb(self, customerName,customerNumberList):
        # TODO CHECK FOR PHONE NUMBER TWO
        j=[]
        p = self.db.retrieveRecord(allstrings.customersTableName,{allstrings.customer_name_column:customerName})
        if not p==[]:
            return p[0][0]
        for i in customerNumberList:
            j = self.db.retrieveRecord(allstrings.customersTableName, {allstrings.customer_phone_number_column:i})

            if not j == []:
                break
        try:
            return j[0][0]
        except:
            return 0



    def addDataToTableInCustomerForm(self,data):
        rowCount = self.custui.tableWidgetAddedItems.rowCount()
        row = rowCount+1
        name = data['name']
        additionalInfo = data['additionalInfo']
        imei = data['imei_serial']
        bill = data['bill']
        paid = data['paid']
        today = data['today']
        status = data['status']
        knownFaults= data['knownFaults']

        self.custui.tableWidgetAddedItems.setRowCount(row)

        self.custui.tableWidgetAddedItems.setItem(rowCount,0,QtGui.QTableWidgetItem(QtCore.QString(name)))
        self.custui.tableWidgetAddedItems.setItem(rowCount,1,QtGui.QTableWidgetItem(QtCore.QString(knownFaults)))
        self.custui.tableWidgetAddedItems.setItem(rowCount,2,QtGui.QTableWidgetItem(QtCore.QString(str(bill))))
        self.custui.tableWidgetAddedItems.setItem(rowCount,3,QtGui.QTableWidgetItem(QtCore.QString(str(paid))))
        self.custui.tableWidgetAddedItems.setItem(rowCount,4,QtGui.QTableWidgetItem(QtCore.QString(status)))
        self.custui.tableWidgetAddedItems.setItem(rowCount,5,QtGui.QTableWidgetItem(QtCore.QString(str(today))))
        self.custui.tableWidgetAddedItems.setItem(rowCount,6,QtGui.QTableWidgetItem(QtCore.QString('---')))
        self.custui.tableWidgetAddedItems.setItem(rowCount,7,QtGui.QTableWidgetItem(QtCore.QString(str(imei))))
        self.custui.tableWidgetAddedItems.setItem(rowCount,8,QtGui.QTableWidgetItem(QtCore.QString(additionalInfo)))

        self.custui.comboBoxNumberToDelete.setEnabled(True)
        self.custui.comboBoxNumberToDelete.addItem(str(row))


        self.addItemObj.addItemWindow.close()
        # DESTROY THIS OBJECT
        self.addItemObj=''


    def addDataToDb(self):
        try:
            allItemsList = self.getAllItemsFromTableWidget()
            custRecordDict = {}

            custName = self.customerName
            custNumber = self.customerMobileNumber
            custNumber2 = self.customerMobileNumber2


            custRecordDict[allstrings.customer_name_column] = custName
            custRecordDict[allstrings.customer_phone_number_column]= custNumber
            custRecordDict[allstrings.customer_other_number_column] = custNumber2
            custRecordDict[allstrings.customer_date_receieved_column] = functions.getDateString(datetime.datetime.now())



            confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Save Customer','Save Customer?',
                                                        QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
            if confirm==QtGui.QMessageBox.No:
                return
            self.loginToAddToDb(custRecordDict,allItemsList)

        except:
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Nothin Saved','Something went wrong, Nothing was saved!!',
                                                        QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)

#************************************ LOGIN TO ADD TO DB *********************************************************

    def loginToAddToDb(self,custRecordDict,allItemsList):
        self.staffObj.showLoginDialog()
        self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(lambda: self.loginStaff(custRecordDict,allItemsList))



    def loginStaff(self,custRecordDict,allItemsList):
        if self.staffObj.loginClickedAction():
            self.staffObj.loginWindow.close()
            custid = self.db.modifyCustomers(custRecordDict,status='add')

            for i in allItemsList:
                i[allstrings.repair_job_customer_id] = custid
                self.db.modifyRepairJobs(i,status='add')
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Saved','Customer Saved! \n TAG NUMBER ='+str(custid),
                                                        QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)

            self.custInfoWindow.close()
            itms = [x[allstrings.repair_job_item_name] for x in allItemsList]
            msg = '\nAdded Item for Repair \nCustomer Name: '+self.customerName+' \nItems Added: '+str(itms)+'.'
            self.logObj.writeToLog(msg,self.staffObj.getStaffName())
        else:
            pass

#*****************************************************************************************************************





    def getAllItemsFromTableWidget(self):
        l = []
        d = {}
        for i in xrange(self.custui.tableWidgetAddedItems.rowCount()):
            d[allstrings.repair_job_item_name] = str(self.custui.tableWidgetAddedItems.item(i,0).text())
            d[allstrings.repair_job_knownfaults] = str(self.custui.tableWidgetAddedItems.item(i,1).text())
            d[allstrings.repair_job_bill] = str(self.custui.tableWidgetAddedItems.item(i,2).text())
            d[allstrings.repair_job_bill_paid] = str(self.custui.tableWidgetAddedItems.item(i,3).text())
            d[allstrings.repair_job_status] = str(self.custui.tableWidgetAddedItems.item(i,4).text())
            d[allstrings.repair_job_date_received] = str(self.custui.tableWidgetAddedItems.item(i,5).text())
            d[allstrings.repair_job_date_returned] = str(self.custui.tableWidgetAddedItems.item(i,6).text())
            d[allstrings.repair_job_imei_serial] = str(self.custui.tableWidgetAddedItems.item(i,7).text())
            d[allstrings.repair_job_other_info] = str(self.custui.tableWidgetAddedItems.item(i,8).text())
            l.append(d)
            d={}
        return l







