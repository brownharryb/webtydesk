import datetime
from misc import allstrings,functions
from forms.parts_form import Ui_dialogSpareParts
from staff_functions import StaffObject
from log.custom_log import LogObj
from PyQt4 import QtGui,QtCore


class SpareParts():


    def __init__(self,db):
        self.db = db
        self.setUpObjs()
        self.logMessage = ''
        self.itemsDeducted = {}
        self.firstLaunch = True
        self.logObj = LogObj()


    def setUpObjs(self):
        self.tableName = allstrings.sparePartsTableName
        self.sparepartName = ''
        self.sparepartQuantity = 0
        self.sparepartUnitPrice = 0
        self.sparepartVendor = ''
        self.sparepartDateAdded = ''


    def getSparePartName(self):
        return self.sparepartName

    def setSparePartName(self,spareName):
        self.sparepartName = spareName

    def getSparePartQuantity(self):
        return self.sparepartQuantity

    def setSparePartQuantity(self,spareQty):
        self.sparepartQuantity = spareQty

    def getSparePartUnitPrice(self):
        return self.sparepartUnitPrice

    def setSpareUnitPrice(self, spareUnitPrice):
        self.sparepartUnitPrice = float(spareUnitPrice)

    def getSpareVendor(self):
        return self.sparepartVendor

    def setSparePartVendor(self,spareVendor):
        self.sparepartVendor = spareVendor

    def getSparePartDateAdded(self):
        return self.sparepartDateAdded

    def setSparePartDateAdded(self,spareDate):
        self.sparepartDateAdded = spareDate

    def getAllSparePartsName(self):
        allVals = functions.dbListTupleToListDict(self.db.retrieveAllVals(self.tableName),self.tableName)
        allNames = [x[allstrings.spareparts_name_column] for x in allVals]
        return allNames

#     TODO FINISH THIS

# ********************************** FOR ADMIN**********************************************
# *********ADD SPARE PARTS*************
    def sparePartsAddSaveButtonClicked(self, addUi, addDialog):
        data = {}
        data[allstrings.spareparts_name_column] = str(addUi.lineEditName.text())
        data[allstrings.spare_quantity_column] = str(addUi.lineEditQuantity.text())
        data[allstrings.spareparts_price_column] = str(addUi.lineEditUnitPrice.text())
        data[allstrings.date_added_column] = datetime.datetime.now()

        if '' in data.values():
            addUi.labelError.setText('Some inputs are empty!')
            addUi.labelError.setVisible(True)
            return

        data[allstrings.spare_vendor_column] = str(addUi.lineEditVendor.text())
        if not functions.isNumber(data[allstrings.spareparts_price_column]):
            addUi.labelError.setText('Numbers only for price')
            addUi.labelError.setVisible(True)
            return
        if not functions.isNumber(data[allstrings.spare_quantity_column]):
            addUi.labelError.setText('Numbers only for quantity')
            addUi.labelError.setVisible(True)
            return

        if self.db.duplicateIsAvailable(self.tableName,{allstrings.spareparts_name_column:
                                                        data[allstrings.spareparts_name_column]}):
            addUi.labelError.setText('Spare part already exists!! ')
            addUi.labelError.setVisible(True)
            return

        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Spare Part','Add Spare Part?',
                                                QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if confirm==QtGui.QMessageBox.Yes:
            self.db.insertNewRecord(self.tableName,data)
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Spare Part','Spare Part Added!',
                                                QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            addDialog.close()
    def sparePartsAddClearButtonClicked(self,addUi):
        addUi.labelError.setVisible(False)
        addUi.lineEditName.setText('')
        addUi.lineEditUnitPrice.setText('')
        addUi.lineEditQuantity.setText('')
        addUi.lineEditVendor.setText('')
