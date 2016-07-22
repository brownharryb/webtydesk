from PyQt4 import QtGui,QtCore
from forms.additem import Ui_MainWindow
from misc import functions,allstrings
from custom_widgets.all_widgets import MyImageLabel
from log.logging_webty import LoggingWebty
import allpaths, datetime





class AddItemFunctions():

    def __init__(self,parent,db):
        self.webtyLog = LoggingWebty(__name__)
        self.db = db
        self.parent = parent
        self.setUpAllObj()


    def setUpAllObj(self):
        self.addItemUi = Ui_MainWindow()
        self.addItemWindow = QtGui.QMainWindow(self.parent)
        self.addItemUi.setupUi(self.addItemWindow)
        self.setUpModel()
        self.setUpCompleter()
        self.currentBrand = ''
        self.currentModel = ''
        self.picLocation = ''

    def setPicAndUrlOnLabel(self,picPath,url):
        try:
            self.picLabel.clear()
        except:
            self.picLabel = MyImageLabel()
            self.picLabel.setParent(self.addItemUi.framePic)
            self.picLabel.setMaximumSize(self.addItemUi.framePic.size())
        self.pixmap = QtGui.QPixmap(picPath)
        scaledPic = self.pixmap.scaled(self.picLabel.size(), QtCore.Qt.KeepAspectRatio)
        self.picLabel.setPixmap(scaledPic)
        self.picLabel.setUrl(url)
        self.picLabel.show()

    def setUpModel(self):
        # for brand
        self.brandCompleterModel = QtGui.QStringListModel()
        self.brandList = functions.getBrandList()
        self.brandCompleterModel.setStringList(self.brandList)

        # for model
        self.modelCompleterModel = QtGui.QStringListModel()

        self.completerModel = QtGui.QStringListModel()
        self.allColumnVals = self.db.retrieveAllColumnsVals(allstrings.phonesTableName, [allstrings.phone_name_column,
                                                                                   allstrings.phone_pic_location_column,
                                                                                   allstrings.phone_page_link_column])
        self.allPhoneNames = [x[0] for x in self.allColumnVals]
        self.completerModel.setStringList(self.allPhoneNames)



    def setUpCompleter(self):
        # for brand
        self.brandCompleter = QtGui.QCompleter()
        self.brandCompleter.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.brandCompleter.setModel(self.brandCompleterModel)
        self.addItemUi.lineEditPhoneBrand.setCompleter(self.brandCompleter)

        # for model
        self.modelCompleter = QtGui.QCompleter()
        self.modelCompleter.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.modelCompleter.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        self.modelCompleter.setModel(self.modelCompleterModel)
        self.addItemUi.lineEditPhoneModel.setCompleter(self.modelCompleter)



        self.nameCompleter = QtGui.QCompleter()
        self.nameCompleter.setModel(self.completerModel)
        self.nameCompleter.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        self.addItemUi.lineEditItemName.setCompleter(self.nameCompleter)


    def showAddItemForm(self,customerName=''):
        if not customerName=='':
            self.addItemWindow.setWindowTitle('ADD ITEM FOR REPAIRS ['+functions.shortenString(customerName, 25).upper()+']')
        self.addItemWindow.show()
        self.addAllActionsEvents()

    def addAllActionsEvents(self):
        self.addItemUi.lineEditItemName.textChanged.connect(self.nameTextChangedAction)
        self.addItemUi.checkBoxPendBill.stateChanged.connect(self.pendBillStateChangedAction)
        # self.addItemUi.pushButtonOk.clicked.connect(self.pushButtonOkAction)
        self.addItemUi.pushButtonCancel.clicked.connect(self.pushButtonCancelAction)
        self.addItemUi.lineEditPhoneBrand.textChanged.connect(self.brandTextChangedAction)
        self.addItemUi.lineEditPhoneModel.textChanged.connect(self.modelTextChangedAction)

    def brandTextChangedAction(self):
        self.clearLabelPic()
        self.addItemUi.lineEditItemName.setEnabled(True)

        self.currentBrand = ''
        self.addItemUi.lineEditPhoneModel.setText('')
        self.addItemUi.lineEditPhoneModel.setEnabled(False)
        searchedBrand = self.addItemUi.lineEditPhoneBrand.text()
        if self.addItemUi.lineEditPhoneBrand.text() == '':
            return
        if searchedBrand in self.brandList:
            self.currentBrand = str(searchedBrand)
            self.addItemUi.lineEditPhoneModel.setEnabled(True)
            self.modelList = functions.getModelList(self.currentBrand)
            self.modelCompleterModel.setStringList(self.modelList)





    def modelTextChangedAction(self):
        self.clearLabelPic()
        self.addItemUi.lineEditItemName.setEnabled(True)
        searchedModel = str(self.addItemUi.lineEditPhoneModel.text())
        self.modelList2 = [x for x in self.modelList if searchedModel.lower() in x.lower()]
        self.modelCompleterModel.setStringList(self.modelList2)
        if searchedModel in self.modelList:
            self.currentModel = searchedModel
            self.displayPicAndSetUrl(self.currentBrand, self.currentModel)
            self.itemName = self.currentBrand+" "+self.currentModel
            self.addItemUi.lineEditItemName.setText(self.itemName)
            self.addItemUi.lineEditItemName.setEnabled(False)




    def nameTextChangedAction(self):
        searchedText = str(self.addItemUi.lineEditItemName.text())
        if searchedText=='':
            return
        self.searchedPhoneNames = [x for x in self.allPhoneNames if searchedText in x]
        self.completerModel.setStringList(self.searchedPhoneNames)

        if searchedText in self.searchedPhoneNames:
            self.displayPicAndSetUrl(self.currentBrand, self.currentModel)



    def pendBillStateChangedAction(self):
        if self.addItemUi.checkBoxPendBill.isChecked():
            self.addItemUi.lineEditBill.setText('0')
            self.addItemUi.lineEditPaid.setText('0')
            self.addItemUi.lineEditBill.setEnabled(False)
        else:
            self.addItemUi.lineEditBill.setText('')
            self.addItemUi.lineEditPaid.setText('')
            self.addItemUi.lineEditBill.setEnabled(True)


    def pushButtonOkAction(self):
        if self.cleanAllData():
            return self.getAllDataAsDict()
        return {}

    def pushButtonCancelAction(self):
        self.addItemWindow.close()

    # def getListOfSearchedItem(self,searchedText):
    #     return ['asudhi','dahfbi','uyagysb']

    def displayPicAndSetUrl(self, brandName, modelName):
        l = functions.getModelAndLinkDict(brandName)[modelName]
        imgExt = functions.getImageExtension(l[2])
        self.setPicAndUrlOnLabel(allpaths.get_model_image_pathname(brandName,modelName,imgExt),l[1])

    def clearLabelPic(self):
        try:
            self.picLabel.clear()
        except:
            pass

    def getAllDataAsDict(self):
        itemName = str(self.addItemUi.lineEditItemName.text())
        knownFaults = str(self.addItemUi.lineEditKnownFaults.text()).lower()
        additionalInfo = str(self.addItemUi.textEditAdditionalDetails.toPlainText()).lower()
        pendBill = self.addItemUi.checkBoxPendBill.checkState()
        bill = self.addItemUi.lineEditBill.text()
        paid = self.addItemUi.lineEditPaid.text()
        imei = str(self.addItemUi.lineEditImeiNumber.text())
        status = str(self.addItemUi.comboBoxStatus.currentText()).lower()
        todayDate = functions.getDateString(datetime.datetime.now())

        bill = int(bill)
        paid = int(paid)

        return {'name':itemName,'additionalInfo':additionalInfo, 'pendBill':pendBill,
                'bill':bill, 'paid':paid, 'today':todayDate,
                'status':status,'knownFaults':knownFaults,'imei_serial':imei}

    def cleanAllData(self):
        alphabets = 'abcdefghijklmnopqrstuvwxyz1234567890,._ '
        statusBar = self.addItemUi.statusbar
        itemName = str(self.addItemUi.lineEditItemName.text())
        imei = str(self.addItemUi.lineEditImeiNumber.text())
        knownFaults = str(self.addItemUi.lineEditKnownFaults.text())
        additionalDetails = str(self.addItemUi.textEditAdditionalDetails.toPlainText())
        status = str(self.addItemUi.comboBoxStatus.currentText())
        pendBill = self.addItemUi.checkBoxPendBill.checkState()
        bill = self.addItemUi.lineEditBill.text()
        paid = self.addItemUi.lineEditPaid.text()

        allAlphaVals = [knownFaults,additionalDetails]
        allInputs = [itemName,imei,knownFaults,additionalDetails,status,pendBill,bill,paid]
        for k in allInputs:
            if k == '':
                statusBar.showMessage('Some Inputs are empty!')
                return False

        for i in allAlphaVals:
            for j in i:
                if not j in alphabets:
                    statusBar.showMessage('You have an invalid letter \'%s\' in one of your inputs' %j)
                    return False
        if not functions.isNumber(imei):
            statusBar.showMessage('Please make sure your imei or serial number is a number!!')
            return False
        if not functions.isNumber(bill):
            statusBar.showMessage('Please make sure bill entered is a number!!')
            return False
        if not functions.isNumber(paid):
            statusBar.showMessage('Please make sure your amount paid entered is a number!!')
            return False
        return True

    def getAllStatusAsDict(self):
        l = {}
        for i in xrange(self.addItemUi.comboBoxStatus.count()):
            l[i] = str(self.addItemUi.comboBoxStatus.itemText(i))
        return l

