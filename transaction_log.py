from misc import allstrings,functions
from forms.transact_log_admin import Ui_transactLog
from custom_widgets.select_date_functions import DateSelectFunctions
from PyQt4 import QtGui, QtCore


class TransactionLog():

    def __init__(self,parent,db):
        self.db = db
        self.parent = parent
        self.tableName = allstrings.moneyTableName
        self.setUp()



    def setUp(self):
        self.logUi = Ui_transactLog()
        self.logWindow = QtGui.QMainWindow(self.parent)
        self.logUi.setupUi(self.logWindow)
        self.table = self.logUi.tableWidget

    def checkCashPosCheckBoxes(self):
        self.logUi.checkBoxShowCash.setChecked(True)
        self.logUi.checkBoxShowPos.setChecked(True)

#************************HIDE COLUMNS***********************************
    def hideTableColumns(self):
        for i in xrange(6):
            if not i==4:
                self.table.hideColumn(i)
#**************************HIDE BALANCE LABELS ********************
    def viewBalanceLabels(self,False):
        self.logUi.labelReceived.setVisible(False)
        self.logUi.labelSpent.setVisible(False)
        self.logUi.labelBalance.setVisible(False)
        self.logUi.labelTitleBalance.setVisible(False)
        self.logUi.labelTitleExpense.setVisible(False)
        self.logUi.labelTitleIncome.setVisible(False)


#***********************SHOW BALANCE CHECKBOXES**********************
    def showWindow(self):
        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.logUi.pushButtonSelectDate2.setEnabled(False)
        self.hideTableColumns()
        self.viewBalanceLabels(False)
        self.logUi.checkBoxDate.setChecked(True)
        self.logWindow.show()
        self.allActionsTrigger()

    def allActionsTrigger(self):
        self.checkCashPosCheckBoxes()
        self.logUi.pushButtonSelectDate1.clicked.connect(self.firstDateButtonAction)
        self.logUi.pushButtonSelectDate2.clicked.connect(self.secondDateButtonAction)
        self.logUi.checkBoxDate.stateChanged.connect(self.checkboxDateAction)
        self.logUi.checkBoxMedium.stateChanged.connect(self.checkboxMediumAction)
        self.logUi.checkBoxPurpose.stateChanged.connect(self.checkboxPurposeAction)
        self.logUi.checkBoxReceived.stateChanged.connect(self.checkboxReceivedAction)
        self.logUi.checkBoxSpent.stateChanged.connect(self.checkboxSpentAction)
        self.logUi.checkBoxShowCalc.stateChanged.connect(self.showCalcAction)
        self.table.doubleClicked.connect(self.tableDoubleClckedAction)
        self.logUi.checkBoxShowCash.stateChanged.connect(self.initCashPos)
        self.logUi.checkBoxShowPos.stateChanged.connect(self.initCashPos)


# *******************************CASH AND POS ACTIONS**************************************
    def initCashPos(self):
        secondDate = str(self.logUi.pushButtonSelectDate2.text())
        firstDate = str(self.logUi.pushButtonSelectDate1.text())
        if firstDate == 'Select Date':
            return
        if secondDate == 'Second Date (Optional)':
            self.dateOkClickedAction('first')
        else:
            self.dateOkClickedAction('second')
        self.showOnlyCashAction()
        self.showOnlyPosAction()
        self.setCalculationOnLabels()

    def showOnlyCashAction(self):
        toDelete=[]
        table = self.logUi.tableWidget
        rowCount = int(table.rowCount())

        if not self.logUi.checkBoxShowCash.isChecked():
            for i in xrange(rowCount):
                if str(table.item(i,5).text()).lower() == 'cash':
                    toDelete.append(i)
            while not toDelete == []:
                maxItem = max(toDelete)
                table.removeRow(maxItem)
                toDelete.remove(maxItem)


    def showOnlyPosAction(self):
        toDelete=[]
        table = self.logUi.tableWidget
        rowCount = int(table.rowCount())
        if not self.logUi.checkBoxShowPos.isChecked():
            for i in xrange(rowCount):
                if str(table.item(i,5).text()).lower() == 'pos':
                    toDelete.append(i)
            while not toDelete == []:
                maxItem = max(toDelete)
                table.removeRow(maxItem)
                toDelete.remove(maxItem)
