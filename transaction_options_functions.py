from misc import allstrings
from fixeditems_functions import FixedItem
from forms.transact_options import Ui_dialogTransaction
from money_functions import MoneyObj
from PyQt4 import QtGui


class TrasanctionObj():


    def __init__(self,parent,db):
        self.db = db
        self.parent = parent
        self.setUpObjs()



    def setUpObjs(self):
        self.transactionUi = Ui_dialogTransaction()
        self.transactionDialog = QtGui.QDialog(self.parent)
        self.transactionUi.setupUi(self.transactionDialog)

    def showDialog(self):
        self.transactionUi.pushButtonSpend.clicked.connect(self.spendButtonClickedAction)
        self.transactionUi.pushButtonReceive.clicked.connect(self.receivedButtonClickedAction)
        self.transactionUi.pushButtonFixed.clicked.connect(self.fixedButtonClickedAction)
        self.transactionDialog.show()


    def spendButtonClickedAction(self):
        self.spendMoneyObj = MoneyObj(self.transactionDialog,self.db)
        self.spendMoneyObj.moneyDialog.setWindowTitle('Purchase')
        self.spendMoneyObj.moneyUi.radioButtonPos.setVisible(False)
        self.spendMoneyObj.moneyUi.radioButtonCash.setVisible(False)
        self.spendMoneyObj.moneyUi.pushButtonSave.clicked.connect(self.spendMoneyObj.saveButtonDialogAction)
        self.spendMoneyObj.dataDict[allstrings.money_transact_type_column]= 'Spent'
        self.spendMoneyObj.showDialog()

    def receivedButtonClickedAction(self):
        self.receiveMoneyObj = MoneyObj(self.transactionDialog,self.db)
        self.receiveMoneyObj.moneyDialog.setWindowTitle('Payment Received')
        self.receiveMoneyObj.moneyUi.pushButtonSave.clicked.connect(self.receiveMoneyObj.saveButtonDialogAction)
        self.receiveMoneyObj.dataDict[allstrings.money_transact_type_column]= 'Received'
        self.receiveMoneyObj.showDialog()

    def fixedButtonClickedAction(self):
        self.fixedItemObj = FixedItem(self.transactionDialog,self.db)
        self.fixedItemObj.showFixedDialog()




