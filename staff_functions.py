import datetime,time

from misc import functions,allstrings
from forms.login import Ui_dialogLogin
from PyQt4 import QtGui,QtCore

class StaffObject():

    def __init__(self,parent,db):
        self.db = db
        self.initialize()
        self.parent = parent


    def initialize(self):
        self.staffId = 0
        self.staffname = ''
        self.password = ''
        self.dateAdded = ''
        self.username = ''
        self.smscredits = 0
        self.designation = ''
        self.allStaffData =[]
        self.staffTable = allstrings.staffTableName

    def checkIfAdminExists(self):
        isPresent = False
        data = self.getAllStaffData()
        if not data==[]:
            for i in data:
                if str(i[allstrings.staff_designation_column])=='admin':
                    isPresent = True
        return isPresent

    def createAdminIfNotPresent(self):
        data={}
        if not self.checkIfAdminExists():
            data[allstrings.staff_name] = 'Admin'
            data[allstrings.staff_designation_column] = 'admin'
            data[allstrings.staff_password_column] = functions.hashPassword('admin')
            data[allstrings.staff_username_column] = 'admin'
            self.db.insertNewRecord(self.staffTable,data)




    def setAllData(self, data):
        data = functions.dbListTupleToListDict(data,allstrings.staffTableName)
        data = data[0]
        self.setStaffId(data[allstrings.allid_column])
        self.setStaffName(data[allstrings.staff_name])
        self.setUsername(data[allstrings.staff_username_column])
        self.setDesignation(data[allstrings.staff_designation_column])
        self.setSmsCredits(data[allstrings.staff_smscredit_column])
        self.setDateAdded(data[allstrings.date_added_column])

    def updateStaffDataToDb(self):
        recordDict = {}
        recordDict[allstrings.staff_name] = self.getStaffName()
        recordDict[allstrings.staff_designation_column] = self.getDesignation()
        recordDict[allstrings.staff_username_column] = self.getUsername()
        recordDict[allstrings.staff_smscredit_column] = self.getSmsCredits()
        self.db.updateRecord(self.staffTable, recordDict,self.getStaffId())


    def showLoginDialog(self):
        self.loginWindow = QtGui.QDialog(self.parent)
        self.loginDialogUi = Ui_dialogLogin()
        self.loginDialogUi.setupUi(self.loginWindow)
        self.loginDialogUi.labelInvalidLogin.setVisible(False)
        self.loginDialogUi.progressBarLogin.setVisible(False)
        self.loginWindow.show()
        self.loginDialogUi.pushButtonClear.clicked.connect(self.clearClickedAction)





    def validateLoginInputs(self,username,password):

        try:
            username = functions.cleanStaffUsername(username)
            password = functions.cleanStaffPassword(password)
            password=functions.hashPassword(password)
            data = self.db.retrieveRecord(allstrings.staffTableName,{allstrings.staff_username_column:username,
                                                              allstrings.staff_password_column:password})
            return data
        except ValueError as e:
            print e.message
            return []


    def clearClickedAction(self):
        self.loginDialogUi.lineEditLoginPassword.setText('')
        self.loginDialogUi.lineEditLoginUsername.setText('')
        self.loginDialogUi.labelInvalidLogin.setVisible(False)

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setSmsCredits(self, credit):
        if credit == '':
            credit = 0
        self.smscredits = float(credit)

    def getSmsCredits(self):
        return self.smscredits

    def setStaffName(self,staffname):
        self.staffname = staffname

    def getStaffName(self):
        return self.staffname

    def setDateAdded(self, dateObj):
        self.dateAdded = dateObj

    def getDateAdded(self):
        return self.dateAdded

    def setDesignation(self,designation):
        self.designation = designation

    def getDesignation(self):
        return self.designation

    def setStaffId(self,id):
        self.staffId = id

    def getStaffId(self):
        return self.staffId

    def getAllStaffData(self):
        data = self.db.retrieveAllVals(self.staffTable)
        data = functions.dbListTupleToListDict(data,self.staffTable)
        return data

    def getAllUsernameList(self):
        data = []
        d = self.getAllStaffData()

        for i in d:
            data.append(i[allstrings.staff_username_column])
        return data






    def saveStaffToDb(self,regUi,regWindow):
        try:
            dictRecord = {}

            dictRecord[allstrings.staff_name] = functions.cleanCustomerName(str(regUi.lineEditName.text()))
            dictRecord[allstrings.staff_designation_column] = functions.cleanCustomerName(str(regUi.lineEditDesignation.text()))
            dictRecord[allstrings.staff_username_column] = functions.cleanStaffUsername(str(regUi.lineEditUsername.text()))
            staffPassword1 = functions.cleanStaffPassword(str(regUi.lineEditPassword1.text()))
            staffPassword2= functions.cleanStaffPassword(str(regUi.lineEditPassword2.text()))

            if any(['' in dictRecord.values(),staffPassword1=='',staffPassword2=='']):
                regUi.labelError.setText('Some Inputs are empty!!')
                regUi.labelError.setVisible(True)
                return
            if not staffPassword1 == staffPassword2:
                regUi.labelError.setText('Passwords don\'t match!')
                regUi.labelError.setVisible(True)
                return
            dictRecord[allstrings.staff_password_column] = functions.hashPassword(staffPassword1)
            dictRecord[allstrings.staff_smscredit_column] = '0'
            dictRecord[allstrings.date_added_column] = datetime.datetime.now()

            if self.db.duplicateIsAvailable(allstrings.staffTableName,
                                            {allstrings.staff_username_column:dictRecord[allstrings.staff_username_column]}):
                regUi.labelError.setText('Username already exists!')
                regUi.labelError.setVisible(True)
                return

            confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'New Staff','Add New Staff?',
                                                    QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if confirm == QtGui.QMessageBox.Yes:
                id = self.db.insertNewRecord(allstrings.staffTableName,dictRecord)
                okd = QtGui.QMessageBox.information(QtGui.QMessageBox(),'New Staff','Staff Added.',
                                                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                regWindow.close()

        except ValueError as e:
            regUi.labelError.setText('Some Inputs are invalid')
            regUi.labelError.setVisible(True)

    def clearClickedRegAction(self, regUi):
        regUi.labelError.setVisible(False)
        regUi.lineEditName.setText('')
        regUi.lineEditDesignation.setText('')
        regUi.lineEditUsername.setText('')
        regUi.lineEditPassword1.setText('')
        regUi.lineEditPassword2.setText('')

# ***************************************STAFF MODIFY SECTION***************************************

    def staffModifyComboChange(self, modifyUi):
        modifyUi.lineEditName.setText('')
        modifyUi.lineEditDesignation.setText('')
        modifyUi.lineEditUsername.setText('')
        modifyUi.lineEditSmsCredits.setText('')
        modifyUi.labelDbId.setText('')
        modifyUi.labelError.setVisible(False)

        if modifyUi.comboBoxAllStaffUsername.currentIndex()==0:
            return

        username = str(modifyUi.comboBoxAllStaffUsername.currentText()).lower()
        data = self.db.retrieveRecord(self.staffTable,{allstrings.staff_username_column:username})
        data = functions.dbListTupleToListDict(data,self.staffTable)[0]
        modifyUi.lineEditName.setText(data[allstrings.staff_name])
        modifyUi.lineEditDesignation.setText(data[allstrings.staff_designation_column])
        modifyUi.lineEditUsername.setText(data[allstrings.staff_username_column])
        modifyUi.lineEditSmsCredits.setText(data[allstrings.staff_smscredit_column])
        modifyUi.labelDbId.setText(str(data[allstrings.allid_column]))

    def staffModifyUpdate(self,modifyUi,modifyWindow):
        if modifyUi.comboBoxAllStaffUsername.currentIndex() == 0:
            modifyUi.labelError.setText('Select a username!!')
            modifyUi.labelError.setVisible(True)
            return
        data = {}
        idToUpdate = str(modifyUi.labelDbId.text())
        data[allstrings.staff_name] = str(modifyUi.lineEditName.text())
        data[allstrings.staff_designation_column] = str(modifyUi.lineEditDesignation.text())
        data[allstrings.staff_username_column] = str(modifyUi.lineEditUsername.text())
        data[allstrings.staff_smscredit_column] = str(modifyUi.lineEditSmsCredits.text())
        passwd1 = str(modifyUi.lineEditPassword1.text())
        passwd2 = str(modifyUi.lineEditPassword2.text())

        if '' in data.values():
            modifyUi.labelError.setText('Some Inputs are empty!!')
            modifyUi.labelError.setVisible(True)
            return

        if not passwd1==passwd2:
            modifyUi.labelError.setText('Passwords don\'t match!!')
            modifyUi.labelError.setVisible(True)
            return

        if not functions.isNumber(data[allstrings.staff_smscredit_column]):
            modifyUi.labelError.setText('Numbers only for sms credit!!')
            modifyUi.labelError.setVisible(True)
            return

        if not passwd1 == '':
            data[allstrings.staff_password_column] = functions.hashPassword(passwd1)

        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Update Staff','Update Staff?',
                                                    QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if confirm==QtGui.QMessageBox.No:
            return
        if not self.db.updateRecord(self.staffTable, data,idToUpdate):
            modifyUi.labelError.setText('Something went wrong, pls check database!!')
            modifyUi.labelError.setVisible(True)
            return
        QtGui.QMessageBox.information(QtGui.QMessageBox(),'Update Staff','Staff Updated.',
                                                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        modifyWindow.close()

    def initializeModifyDialog(self,modifyUi):
        modifyUi.comboBoxAllStaffUsername.setCurrentIndex(0)
        modifyUi.lineEditName.setText('')
        modifyUi.lineEditDesignation.setText('')
        modifyUi.lineEditUsername.setText('')
        modifyUi.lineEditSmsCredits.setText('')
        modifyUi.labelDbId.setText('')
        modifyUi.labelError.setVisible(False)

# *************************************************************************************************

#**********************************************STAFF MODIFY DELETE SECTION******************

    def staffModifyDelete(self,modifyUi,modifyDialog):
        deleteId = modifyUi.labelDbId.text()
        if deleteId=='':
            modifyUi.labelError.setText('Select Username to delete!!')
            modifyUi.labelError.setVisible(True)
            return

        confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Delete Staff','Delete Staff?',
                                                    QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if confirm==QtGui.QMessageBox.Yes:
            self.db.deleteRecord(self.staffTable,deleteId)
            self.initializeModifyDialog(modifyUi)
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Delete Staff','Staff Deleted!.',
                                                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

            modifyDialog.close()


# ********************************************************************************************


    def showProgress(func):
        def innerfunc(self,*args,**kwargs):
            self.confirmThread = ConfirmTime()
            self.confirmThread.start()
            keepChecking = True
            i = 0
            self.loginDialogUi.progressBarLogin.setValue(0)
            self.loginDialogUi.progressBarLogin.setVisible(True)
            while i<100:
                i = i + 0.00001
                if keepChecking == True:
                    self.loginDialogUi.progressBarLogin.setValue(i)
                if self.confirmThread.isFinished():
                    self.loginDialogUi.progressBarLogin.setVisible(False)
                    break
            if self.confirmThread.returnVal == True:
                return func(self)
            elif self.confirmThread.returnVal == 'timing':
                QtGui.QMessageBox.information(QtGui.QMessageBox(),'Time Check',
                    'Your System time doesn\'t seem to match mine!! Please correct it'
                    '\nIf this problem persists, connect to the internet then try again!!',
                    QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                return False
            elif self.confirmThread.returnVal == 'database':
                QtGui.QMessageBox.information(QtGui.QMessageBox(),'Database Check',
                                    'Please confirm Database is running!',
                                    QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                return False
        return innerfunc




    @showProgress
    def loginClickedAction(self):
        loginUsername = str(self.loginDialogUi.lineEditLoginUsername.text())
        loginPassword = str(self.loginDialogUi.lineEditLoginPassword.text())

        allData = self.validateLoginInputs(loginUsername,loginPassword)

        if allData == []:
            self.loginDialogUi.labelInvalidLogin.setVisible(True)
            return False
        self.setAllData(allData)
        return True


class ConfirmTime(QtCore.QThread):

    def __init__(self):
        self.returnVal = False
        QtCore.QThread.__init__(self)


    def run(self):
        self.returnVal = self.doOp()

    def doOp(self):
        try:
            from time_monitor import TimeMonitor
            timeMonitor = TimeMonitor()
            if timeMonitor.confirmTimeIntegrity():
                return True
            else:
                return 'timing'
        except:
            return 'database'