# *************************************
# *****************MODIFY SPARE PARTS***********
    def sparePartsCheckComboChanged(self,checkUi):
        currentName = str(checkUi.comboBoxSpareParts.currentText()).lower()
        checkUi.labelDbId.setText('')
        checkUi.lineEditQtyRemaining.setText('')
        checkUi.lineEditUnitPrice.setText('')
        checkUi.lineEditVendor.setText('')
        checkUi.labelError.setVisible(False)
        if checkUi.comboBoxSpareParts.currentIndex() == 0:
            return
        recd= self.db.retrieveRecord(self.tableName,{allstrings.spareparts_name_column:currentName})
        recd = functions.dbListTupleToListDict(recd,self.tableName)[0]
        print 'recd = '+str(recd)
        checkUi.labelDbId.setText(str(recd[allstrings.allid_column]))
        checkUi.lineEditQtyRemaining.setText(str(recd[allstrings.spare_quantity_column]))
        checkUi.lineEditUnitPrice.setText(str(recd[allstrings.spareparts_price_column]))
        checkUi.lineEditVendor.setText(str(recd[allstrings.spare_vendor_column]))

    def sparePartsUpdateClickedAction(self,checkUi,checkDialog):
        if checkUi.comboBoxSpareParts.currentIndex()==0:
            checkUi.labelError.setText('Select a valid name!!')
            checkUi.labelError.setVisible(True)
            return

        data = {}
        idToUpdate = str(checkUi.labelDbId.text())
        data[allstrings.spare_quantity_column] = str(checkUi.lineEditQtyRemaining.text())
        data[allstrings.spareparts_price_column] = str(checkUi.lineEditUnitPrice.text())

        if '' in data.values():
            checkUi.labelError.setText('Some Inputs are empty!!')
            checkUi.labelError.setVisible(True)
            return

        if not functions.isNumber(data[allstrings.spare_quantity_column]):
            checkUi.labelError.setText('Numbers only for quantity!')
            checkUi.labelError.setVisible(True)
            return
        if not functions.isNumber(data[allstrings.spareparts_price_column]):
            checkUi.labelError.setText('Numbers only for price!')
            checkUi.labelError.setVisible(True)
            return
        data[allstrings.spare_vendor_column] = str(checkUi.lineEditVendor.text())

        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Spare Part','Update Spare Part?',
                                                QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if confirm==QtGui.QMessageBox.Yes:
            self.db.updateRecord(self.tableName, data,idToUpdate)
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Spare Part','Spare Part Updated!',
                                                QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            checkDialog.close()

    def sparePartsCheckClearButtonClicked(self,checkUi):
        checkUi.comboBoxSpareParts.setCurrentIndex(0)
        checkUi.labelError.setVisible(False)
        checkUi.lineEditUnitPrice.setText('')
        checkUi.lineEditQtyRemaining.setText('')
        checkUi.lineEditVendor.setText('')
# **********************************************