# *******************************************************************************************

# *************************************** DATE CLICKED ACTIONS *****************************************************
    def firstDateButtonAction(self):
        self.logUi.checkBoxShowCash.setEnabled(True)
        self.logUi.checkBoxShowPos.setEnabled(True)
        self.checkCashPosCheckBoxes()
        self.logUi.pushButtonSelectDate2.setText('Second Date (Optional)')
        self.showDateDialog('first')


    def secondDateButtonAction(self):
        self.checkCashPosCheckBoxes()
        self.showDateDialog('second')
# ******************************************************************************************************************

# *****************************************CHECKBOX ACTIONS*********************************************************
# ******************SPENT****************
    def checkboxSpentAction(self):
        if self.logUi.checkBoxSpent.isChecked():
            self.table.showColumn(2)
        else:
            self.table.hideColumn(2)

# ****************RECEIVED**************
    def checkboxReceivedAction(self):
        if self.logUi.checkBoxReceived.isChecked():
            self.table.showColumn(1)
        else:
            self.table.hideColumn(1)

# ****************PURPOSE**************
    def checkboxPurposeAction(self):
        if self.logUi.checkBoxPurpose.isChecked():
            self.table.showColumn(3)
        else:
            self.table.hideColumn(3)
# ****************MEDIUM***************
    def checkboxMediumAction(self):
        if self.logUi.checkBoxMedium.isChecked():
            self.table.showColumn(5)
        else:
            self.table.hideColumn(5)

# ***************DATE******************
    def checkboxDateAction(self):
        if self.logUi.checkBoxDate.isChecked():
            self.table.showColumn(4)
        else:
            self.table.hideColumn(4)
#**************CALCULATION***********
    def showCalcAction(self):
        if self.logUi.checkBoxShowCalc.isChecked():
            self.viewBalanceLabels(True)
        else:
            self.viewBalanceLabels(False)

# *******************************************************************************************************************

# ********************************DATE DIALOG************
    def showDateDialog(self,btn):
        self.dateObj = DateSelectFunctions(self.logWindow)
        self.dateObj.dateUi.pushButtonOk.clicked.connect(lambda: self.dateOkClickedAction(btn))
        self.dateObj.dateUi.pushButtonCancel.clicked.connect(self.dateCancelClickedAction)

    def dateOkClickedAction(self,btn):
        data = []
        self.dateSelected = self.dateObj.dateUi.calendarWidget.selectedDate()
        self.dateObj.dateWindow.close()
        dateSelectedObj = self.convertDateToRequiredString(self.dateSelected)
        if btn == 'first':
            self.logUi.pushButtonSelectDate2.setEnabled(True)
            self.logUi.pushButtonSelectDate1.setText(str(self.convertDateToRequiredString(self.dateSelected)))
            data = self.getData(dateSelectedObj,None)
        elif btn=='second':
            firstDateSelected = str(self.logUi.pushButtonSelectDate1.text())
            self.logUi.pushButtonSelectDate2.setText(str(self.convertDateToRequiredString(self.dateSelected)))
            data = self.getData(firstDateSelected,dateSelectedObj)
        self.populateTable(data)


    def dateCancelClickedAction(self):
        self.dateObj.dateWindow.close()

    def convertDateToRequiredString(self,qdate):
        pydate = qdate.toPyDate()
        return pydate
# **********************************************************************************

