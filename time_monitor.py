from misc import allstrings,functions
from misc.dbfunctions import WebtyDb
import datetime,ntplib,time,os,sys
from PyQt4 import QtGui,QtCore


class TimeMonitor():

    def __init__(self):
        self.currentTime = ''
        self.allowedTimeBackdatedInSeconds = functions.calculateAllowedTimeInSeconds(numOfMins=20)
        self.allowedForwardTimeInSeconds = functions.calculateAllowedTimeInSeconds(numOfDays=10)
        self.db = WebtyDb()

    def setCurrentTime(self,currentTime):
        self.currentTime = currentTime

    def getCurrentTime(self):
        return self.currentTime

    def confirmTimeIntegrity(self):
        mainTime = self.getStoredTimeFromDb()

        internetTime = self.getCurrentTimeFromInternet()
        if internetTime or mainTime=='':
            mainTime = functions.convertTimeToDatetime(internetTime)
        systemTime = self.getCurrentTimeOfSystem()
        # timeDiff = max(systemTime,mainTime) - min(systemTime,mainTime)

        if mainTime>systemTime and (mainTime - systemTime).seconds > self.allowedTimeBackdatedInSeconds:
            return False
        elif systemTime>mainTime and (systemTime - mainTime).seconds > self.allowedForwardTimeInSeconds:
            return False
        else:
            mainTime = systemTime
            self.saveCurrentTimeToDb(mainTime)
            return True


    def getCurrentTimeOfSystem(self):
        d = datetime.datetime.now()
        return d

# ****************************** DATABASE ************************************

    def getDbPrefTableName(self):
        return allstrings.webtyprefsTableName

    def getAllPrefsData(self):
        d  = self.db.retrieveAllVals(self.getDbPrefTableName())
        return d

    def getStoredTimeFromDb(self):
        targetDict = {allstrings.webtyprefs_item_column:allstrings.webtyprefs_item_timestamp}
        e = self.db.retrieveRecord(self.getDbPrefTableName(),targetDict)
        e = functions.dbListTupleToListDict(e,self.getDbPrefTableName())
        if e == []:
            return ''
        e = e[0]
        e = e[allstrings.date_added_column]
        return e


    def saveCurrentTimeToDb(self,currentTime):
        found = False
        recordDict = {allstrings.webtyprefs_item_column:allstrings.webtyprefs_item_timestamp,
                      allstrings.date_added_column:currentTime}
        data = self.getAllPrefsData()
        data = functions.dbListTupleToListDict(data,self.getDbPrefTableName())
        for i in data:
            if allstrings.webtyprefs_item_timestamp in i.values():
                found = True
                dataId = i[allstrings.allid_column]
                self.db.updateRecord(self.getDbPrefTableName(),recordDict,dataId)
                break
        if found == False:
            self.db.insertNewRecord(self.getDbPrefTableName(),recordDict)
        return True


# **************************************************************************

#********************************** INTERNET *******************************
    def getCurrentTimeFromInternet(self):
        try:
            client = ntplib.NTPClient()
            response = client.request('pool.ntp.org')
            # response = time.strftime('%Y-%m-%d-%H:%M',time.localtime(response.tx_time))
            response = time.localtime(response.tx_time)
            return response
        except:
            return False
# **************************************************************************


if __name__ == '__main__':
    t = TimeMonitor()
    r = t.confirmTimeIntegrity()