# *****************************************************************************************
# *********************************************MAIN FRONT FORM********************************
    def showPartsForm(self,parent):
        self.mainFrontPartsUi = Ui_dialogSpareParts()
        self.mainFrontPartsDialog = QtGui.QDialog(parent)
        self.mainFrontPartsUi.setupUi(self.mainFrontPartsDialog)
        self.mainFrontPartsUi.tableWidgetAllParts.hideColumn(0)
        self.mainFrontPartsUi.tableWidgetAllParts.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.mainFrontPartsUi.pushButtonDeduct.setEnabled(False)
        self.mainFrontPartsUi.lineEditQuantityUsed.setEnabled(False)
        self.allVals = functions.dbListTupleToListDict(self.db.retrieveAllVals(self.tableName),self.tableName)
        self.mainFrontPartsUi.lineEditSearchText.textChanged.connect(self.searchedTextAction)
        self.mainFrontPartsUi.tableWidgetAllParts.clicked.connect(self.tableClickedAction)
        self.mainFrontPartsUi.pushButtonDeduct.clicked.connect(self.deductAction)
        self.mainFrontPartsUi.pushButtonCancel.clicked.connect(self.cancelButtoneAction)
        self.mainFrontPartsUi.checkBoxPrice.stateChanged.connect(self.priceCheckAction)
        self.mainFrontPartsUi.checkBoxQuantity.stateChanged.connect(self.quantityCheckAction)
        self.mainFrontPartsUi.checkBoxVendor.stateChanged.connect(self.vendorCheckAction)
        self.mainFrontPartsUi.tableWidgetAllParts.hideColumn(2)
        self.mainFrontPartsUi.tableWidgetAllParts.hideColumn(3)
        self.mainFrontPartsUi.tableWidgetAllParts.hideColumn(4)
        self.qtyEnabled = False
        self.mainFrontPartsDialog.show()

    def priceCheckAction(self):
        checkBox = self.mainFrontPartsUi.checkBoxPrice
        if checkBox.isChecked():
            self.mainFrontPartsUi.tableWidgetAllParts.showColumn(2)
        else:
            self.mainFrontPartsUi.tableWidgetAllParts.hideColumn(2)


    def quantityCheckAction(self):
        checkBox = self.mainFrontPartsUi.checkBoxQuantity
        if checkBox.isChecked():
            self.qtyEnabled = True
            self.mainFrontPartsUi.tableWidgetAllParts.showColumn(3)
        else:
            self.qtyEnabled = False
            self.mainFrontPartsUi.tableWidgetAllParts.hideColumn(3)
            self.mainFrontPartsUi.lineEditQuantityUsed.setEnabled(False)
            self.mainFrontPartsUi.pushButtonDeduct.setEnabled(False)
            self.mainFrontPartsUi.lineEditQuantityUsed.setText('')

    def vendorCheckAction(self):
        checkBox = self.mainFrontPartsUi.checkBoxVendor
        if checkBox.isChecked():
            self.mainFrontPartsUi.tableWidgetAllParts.showColumn(4)
        else:
            self.mainFrontPartsUi.tableWidgetAllParts.hideColumn(4)

    def searchedTextAction(self):
        self.mainFrontPartsUi.tableWidgetAllParts.clearContents()
        self.mainFrontPartsUi.tableWidgetAllParts.setRowCount(0)
        searchedText = str(self.mainFrontPartsUi.lineEditSearchText.text())
        if searchedText <> '':
            self.populateTable(searchedText)

    def populateTable(self,searchedText):
        table = self.mainFrontPartsUi.tableWidgetAllParts
        li = [x for x in self.allVals if str(searchedText).lower() in str(x[allstrings.spareparts_name_column]).lower()]
        table.setRowCount(len(li))
        for i in xrange(len(li)):
            l = li[i]
            itemId = QtGui.QTableWidgetItem()
            itemId.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            itemName = itemId.clone()
            itemPrice = itemId.clone()
            itemQuantitiy = itemId.clone()
            itemVendor = itemId.clone()

            table.setItem(i,0,itemId)
            table.setItem(i,1,itemName)
            table.setItem(i,2,itemPrice)
            table.setItem(i,3,itemQuantitiy)
            table.setItem(i,4,itemVendor)

            itemId.setText(str(l[allstrings.allid_column]))
            itemName.setText(str(l[allstrings.spareparts_name_column]))
            itemPrice.setText(str(l[allstrings.spareparts_price_column]))
            itemQuantitiy.setText(str(l[allstrings.spare_quantity_column]))
            itemVendor.setText(str(l[allstrings.spare_vendor_column]))

    def tableClickedAction(self):
        self.dataFormDict = {}
        table = self.mainFrontPartsUi.tableWidgetAllParts
        if self.qtyEnabled == True:
            self.mainFrontPartsUi.lineEditQuantityUsed.setEnabled(True)
            self.mainFrontPartsUi.pushButtonDeduct.setEnabled(True)
            self.mainFrontPartsUi.lineEditQuantityUsed.setText('1')
        self.dataFormDict[allstrings.allid_column] = str(table.item(table.currentRow(),0).text())
        self.dataFormDict[allstrings.spareparts_name_column]  = str(table.item(table.currentRow(),1).text())
        self.dataFormDict[allstrings.spareparts_price_column] = str(table.item(table.currentRow(),2).text())
        self.dataFormDict[allstrings.spare_quantity_column] = str(table.item(table.currentRow(),3).text())
        self.dataFormDict[allstrings.spare_vendor_column] = str(table.item(table.currentRow(),4).text())
        self.itemsDeducted[self.dataFormDict[allstrings.spareparts_name_column]]=[]

    def deductAction(self):
        amount = self.mainFrontPartsUi.lineEditQuantityUsed.text()
        if not functions.isNumber(amount) or amount =='':
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Invalid Input',
                'Please input a valid number to deduct!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            return
        self.deductedAmount = int(amount)
        self.tableOldAmount = self.dataFormDict[allstrings.spare_quantity_column]

        if int( self.deductedAmount)>int(self.tableOldAmount):
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Invalid Input',
                'Your amount is higher than the available quantity!!!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
            return
        self.saveAction()

    def saveAction(self):
        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Deduct Spareparts','Deduct Spare Part?\nThis cannot be undone.',QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if confirm == QtGui.QMessageBox.Yes:

            self.loginStaff()


    def loginStaff(self):
        self.staffObj = StaffObject(self.mainFrontPartsDialog,self.db)
        self.staffObj.showLoginDialog()
        self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(self.loginClicked)

    def loginClicked(self):
        table = self.mainFrontPartsUi.tableWidgetAllParts
        if self.staffObj.loginClickedAction():
            self.dataFormDict[allstrings.spare_quantity_column] = str(int(self.tableOldAmount) - int(self.deductedAmount))
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(self.dataFormDict[allstrings.spare_quantity_column])
            table.setItem(table.currentRow(),3,item)
            self.db.updateRecord(self.tableName,self.dataFormDict,self.dataFormDict[allstrings.allid_column])
            msg = '\nSparePart deducted \nName: '+str(self.dataFormDict[allstrings.spareparts_name_column])+\
                  '\nQuantiy Used:'+str(self.deductedAmount)
            self.logObj.writeToLog(msg,self.staffObj.getStaffName())
        self.staffObj.loginWindow.close()
        QtGui.QMessageBox.information(QtGui.QMessageBox(),'Parts Deducted',
                str(self.deductedAmount)+' successfully deducted',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)

    def cancelButtoneAction(self):
        self.mainFrontPartsDialog.close()









# ********************************************************************************************