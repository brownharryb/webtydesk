import os,csv
from misc import functions,allstrings
from PyQt4 import QtGui, QtCore
from forms.group_send_message import Ui_dialodGroupSmsAdd

class GroupSms():

    def __init__(self,parent,db):
        self.db = db
        self.parent = parent
        self.setUp()

    def setUp(self):
        self.groupSmsUi = Ui_dialodGroupSmsAdd()
        self.groupSmsDialog = QtGui.QDialog(self.parent)
        self.groupSmsUi.setupUi(self.groupSmsDialog)

    def showForm(self):
        self.groupSmsDialog.show()
        self.groupSmsUi.tableWidgetNumbers.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.groupSmsUi.pushButtonAddCustomers.clicked.connect(self.addGroupAllCustomers)
        self.groupSmsUi.pushButtonAddCsv.clicked.connect(self.addCsv)
        self.groupSmsUi.pushButtonDelete.clicked.connect(self.deleteSelectedNumbers)


    def addCsv(self):
        table = self.groupSmsUi.tableWidgetNumbers
        csvList = []
        csvDictKeys = {}
        csvFile = QtGui.QFileDialog.getOpenFileName(self.groupSmsDialog,'Select CSV file','',('*.csv'))
        nameNumberList = self.getNameNumberListOfCsvFile(csvFile)
        self.populateTable(nameNumberList)

    def addGroupAllCustomers(self):
        cDict = {}
        countStep = 0
        allCust = self.db.retrieveAllVals(allstrings.customersTableName)
        allCust = functions.dbListTupleToListDict(allCust,allstrings.customersTableName)
        for i in allCust:
            custName = i[allstrings.customer_name_column]
            custPhone1 = i[allstrings.customer_phone_number_column]
            custPhone2 = i[allstrings.customer_other_number_column]
            cDict.update({countStep:[custName,[custPhone1,custPhone2]]})
            countStep = countStep + 1
        self.populateTable(cDict)


    def updateToMain(self):
        pass

    def deleteSelectedNumbers(self):
        table = self.groupSmsUi.tableWidgetNumbers
        itemsSelected = table.selectedIndexes()
        rowsSelected = [x.row() for x in itemsSelected]
        rowsSelected = list(set(rowsSelected))
        iterateCount = len(rowsSelected)
        for i in xrange(iterateCount):
            rowToDelete = max(rowsSelected)
            table.removeRow(rowToDelete)
            rowsSelected.remove(rowToDelete)
        self.groupSmsUi.labelNumberOfPeople.setText(str(table.rowCount()))

    def populateTable(self,contactDict):
        table = self.groupSmsUi.tableWidgetNumbers
        countStep = table.rowCount()
        rowCount = len(contactDict.keys())
        table.setRowCount(countStep + rowCount)

        for i in contactDict.keys():
            numList = contactDict[i][1]
            nameItem = QtGui.QTableWidgetItem(str(contactDict[i][0]))
            phoneNumberItem1 = QtGui.QTableWidgetItem(str(numList[0]))
            table.setItem(countStep,0,nameItem)
            table.setItem(countStep,1,phoneNumberItem1)
            try:
                phoneNumberItem2 = QtGui.QTableWidgetItem(str(numList[1]))
                table.setItem(countStep,2,phoneNumberItem2)
            except IndexError as e:
                pass
            finally:
                countStep = countStep + 1

        labelCount = int(self.groupSmsUi.labelNumberOfPeople.text())
        self.groupSmsUi.labelNumberOfPeople.setText(str(labelCount+int(table.rowCount())))



    def getNameNumberListOfCsvFile(self,csvFile):
        returnVal = {}
        countStep = 0
        if os.path.exists(csvFile):
            with open(csvFile, 'r') as aFile:
                csvObj = csv.DictReader(aFile)
                for i in csvObj:
                    numList = []
                    tempNumList = []
                    firstName = i['First Name']
                    midName = i['Middle Name']
                    lastName = i['Last Name']
                    primaryPhone = i['Primary Phone']
                    homePhone = i['Home Phone']
                    homePhone2 = i['Home Phone 2']
                    mobilePhone = i['Mobile Phone']
                    companyMainPhone = i['Company Main Phone']
                    businessPhone = i['Business Phone']
                    businessPhone2 = i['Business Phone 2']
                    otherPhone = i['Other Phone']

                    allNumbers = [primaryPhone,homePhone,homePhone2,mobilePhone,companyMainPhone,
                                  businessPhone,businessPhone2,otherPhone]

                    fullname = ' '.join([firstName,midName,lastName])
                    fullname = fullname.strip()
                    fullname = fullname.replace('  ',' ')

                    for j in allNumbers:
                        j = str(j).strip()
                        if '-' in j:
                            j = str(j).replace('-','')
                        if ' ' in j:
                            j = str(j).replace(' ','')
                        if not j == '' and functions.isNumber(j):
                            tempNumList.append(j)
                    if not len(tempNumList) < 1:
                        numList.append(tempNumList[0])
                    if len(tempNumList)>1:
                        numList.append(tempNumList[1])
                    if not numList == []:
                        returnVal.update({countStep:[fullname,numList]})
                        countStep = countStep + 1
        return returnVal
