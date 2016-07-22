from PyQt4 import QtGui
from forms.select_date import Ui_formDateWidget


class DateSelectFunctions():


    def __init__(self,parent):
        self.parent = parent
        self.setUpObj()



    def setUpObj(self):
        self.dateWindow = QtGui.QDialog(self.parent)
        self.dateUi = Ui_formDateWidget()
        self.dateUi.setupUi(self.dateWindow)
        self.dateWindow.show()
