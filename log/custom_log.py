import os,datetime
from misc.dbfunctions import WebtyDb
from misc import allstrings,functions


class LogObj():

    def __init__(self):
        self.db = WebtyDb()
        self.tableName = allstrings.activityTableName
        self.setup()

    def setup(self):
        self.currentPath = os.path.dirname(__file__)
        self.today = datetime.datetime.now()

    def writeToLog(self,message,staffObjname = 'guest'):
        data = {}
        data[allstrings.date_added_column] = datetime.datetime.now()
        data[allstrings.activity_staff_column] = staffObjname
        data[allstrings.activity_info_column] = message
        self.db.insertNewRecord(self.tableName,data)

    def readFromLog(self,date):
        data = self.db.retrieveSearchedRecords(self.tableName,allstrings.date_added_column,date)
        data = functions.dbListTupleToListDict(data,self.tableName)
        for i in data:
            i[allstrings.date_added_column] = self.getDateString(i[allstrings.date_added_column])
        return data

    def getLogTimeString(self):
        todayString = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return todayString

    def getDateString(self,date):
        todayString = date.strftime('%Y-%m-%d %H:%M:%S')
        return todayString
