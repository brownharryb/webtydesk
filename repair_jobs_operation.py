import allpaths,datetime

from PyQt4 import QtGui, QtCore
from misc import functions, allstrings
from forms.itemreg import Ui_mainWindow
from custom_widgets.all_widgets import MyImageLabel



class RepairJobFunctions():
    old_brand_name = ''
    new_brand_name = ''
    searched_model_list = []
    temp_empty_model_list = []
    cached_model_list=[]
    model_qmodel = QtGui.QStringListModel()

    def __init__(self):
        self.setupAllObj()

    def setupAllObj(self):
        self.mainWindow = QtGui.QMainWindow()
        self.itemregui = Ui_mainWindow()
        self.itemregui.setupUi(self.mainWindow)
        self.brandList = functions.getBrandList()



    def showRepairJobForm(self):
        pass


    def showAddNewForm(self,customerName='', requiredDict={}):
        self.itemregui.labelItemInfo.setText("Repair Job for "+customerName+".")
        self.completer = QtGui.QCompleter(self.brandList)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.itemregui.lineEditBrandSearch.setCompleter(self.completer)
        self.itemregui.lineEditBrandSearch.textChanged.connect(self.getModelList)
        self.itemregui.lineEditModelSearch.textChanged.connect(self.updateModelList)
        self.itemregui.listViewModelSearch.itemClicked.connect(self.displaymodelinfo)
        self.itemregui.pushButtonSave.clicked.connect(self.addButtonOnItemRegAction)
        self.itemregui.pushButtonReset.clicked.connect(self.resetButtonOnItemRegAction)
        self.itemregui.checkBoxPendBill.stateChanged.connect(self.checkButtonsTickedAction)

        if not requiredDict=={}:

            self.positionOfItemToUpdate = requiredDict['position']
            self.itemregui.labelItemInfo.setText("Repair Job for "+requiredDict['customer_name']+".")
            self.itemregui.lineEditUnavailableType.setText(requiredDict['job_item'])
            self.itemregui.textEditProblemDescription.setText(requiredDict['problem'])
            if requiredDict['bill_charged']=='0':
                self.itemregui.checkBoxPendBill.setChecked(True)
            else:
                self.itemregui.lineEditCurrentBill.setText(requiredDict['bill_charged'])
                self.itemregui.lineEditBalanceBill.setText(requiredDict['paid'])
        self.mainWindow.show()

    def getModelList(self):
        # clear model text
        self.itemregui.lineEditModelSearch.setText('')
        self.itemregui.lineEditUnavailableType.setText('')
        self.new_brand_name = str(self.itemregui.lineEditBrandSearch.text())


        if not self.new_brand_name in self.brandList:
            self.searched_model_list = []
            return

        if not self.new_brand_name == self.old_brand_name or self.cached_model_list == []:
            self.old_brand_name = self.new_brand_name
            self.searched_model_list = functions.getModelList(self.new_brand_name)
            self.cached_model_list = self.searched_model_list
        else:
            self.searched_model_list = self.cached_model_list


    def updateModelList(self):
        self.itemregui.listViewModelSearch.clear()
        modeltxt = str(self.itemregui.lineEditModelSearch.text()).lower()
        if not modeltxt=='':
            updated_model_list = [x for x in self.searched_model_list if modeltxt in x.lower()]
            self.model_qmodel.setStringList(updated_model_list)
            self.itemregui.listViewModelSearch.addItems(updated_model_list)

    def displaymodelinfo(self,item):
        try:
            self.label.clear()
            self.label.setUrl('')
        except:
            self.label = MyImageLabel()


        modelName = str(item.text())
        modelsAndLinksDict = functions.getModelAndLinkDict(self.new_brand_name)
        modelLink = modelsAndLinksDict[modelName][1]
        imageExtension = functions.getImageExtension(modelsAndLinksDict[modelName][2])

        selectedPhone = self.new_brand_name+"  "+modelName
        self.itemregui.lineEditUnavailableType.setText(selectedPhone)

        try:
            self.current_model_image_path = allpaths.get_model_image_pathname(self.new_brand_name,modelName,imageExtension)
            self.label.setParent( self.itemregui.widgetPic)
            self.pixmap = QtGui.QPixmap(self.current_model_image_path)
            self.label.setMaximumSize(self.itemregui.widgetPic.size())
            scaledPic = self.pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(scaledPic)
            self.label.setUrl(modelLink)
            self.label.setStatusTip('Get More Information (Visit Website)')
            self.label.show()
            #TODO png image file not displaying eg Iconia Tab 10 A3-A30 under acer
        except Exception as e:
            pass

    def checkButtonsTickedAction(self):
        pendBillState = self.itemregui.checkBoxPendBill.checkState()

        if pendBillState:
            self.itemregui.lineEditCurrentBill.setText('0')
            self.itemregui.lineEditCurrentBill.setDisabled(True)
            self.itemregui.lineEditBalanceBill.setText('0')
            self.itemregui.lineEditBalanceBill.setDisabled(True)
        else:
            self.itemregui.lineEditCurrentBill.setText('')
            self.itemregui.lineEditCurrentBill.setDisabled(False)
            self.itemregui.lineEditBalanceBill.setText('')
            self.itemregui.lineEditBalanceBill.setDisabled(False)

    def allInputsOk(self):
        allgood = True
        self.unavailableType = self.itemregui.lineEditUnavailableType.text()
        self.problemDescription = self.itemregui.textEditProblemDescription.toPlainText()
        self.amountCharged = self.itemregui.lineEditCurrentBill.text()
        self.balanceAmountToBePaid = self.itemregui.lineEditBalanceBill.text()
        self.pendBillCheckBox = self.itemregui.checkBoxPendBill.checkState()

        if self.unavailableType == '':
            self.mainWindow.statusBar().showMessage("No phone selected!!")
            allgood = False
        if self.problemDescription == '':
            self.mainWindow.statusBar().showMessage("What is the problem of the item?")
            allgood = False
        if all([self.amountCharged=='', self.pendBillCheckBox==0]):
            self.mainWindow.statusBar().showMessage("Specify amount charged or pend the bill")
            allgood = False
        if self.balanceAmountToBePaid=='':
            self.mainWindow.statusBar().showMessage("Has the money been paid?")
            allgood = False
        if not functions.isNumber(self.amountCharged)or not functions.isNumber(self.balanceAmountToBePaid):
            self.mainWindow.statusBar().showMessage("Please enter a valid amount of money")
            allgood = False

        return allgood

    def updateButtonOnRepairAction(self):
        todayDate = functions.getDateValue(datetime.datetime.now())
        if self.allInputsOk():
            stringDisplayOnListWidget = self.unavailableType+" | "+\
                                        self.problemDescription+\
                                        " | BILL:"+self.amountCharged+" | PAID:"+self.balanceAmountToBePaid+\
                                        " | STATUS:UNFIXED | DATE:"+todayDate
            self.mainWindow.close()
            return stringDisplayOnListWidget


    def addButtonOnItemRegAction(self):
        if all([ not self.itemregui.groupBoxAllItems.isChecked(),self.itemregui.pushButtonSave.text()=='Add']):
            self.mainWindow.close()
            return ''

        try:
            todayDate = functions.getDateValue(datetime.datetime.now())
            if self.allInputsOk():
                stringDisplayOnListWidget = self.unavailableType+" | "+\
                                            self.problemDescription+\
                                            " | BILL:"+self.amountCharged+" | PAID:"+self.balanceAmountToBePaid+\
                                            " | STATUS:UNFIXED | DATE:"+todayDate
                self.mainWindow.close()
                return stringDisplayOnListWidget

        except Exception as e:
            print "Exception at adding item to customer = "+e.message

    def resetButtonOnItemRegAction(self):
        self.itemregui.lineEditBrandSearch.setText('')
        self.itemregui.textEditProblemDescription.setText('')
        self.itemregui.lineEditBalanceBill.setText('')
        self.itemregui.lineEditCurrentBill.setText('')
        self.itemregui.checkBoxPendBill.setChecked(False)
        self.itemregui.lineEditUnavailableType.setText('')
        try:
            self.label.clear()
            self.label.setUrl('')
        except Exception as e:
            print "Attribute error from reset button = "+e.message
            pass

