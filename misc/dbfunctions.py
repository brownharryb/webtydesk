import mysql.connector
from log.logging_webty import LoggingWebty
from misc import allstrings, functions
from PyQt4 import QtGui


class WebtyDb():

    def __init__(self):
        self.webtyLog = LoggingWebty(__name__)
        self.createDatabase()
        self.createAllTables()


    def createDatabase(self):
        self.conn = mysql.connector.connect(host=allstrings.databaseHostName,
                                            user=allstrings.databaseUserName,
                                            password=allstrings.databasePassword)
        self.firstCursor = self.conn.cursor()
        self.firstCursor.execute(allstrings.createDatabase)
        self.conn.commit()
        self.closeConnection()

    def createAllTables(self):
        # Create all tables if not existing
        self.createConnectionAndCursor()
        self.firstCursor.execute(allstrings.createStaffTable)
        self.firstCursor.execute(allstrings.createCustomerTable)
        self.firstCursor.execute(allstrings.createPhonesTable)
        self.firstCursor.execute(allstrings.createRepairJobsTable)
        self.firstCursor.execute(allstrings.createSparePartsTable)
        self.firstCursor.execute(allstrings.createSmsTable)
        self.firstCursor.execute(allstrings.createTransactionTable)
        self.firstCursor.execute(allstrings.createLogTable)
        self.firstCursor.execute(allstrings.createPrefsTable)
        self.conn.commit()
        self.closeConnection()


    def createConnectionAndCursor(self):
        self.conn = mysql.connector.connect(host=allstrings.databaseHostName,
                                            database=allstrings.databaseName,
                                            user=allstrings.databaseUserName,
                                            password=allstrings.databasePassword)
        self.firstCursor = self.conn.cursor()

    def closeConnection(self):
        if self.conn.is_connected():
            self.webtyLog.info('Closing db connection')
            self.firstCursor.close()
            self.conn.close()


    def insertNewRecord(self, tableName, recordDict):
        if self.duplicateIsAvailable(tableName,recordDict):
            self.webtyLog.info('Inserting record into '+tableName)
            self.webtyLog.warn("Duplicate found.. for inserting"+str(recordDict)+'into'+str(tableName))
            return False
        try:
            self.createConnectionAndCursor()
            allColumns = recordDict.keys()
            allColumnsAsString = ','.join(allColumns)
            allValues = [x for x in recordDict.values()]
            placeHolderValues = ','.join(['%s' for _ in xrange(len(recordDict))])
            q = "INSERT INTO "+tableName+" ("+allColumnsAsString+") VALUES ("+placeHolderValues+");"
            self.firstCursor.execute(q,tuple(allValues))
            self.conn.commit()
            idReturned = self.retrieveRecord(tableName,recordDict,flag='id')
            self.webtyLog.info('id returned for inserting data = '+str(idReturned))
            return idReturned
        except Exception as e:
            self.webtyLog.error("Exception for Adding record "+str(recordDict)+" to "+tableName,excinfo=True)
            return 0
        finally:
            self.closeConnection()


    def updateRecord(self, tableName, recordDict,id):
        self.webtyLog.info('Updating record in '+tableName)
        try:
            self.createConnectionAndCursor()
            placeHolderValues = [x+"=%s"for x in recordDict.keys()]
            placeHolderValues = ','.join(placeHolderValues)
            allValues = tuple([x for x in recordDict.values()])


            q = "UPDATE "+tableName+" SET "+placeHolderValues+" WHERE _id="+str(id)+";"
            self.firstCursor.execute(q,allValues)
            self.conn.commit()
            return True
        except Exception as e:
            self.webtyLog.error('Exception for Updating record in '+tableName,excinfo=True)
            return False
        finally:
            self.closeConnection()


    def deleteRecord(self, tableName, id):
        self.webtyLog.info('Deleting record with id: '+str(id)+' from '+tableName)
        try:
            self.createConnectionAndCursor()
            q = "DELETE FROM "+tableName+" WHERE _id=%s;" %id
            self.firstCursor.execute(q)
            self.conn.commit()
            return True
        except Exception as e:
            self.webtyLog.error('Exception for Deleting record with id: '+str(id)+' in '+tableName,
                                excinfo=True)
            return False
        finally:
            self.closeConnection()


    def deleteRecordUsingValue(self, tableName, column, value):
        self.webtyLog.info('Deleting record with value: '+str(value)+' in column: '+str(column)+' from '+tableName)
        try:
            self.createConnectionAndCursor()
            q = "DELETE FROM "+tableName+" WHERE "+column+" = %s;" %value
            self.firstCursor.execute(q)
            self.conn.commit()
            return True
        except Exception as e:
            self.webtyLog.error('Exception for Deleting record in '+tableName,excinfo=True)
            return False
        finally:
            self.closeConnection()


    def retrieveRecordUsingId(self, tableName,id=0):
        self.webtyLog.info('Retrieving record using id: '+str(id)+' from '+tableName)
        try:
            self.createConnectionAndCursor()
            if id>0:
                q = "SELECT * FROM "+tableName+" WHERE _id=%s;" %id
                self.firstCursor.execute(q)
                return self.firstCursor.fetchall()
        except Exception as e:
            self.webtyLog.error("Exception for Fetching record using id: "+str(id)+" in "+tableName,
                                excinfo=True)
            return []
        finally:
            self.closeConnection()


    def retrieveRecord(self,tableName,targetDict, flag='all'):
        self.webtyLog.info('Retrieving record: '+str(targetDict)+' from '+tableName)
        allValues = tuple(targetDict.values())
        placeHolderValues = str(targetDict.keys()[0])+"=%s"
        if len(targetDict)>1:
            for i in xrange(len(targetDict)-1):
                placeHolderValues = placeHolderValues+" AND "+str(targetDict.keys()[i+1])+" =%s"
        try:
            self.createConnectionAndCursor()
            q= "SELECT * FROM "+tableName+" WHERE "+placeHolderValues+";"
            self.firstCursor.execute(q,allValues)
            returnVal = self.firstCursor.fetchall()
            if flag=='id':
                returnVal = returnVal[0][0]
            return returnVal
        except Exception as e:
            self.webtyLog.error("Exception for Fetching record"+str(targetDict)+" in "+tableName,
                                excinfo=True)
            if flag=='id':
                return 0
            return []
        finally:
            self.closeConnection()


    def retrieveAllColumnsVals(self, tableName, columnsAsList):
        self.webtyLog.info('Retrieving records from columns: '+str(columnsAsList)+' from '+tableName)
        if len(columnsAsList)>1:
            q = "SELECT "+','.join(columnsAsList)+" FROM "+tableName+";"
        else:
            q = "SELECT "+columnsAsList[0]+" FROM "+tableName+";"

        try:
            self.createConnectionAndCursor()
            self.firstCursor.execute(q)
            returnVal = self.firstCursor.fetchall()
            return returnVal
        except Exception as e:
            self.webtyLog.error("Exception for Retrieving records in "+tableName,excinfo=True)
            return []
        finally:
            self.closeConnection()


    def retrieveAllVals(self,tableName):
        self.webtyLog.info('Retrieving all records from '+tableName)
        try:
            self.createConnectionAndCursor()
            q = "SELECT  * FROM "+tableName+";"
            self.firstCursor.execute(q)
            returnVal = self.firstCursor.fetchall()
            return returnVal
        except Exception as e:
            self.webtyLog.error("Exception for Retrieving records in "+tableName,excinfo=True)
            return []
        finally:
            self.closeConnection()


    def specialRetrieveCustomerVals(self):
        self.webtyLog.info('Retrieving special vals from customer table')
        d = {}
        li = self.retrieveAllColumnsVals(allstrings.customersTableName,
                                         ['_id',allstrings.customer_name_column,
                                          allstrings.customer_phone_number_column])
        for i in li:
            d[i[0]] = i[1]+" | "+i[2]

        return d


    def duplicateIsAvailable(self, tableName, targetDict):
        try:
            self.createConnectionAndCursor()
            row = self.retrieveRecord(tableName,targetDict)
            if row == []:
                return False
            self.webtyLog.warn("Duplicate found for "+str(targetDict)+" in "+tableName+" skipping record..")
            return True
        except Exception as e:
            pass
        finally:
            self.closeConnection()



    def retrieveSearchedRecords(self,tableName,columnName, text):
        self.webtyLog.info('Retrieving searched record using text: '+str(text)+' from '+str(tableName))
        try:
            self.createConnectionAndCursor()
            q = "SELECT * FROM "+tableName+" WHERE "+columnName+" LIKE '%"+str(text).lower()+"%';"
            self.firstCursor.execute(q)
            returnVal = self.firstCursor.fetchall()
            return returnVal
        except:
            self.webtyLog.error('Exception retrieving serached record: text:'+str(text)+' from '+str(tableName),
                                excinfo=True)
            return []
        finally:
            self.closeConnection()


    def retrieveSearchedRecordsBetweenDates(self,tableName, columnName,firstDate,secondDate):
        self.webtyLog.info('Retrieving searched record between dates: '+str(firstDate)+' and '+str(secondDate)+' from '+
                           str(tableName))
        try:
            self.createConnectionAndCursor()
            q = "SELECT * FROM "+tableName+" WHERE "+columnName+" >= CAST(%s AS DATE) AND "+\
                columnName+" <= CAST( %s AS DATE);"
            self.firstCursor.execute(q,(firstDate,secondDate))
            returnVal = self.firstCursor.fetchall()
            return returnVal
        except Exception as e:
            self.webtyLog.error("Exception getting dates between "+str(firstDate)+" and "+str(secondDate), excinfo=True)
            return []
        finally:
                self.closeConnection()


    def modifyPhones(self, phoneRecordDict, status='update',id=0):
        tableName = allstrings.phonesTableName
        if status=='add':
            return self.insertNewRecord(tableName,phoneRecordDict)
        elif status=='update' and not id==0:
            return self.updateRecord(tableName,phoneRecordDict,id)
        elif status=='delete' and not id==0:
            return self.deleteRecord(tableName,id)
        else:
            return False

    def modifyStaffs(self, staffRecordDict, status='update',id=0):
        tableName = allstrings.staffTableName
        if status=='add':
            return self.insertNewRecord(tableName,staffRecordDict)
        elif status=='update' and not id==0:
            return self.updateRecord(tableName,staffRecordDict,id)
        elif status=='delete' and not id==0:
            return self.deleteRecord(tableName,id)
        else:
            return False

    def modifyRepairJobs(self, jobsRecordDict, status='update',id=0):
        tableName = allstrings.repairJobsTableName
        if status=='add':
            return self.insertNewRecord(tableName, jobsRecordDict)
        elif status=='update' and not id==0:
            return self.updateRecord(tableName,jobsRecordDict,id)
        elif status=='delete' and not id==0:
            return self.deleteRecord(tableName,id)
        else:
            return False


    def modifyCustomers(self, customerRecordDict, status='update',id=0):
        tableName = allstrings.customersTableName
        if status=='add':
            return self.insertNewRecord(tableName,customerRecordDict)
        elif status=='update' and not id==0:
            return self.updateRecord(tableName,customerRecordDict,id)
        elif status=='delete' and not id==0:
            return self.deleteRecord(tableName,id)
        else:
            return False

    def modifySpareParts(self, sparepartsRecordDict, status='update',id=0):
        tableName = allstrings.sparePartsTableName
        if status=='add':
            return self.insertNewRecord(tableName, sparepartsRecordDict)
        elif status=='update' and not id==0:
            return self.updateRecord(tableName,sparepartsRecordDict,id)
        elif status=='delete' and not id==0:
            return self.deleteRecord(tableName,id)
        else:
            return False

