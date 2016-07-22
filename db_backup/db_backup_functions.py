import os,datetime
from misc import allstrings
from subprocess import call
from forms.backup_db import Ui_dialogBackupDb
from forms.db_login import Ui_dialogDbLogin
from staff_functions import StaffObject
from log.custom_log import LogObj
from PyQt4 import QtGui,QtCore


class DbBackup():


    def __init__(self,parent,db):
        self.db = db
        self.parent = parent
        self.folderPath = ''
        self.logObj = LogObj()

    def showForm(self):
        self.backupUi = Ui_dialogBackupDb()
        self.backupDialog = QtGui.QDialog(self.parent)
        self.backupUi.setupUi(self.backupDialog)
        self.initializeFm()
        self.backupUi.comboBoxChooseFunction.currentIndexChanged.connect(self.comboChangedAction)
        self.backupUi.pushButtonOk.setText('BACK UP')
        self.backupUi.tableWidgetAllFiles.setEnabled(False)
        self.backupUi.pushButtonSelectFolder.clicked.connect(self.selectFolderAction)
        self.backupUi.pushButtonOk.clicked.connect(self.okButtonAction)
        self.backupUi.pushButtonCancel.clicked.connect(self.cancelButtonAction)
        self.backupUi.tableWidgetAllFiles.clicked.connect(self.tableClickedAction)
        self.backupDialog.show()

    def initializeFm(self):
        self.backupUi.tableWidgetAllFiles.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.backupUi.tableWidgetAllFiles.setRowCount(0)
        self.backupUi.pushButtonOk.setEnabled(False)
        self.backupUi.labelFolderlPath.setVisible(False)
        self.backupUi.progressBarUpdate.setVisible(False)
        self.backupUi.progressBarUpdate.setValue(0)

    def comboChangedAction(self):
        self.initializeFm()
        if self.backupUi.comboBoxChooseFunction.currentIndex() == 0:
            self.backupUi.pushButtonOk.setText('BACK UP')
            self.backupUi.tableWidgetAllFiles.setEnabled(False)
        elif self.backupUi.comboBoxChooseFunction.currentIndex() == 1:
            self.backupUi.pushButtonOk.setText('RESTORE')
            self.backupUi.tableWidgetAllFiles.setEnabled(True)

    def selectFolderAction(self):
        self.initializeFm()
        folderPath = self.getFolderPathSelected()
        self.folderPath = str(folderPath)
        self.backupUi.labelFolderlPath.setText(self.folderPath)
        self.backupUi.labelFolderlPath.setVisible(True)
        self.backupUi.pushButtonOk.setEnabled(True)
        self.populateTable(self.folderPath)


    def tableClickedAction(self):
        self.backupUi.pushButtonOk.setEnabled(True)


    def okButtonAction(self):

        if self.backupUi.comboBoxChooseFunction.currentIndex() == 1: #restore
            if self.backupUi.tableWidgetAllFiles.currentRow() == -1:
                 QtGui.QMessageBox.information(QtGui.QMessageBox(),'Error','Please Select file to restore!',
                                    QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                 return False
            self.showStaffLogin(self.folderPath,flag='restore')

        elif self.backupUi.comboBoxChooseFunction.currentIndex() == 0: #backup
            if self.folderPath == '':
                QtGui.QMessageBox.information(QtGui.QMessageBox(),'Select Folder','Select a folder first!',
                                        QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                return False
            confirm = QtGui.QMessageBox.question(QtGui.QMessageBox(),'Backup Database','Do you want to back up the database?',
                                        QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
            if confirm == QtGui.QMessageBox.No:
                return False
            self.showStaffLogin(self.folderPath)



    def cancelButtonAction(self):
        self.backupDialog.close()


#********************************************MISC*******************************

    def getFolderPathSelected(self):
        folder = QtGui.QFileDialog.getExistingDirectory(self.backupDialog,'Choose Folder','')
        return folder

    def getAllSqlFiles(self,folderPath):
        allsqlfiles = []
        try:
            for i in os.listdir(folderPath):
                if str(i).endswith('.sql'):
                    allsqlfiles.append(str(i))
            return allsqlfiles
        except:
            pass

    def populateTable(self,folderPath):
        table = self.backupUi.tableWidgetAllFiles
        table.clearContents()
        table.setRowCount(0)
        allFiles = self.getAllSqlFiles(folderPath)
        if allFiles == None or len(allFiles) == 0:
            return False
        table.setRowCount(len(allFiles))
        count = 0
        for i in allFiles:
            li = self.splitSqlString(str(i))

            itemName = QtGui.QTableWidgetItem()
            itemName.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            itemDate = itemName.clone()
            itemTime = itemName.clone()

            itemName.setText(str(i))
            itemDate.setText(li[0])
            itemTime.setText(li[1])

            table.setItem(count, 0,itemName)
            table.setItem(count, 1,itemDate)
            table.setItem(count, 2,itemTime)

            count = count + 1
        return True

    def splitSqlString(self,sqlString):
        li = str(sqlString).split('_')
        li2 = [str(li[0]+'-'+li[1]+'-'+li[2]),str(li[3]+':'+li[4]+':'+li[5][:-4])]
        return li2



    def backupToFolder(self,username,password,folderPath):
        today = datetime.datetime.now()
        backupFilename = today.strftime('%Y_%m_%d_%H_%M_%S')+'.sql'
        filePath = os.path.join(folderPath,backupFilename)
        pathForDump = allstrings.wamp_mysql_path_dir+'\\mysqldump'


        dumpCommand = pathForDump+' -u'+username+' -p'+password+' '+allstrings.databaseName+' > '+filePath
        self.commThread = DbComm(dumpCommand)
        self.commThread.start()
        count = 0
        speed = 0.0001

        self.backupUi.progressBarUpdate.setVisible(True)
        while count < 100:
            count = count +speed
            self.backupUi.progressBarUpdate.setValue(count)
            if self.commThread.isFinished():
                if self.commThread.success:
                    speed = 0.001
        self.backupUi.progressBarUpdate.setVisible(False)
        if self.confirmBackUp(filePath):
            r = self.showConfirmSave()
            if r == 0:
                self.populateTable(self.folderPath)
                self.openFileInExplorer(self.folderPath,filePath)
            elif r == 1:
                print 'rejected'
            self.logObj.writeToLog('\nDatabase was successfully Backed up to \n'+str(filePath),self.staffObj.getStaffName())
        else:
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Error','Something went wrong, \nDatabse was not backed up!',
                                    QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)

    def confirmBackUp(self,fileName):
        allOk = False
        if os.path.exists(fileName):
            if os.stat(fileName).st_size > 0:
                allOk = True
        return allOk

    def showConfirmSave(self):
        msgbox = QtGui.QMessageBox()
        msgbox.setWindowTitle('Success')
        msgbox.setText('Database was successfully backed up! \nYou can move the file to another computer incase of a breakdown!!')
        msgbox.addButton(QtGui.QPushButton('View File'), QtGui.QMessageBox.YesRole)
        msgbox.addButton(QtGui.QPushButton('Close'), QtGui.QMessageBox.NoRole)
        return msgbox.exec_()

    def openFileInExplorer(self,folderPath,filename):
        if os.path.exists(filename):
            call("explorer /select,%s" %filename, shell=True)




# ******************************STAFF LOGIN ***********************
    def showStaffLogin(self,folderPath,flag='backup'):
        self.staffObj = StaffObject(self.backupDialog,self.db)
        self.staffObj.showLoginDialog()
        self.staffObj.loginDialogUi.pushButtonLogin.clicked.connect(lambda: self.loginAction(folderPath,flag))

    def loginAction(self,folderPath,flag):
        if self.staffObj.loginClickedAction():
            if flag == 'backup':
                self.staffObj.loginWindow.close()
                self.backupToFolder(allstrings.databaseUserName,allstrings.databasePassword,folderPath)
            elif flag == 'restore':
                if not self.staffObj.getDesignation().lower() == 'admin':
                    self.staffObj.loginDialogUi.labelInvalidLogin.setVisible(True)
                    self.staffObj.loginDialogUi.labelInvalidLogin.setText('Only the admin is allowed to restore the database!')
                    return False
                self.staffObj.loginWindow.close()
                self.restoreDb(folderPath)



# ********************************************************************
# ****************************** RESTORE ******************************
    def restoreDb(self,folderPath):
        table = self.backupUi.tableWidgetAllFiles
        row = table.currentRow()
        filename = table.item(row,0).text()
        filepath = os.path.join(folderPath,str(filename))

        pathForRestore = allstrings.wamp_mysql_path_dir+'\\mysql'
        username = allstrings.databaseUserName
        password = allstrings.databasePassword
        restoreCommand = pathForRestore+' -u'+username+' -p'+password+' '+allstrings.databaseName+' < '+filepath

        self.retoreThread = DbComm(restoreCommand,flag='restore')
        self.retoreThread.start()
        self.backupUi.progressBarUpdate.setVisible(True)
        count = 0
        speed = 0.000001
        while count<100:
            count = count + speed
            self.backupUi.progressBarUpdate.setValue(count)
            if self.retoreThread.isFinished():
                speed = 0.001
        if self.retoreThread.success:
            self.backupUi.progressBarUpdate.setVisible(False)
            self.logObj.writeToLog('\nDatabase was successfully Restored from \n'+str(filename),self.staffObj.getStaffName())
            QtGui.QMessageBox.information(QtGui.QMessageBox(),'Success','Database Successfully Restored!!',
                                        QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
# *********************************************************************

#***************************** DATABASE LOGIN**********************

    # def showDbLogin(self,folderPath):
    #     self.loginDbUi = Ui_dialogDbLogin()
    #     self.loginDbDialog = QtGui.QDialog(self.backupDialog)
    #     self.loginDbUi.setupUi(self.loginDbDialog)
    #     self.loginDbUi.labelError.setVisible(False)
    #     self.loginDbUi.pushButtonLogin.clicked.connect(lambda: self.dbLoginAction(folderPath))
    #     self.loginDbUi.pushButtonCancel.clicked.connect(self.dbLoginCancelAction)
    #     self.loginDbDialog.show()
    #
    #
    # def dbLoginAction(self,folderPath):
    #     username = str(self.loginDbUi.lineEditUsername.text())
    #     password = str(self.loginDbUi.lineEditPassword.text())
    #     pathForDump = allstrings.wamp_mysql_path_dir+'\\mysql'
    #     if username =='' or password == '':
    #         return False
    #     try:
    #         cmd = pathForDump+' -u'+username+' -p'+password
    #     except Exception as e:
    #         print e.message
    #
    #     # self.backupToFolder(username,password,folderPath)
    #
    # def dbLoginCancelAction(self):
    #     pass

# *****************************************************************


class DbComm(QtCore.QThread):

    def __init__(self,cmd,flag='backup'):
        QtCore.QThread.__init__(self)
        self.flag = flag
        self.cmd = cmd
        self.success = False

    def run(self):
        if self.flag == 'backup':
            call(self.cmd,shell=True)
            self.success = True
        elif self.flag == 'restore':
            call(self.cmd,shell=True)
            self.success = True










