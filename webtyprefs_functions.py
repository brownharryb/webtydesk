from misc import allstrings,functions
import datetime

class WebtyPrefs():

    def __init__(self,db):
        self.db = db
        self.tableName = allstrings.webtyprefsTableName
        self.setUpObj()


    def setUpObj(self):
        self.data = self.db.retrieveAllVals(self.tableName)
        self.data = functions.dbListTupleToListDict(self.data,self.tableName)

    def getDictForPrefs(self,item):
        d = {}
        if not self.data==[]:
            for i in self.data:
                if i[allstrings.webtyprefs_item_column] == item:
                    d.update(i)
                    break
        return d

    def getFixedItemsSms(self,nameOfCust,itemName):

        dataToAdd = self.getDictForPrefs(allstrings.webtyprefs_item_fixed_sms)
        self.fixedItemsSms = "Dear {{name}},\nYour item '{{item}}' has been fixed. " \
                                 "\nPlease come for collection. " \
                                 "\nRegards. " \
                                 "\nWebty Solutions."



        if dataToAdd=={}:
            dataToAdd[allstrings.webtyprefs_item_column] = allstrings.webtyprefs_item_fixed_sms
            dataToAdd[allstrings.webtyprefs_info_column] = self.fixedItemsSms
            dataToAdd[allstrings.date_added_column] = datetime.datetime.now()
            self.db.insertNewRecord(self.tableName, dataToAdd)
        msg = str(dataToAdd[allstrings.webtyprefs_info_column])
        if '{{name}}' in msg:
            msg = msg.replace('{{name}}',nameOfCust)
        if '{{item}}' in msg:
            msg = msg.replace('{{item}}',itemName)
        return msg


    def getPrefsTimeStamp(self):
        pass