# ***************FIRST DATE SELECTED ACTION**************************
    def getData(self,date1,date2):
        columnName = allstrings.date_added_column
        data = []
        if date2 == None:
            data = self.db.retrieveSearchedRecords(self.tableName,columnName,str(date1))
            data = functions.dbListTupleToListDict(data,self.tableName)
        else:
            data = self.db.retrieveSearchedRecordsBetweenDates(self.tableName, columnName,str(date1),str(date2))
            data = functions.dbListTupleToListDict(data,self.tableName)
        return data

    def populateTable(self,data):
        self.table.setRowCount(len(data))

        count = 0
        for i in data:
            itemid = QtGui.QTableWidgetItem()
            itemid.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            itemReceived = itemid.clone()
            itemSpent = itemid.clone()
            itemPurpose = itemid.clone()
            itemTime = itemid.clone()
            itemMedium = itemid.clone()

            self.table.setItem(count, 0, itemid)
            self.table.setItem(count, 1, itemReceived)
            self.table.setItem(count, 2, itemSpent)
            self.table.setItem(count, 3, itemPurpose)
            self.table.setItem(count, 4, itemTime)
            self.table.setItem(count, 5, itemMedium)

            itemid.setText(str(i[allstrings.allid_column]))
            if i[allstrings.money_transact_type_column] == 'Received':
                itemReceived.setText(str(i[allstrings.money_amount_column]))
                itemSpent.setText('')
            elif i[allstrings.money_transact_type_column] == 'Spent':
                itemReceived.setText('')
                itemSpent.setText(str(i[allstrings.money_amount_column]))
            itemPurpose.setText(str(i[allstrings.money_other_info_column]))
            itemTime.setText(str(i[allstrings.date_added_column]))
            itemMedium.setText(str(i[allstrings.money_medium_column]))
            count = count + 1
        self.setCalculationOnLabels()

# ******************************TABLE ACTIONS*****************
    def tableDoubleClckedAction(self):
        txt = str(self.table.item(self.table.currentRow(),3).text())
        self.detailsDialog = QtGui.QDialog(self.logWindow)
        self.detailsDialog.setModal(True)
        self.detailsDialog.setWindowTitle('Purpose Detail')
        self.label = QtGui.QLabel()
        self.label.setText(txt)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.detailsDialog.setLayout(self.vbox)
        self.detailsDialog.show()

# ************************************************************
# *****************************CALCULATE***********************************
# *************RECEIVED*************************
    def calculateReceived(self):
        table = self.logUi.tableWidget
        columnNumber = 1
        added = 0
        rows = table.rowCount()
        if rows == 0:
            return 0
        for i in xrange(rows):
            if not str(table.item(i,columnNumber).text()) == '':
                added = added + float(table.item(i,columnNumber).text())
        return added
# *************SPENT*******************
    def calculateSpent(self):
        table = self.logUi.tableWidget
        columnNumber = 2
        added = 0
        rows = table.rowCount()
        if rows == 0:
            return 0
        for i in xrange(rows):
            if not str(table.item(i,columnNumber).text()) == '':
                added = added + float(table.item(i,columnNumber).text())
        return added
# ************BALANCE***************
    def calculateBalance(self):
        balance = self.calculateSpent() -self.calculateReceived()
        return abs(float(balance))
#******************SET CALCULATION*******************************
    def setCalculationOnLabels(self):
        self.logUi.labelBalance.setStyleSheet('#labelBalance{color: rgb(0, 0, 0);}')
        r = "N{:,.2f}".format(self.calculateReceived())
        s = "N{:,.2f}".format(self.calculateSpent())
        b = "N{:,.2f}".format(self.calculateBalance())
        self.logUi.labelReceived.setText(r)
        self.logUi.labelSpent.setText(s)
        self.logUi.labelBalance.setText(b)

        if float(self.calculateSpent())> float(self.calculateReceived()):
            self.logUi.labelBalance.setStyleSheet('#labelBalance{color: rgb(255, 0, 0);}')
        else:
            self.logUi.labelBalance.setStyleSheet('#labelBalance{color: rgb(0, 0, 0);}')

# *********************************************************************************



#
# if __name__=='__main__':
#     import sys
#     from misc.dbfunctions import WebtyDb
#     app = QtGui.QApplication(sys.argv)
#     widget = QtGui.QMainWindow()
#     db2 = WebtyDb()
#     tlog = TransactionLog(widget, db2)
#     tlog.showWindow()
#     app.exec_()
