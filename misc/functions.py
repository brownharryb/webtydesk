import allpaths, json, requests,datetime
import allstrings
from custom_exceptions import SiteUnavailableException
import time
from PyQt4 import QtGui

def getBrandList():
        li=[]
        with open(allpaths.ALL_BRANDS_FILENAME, 'r') as aFile:
            li = aFile.readlines()
        li = [x[:-1] for x in li]
        return li

def getModelList(brandName):
    brand_list = getBrandList()
    allModels=[]
    if not brandName in brand_list:
        return []
    allInfoFilePath = allpaths.getAllInfoJsonFileForBrand(brandName)
    with open(allInfoFilePath,'r') as infoFile:
        modelDict = json.loads(infoFile.read())
        allModels = modelDict.keys()
    return allModels

def getModelAndLinkDict(brandName):
    modelDict={}
    brand_list = getBrandList()
    if not brandName in brand_list:
        return {}
    allInfoFilePath = allpaths.getAllInfoJsonFileForBrand(brandName)
    with open(allInfoFilePath,'r') as infoFile:
        modelDict = json.loads(infoFile.read())
    return modelDict

def getImageExtension(imageUrlString):
    ext = imageUrlString[-4:]
    if ext=='.png':
        ext = '.jpg'
    return ext


def getSiteRequests(url):
    try:
        return requests.get(url)
    except:
        raise SiteUnavailableException('Website is not available or no internet for url: '+url)

def retrieveAndStoreImageFromNet(imageUrl, pathToStoreImage):
    from urllib import urlretrieve
    from custom_exceptions import SiteUnavailableException
    try:
        urlretrieve(imageUrl,pathToStoreImage)
    except:
        raise SiteUnavailableException('Unable to get image from url: '+imageUrl)

def isNumber(s):
    if 'e' in s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

def shortenString(s,number):
    """Shortens the string length to the specified number, then add a 3 dot ellipses"""

    if len(s)>number:
        return s[:number]+"..."
    return s
def getListValueOfDateTimeObject(dateTimeObj):
    """
    :param dateTimeObj: datetime.datetime
    :return: a list containing [year, month, day, hour, minute,second]
    """

    return [dateTimeObj.year, dateTimeObj.month, dateTimeObj.day, dateTimeObj.hour, dateTimeObj.minute, dateTimeObj.second]

def displayYesNoDialog(title,message):
    from PyQt4 import QtGui
    r = QtGui.QMessageBox.question(QtGui.QWidget(), title,
                                   message, QtGui.QMessageBox.Yes |
                                   QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    return r

def getDateValue(dateTimeObject):
    """Returns datetime as yyyy-mm-dd-hh-mm-ss"""

    return datetime.datetime.strftime(dateTimeObject,allstrings.dateTimeFormat)

def cleanCustomerName(custName):
    wantedChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890- '
    for i in custName:
        if not i in wantedChars:
            raise ValueError
    li = custName.strip().split()
    li2 = [x[0].upper()+x[1:] for x in li]
    custName = ' '.join(li2)
    return custName

def cleanStaffUsername(username):
    wantedChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in username:
        if not i in wantedChars:
            raise ValueError('Invalid input in username or password!')
    return str(username).lower()

def cleanStaffPassword(password):
    return cleanStaffUsername(password)

def hashPassword(password):
    import hashlib
    hashobj = hashlib.sha1(str(password).encode())
    return hashobj.hexdigest()


def cleanCustomerMobileNumber(custPhone):
    wantedChars = '0123456789-'
    for i in custPhone:
        if not i in wantedChars:
            raise ValueError
    r = long(custPhone) # this raises a valueerror if not valid
    return custPhone


def centerWindow(window):
    from PyQt4 import QtGui
    qr = window.frameGeometry().center()
    cp = QtGui.QDesktopWidget().availableGeometry().center()
    p = cp-qr
    window.move(p)

def filterListForCompleter(listVals, searchedText):
    return [x for x in listVals if str(searchedText).lower() in x.lower()]

def convertListOfTuplseToDict(listOfTuples):
    """
    :param listOfTuples: eg [(5, u'Bomadfdfdaf'), (6, u'Boma Brown'), (7, u'harry brown')]
    :return: {5:
    """
    pass


def getDateString(dateObj):
    dateStr = str(dateObj)
    newObj = dateStr[:dateStr.find('.')]
    return newObj

def getLockedTableItem(s):
    from PyQt4 import QtGui,QtCore
    d = QtGui.QTableWidgetItem(s)
    d.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
    return d

def getAllSearchedNamesNumbers(db, searchedText):
    if searchedText=='':
        return []
    returnList = db.retrieveSearchedRecords(allstrings.customersTableName,
                                            allstrings.customer_name_column,searchedText)
    if returnList == []:
        returnList = db.retrieveSearchedRecords(allstrings.customersTableName,
                                                allstrings.customer_phone_number_column,searchedText)
    if returnList==[]:
        returnList = db.retrieveSearchedRecords(allstrings.customersTableName,
                                                allstrings.customer_other_number_column,searchedText)
    return returnList

def checkTextInMessage(text):
    wantedChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-.,\'\r\n '
    t = 'ok'
    for i in text:
        if not str(i) in wantedChars:
            t = "The Letter \""+i+"\" in your message is not a valid letter, please remove and resend"
            break
    return t


def sendSms(sender,recipient,message):
    """
    OK=Successful
    2904=SMS Sending Failed
    2905=Invalid username/password combination
    2906=Credit exhausted
    2907=Gateway unavailable
    2908=Invalid schedule date format
    2909=Unable to schedule
    2910=Username is empty
    2911=Password is empty
    2912=Recipient is empty
    2913=Message is empty
    2914=Sender is empty
    2915=One or more required fields are empty
    """
    import requests, urllib
    sender = cleanMessage(sender)
    message = cleanMessage(message)
    url = 'http://www.nigerianbulksms.com/components/com_spc/smsapi.php?' \
          'username=bomsy&password=personal&sender='+sender+'&' \
          'recipient='+str(recipient)+'&message='+str(message)

    r = requests.get(url)
    return r.content
def cleanMessage(message):
    """
    http://www.w3schools.com/tags/ref_urlencode.asp
    for encoding
    """
    message = str(message).strip()
    message = message.replace('  ',' ')
    message = message.replace('\n',' ')
    message = message.replace('\r',' ')
    message = message.replace(' ','%20')
    return message




def dbListTupleToListDict(dbTupleList,tableName):

    returnList = []

    for eachTuple in dbTupleList:
        if tableName == allstrings.staffTableName:
            returnDict={}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.staff_name] = eachTuple[1]
            returnDict[allstrings.staff_username_column] = eachTuple[2]
            returnDict[allstrings.staff_password_column] = eachTuple[3]
            returnDict[allstrings.staff_designation_column] = eachTuple[4]
            returnDict[allstrings.staff_smscredit_column] = eachTuple[5]
            returnDict[allstrings.date_added_column] = eachTuple[6]
            returnList.append(returnDict)
        if tableName == allstrings.repairJobsTableName:
            returnDict = {}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.repair_job_item_name] = eachTuple[1]
            returnDict[allstrings.repair_job_customer_id] = eachTuple[2]
            returnDict[allstrings.repair_job_bill] = eachTuple[3]
            returnDict[allstrings.repair_job_other_info] = eachTuple[4]
            returnDict[allstrings.repair_job_bill_paid] = eachTuple[5]
            returnDict[allstrings.repair_job_status] = eachTuple[6]
            returnDict[allstrings.date_added_column] = eachTuple[7]
            returnDict[allstrings.repair_job_date_returned] = eachTuple[8]
            returnDict[allstrings.repair_job_imei_serial] = eachTuple[9]
            returnDict[allstrings.repair_job_knownfaults] = eachTuple[10]
            returnDict[allstrings.repair_job_customer_notified] = eachTuple[11]

            returnList.append(returnDict)
        if tableName == allstrings.customersTableName:
            returnDict = {}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.customer_name_column] = eachTuple[1]
            returnDict[allstrings.customer_phone_number_column] = eachTuple[2]
            returnDict[allstrings.customer_other_number_column] = eachTuple[3]
            returnDict[allstrings.date_added_column] = eachTuple[4]
            returnList.append(returnDict)
        if tableName == allstrings.sparePartsTableName:
            returnDict={}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.spareparts_name_column] = eachTuple[1]
            returnDict[allstrings.spare_quantity_column] = eachTuple[3]
            returnDict[allstrings.spareparts_price_column] = eachTuple[2]
            returnDict[allstrings.spare_vendor_column] = eachTuple[4]
            returnDict[allstrings.date_added_column] = eachTuple[5]
            returnList.append(returnDict)
        if tableName == allstrings.phonesTableName:
            pass
        if tableName == allstrings.smsAccTableName:
            returnDict = {}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.sms_username_column] = eachTuple[1]
            returnDict[allstrings.sms_password_column] = eachTuple[2]
            returnDict[allstrings.sms_balance_column] = eachTuple[3]
            returnDict[allstrings.sms_check_balance_column] = eachTuple[4]
            returnDict[allstrings.sms_active_column] = eachTuple[5]
            returnDict[allstrings.sms_sender_id] = eachTuple[6]
            returnDict[allstrings.sms_send_url_column] = eachTuple[7]
            returnDict[allstrings.date_added_column] = eachTuple[8]
            returnList.append(returnDict)
        if tableName == allstrings.moneyTableName:
            returnDict = {}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.money_amount_column] = eachTuple[1]
            returnDict[allstrings.money_transact_type_column] = eachTuple[2]
            returnDict[allstrings.money_repairjob_id_column] = eachTuple[3]
            returnDict[allstrings.money_other_info_column] = eachTuple[4]
            returnDict[allstrings.money_medium_column] = eachTuple[5]
            returnDict[allstrings.date_added_column] = eachTuple[6]
            returnList.append(returnDict)
        if tableName == allstrings.activityTableName:
            returnDict = {}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.activity_staff_column] = eachTuple[1]
            returnDict[allstrings.activity_info_column] = eachTuple[2]
            returnDict[allstrings.date_added_column] = eachTuple[3]
            returnList.append(returnDict)
        if tableName == allstrings.webtyprefsTableName:
            returnDict = {}
            returnDict[allstrings.allid_column] = eachTuple[0]
            returnDict[allstrings.webtyprefs_item_column] = eachTuple[1]
            returnDict[allstrings.webtyprefs_info_column] = eachTuple[2]
            returnDict[allstrings.date_added_column] = eachTuple[3]
            returnList.append(returnDict)
    return returnList


def encryptSmsPassword(passwordToDb):
    wantedChars = 'mnopqrs456tuvwxyzabcdefghijkl1237890'
    passwordToDb = str(passwordToDb).lower()
    l = []
    for i in passwordToDb:
        l.append(str(wantedChars.index(i)))
        l.append('$')

    returnVal= ''.join(l)
    return returnVal



def decryptSmsPassword(passwordFromDb):
    wantedChars = 'mnopqrs456tuvwxyzabcdefghijkl1237890'
    p = str(passwordFromDb).split('$')
    p = [wantedChars[int(x)] for x in p if not x=='']
    p = ''.join(p)
    return p

def getShortDate(dateObj):
    if dateObj:
        val = dateObj.strftime('%Y-%m-%d')
        return str(val)
    return ''

def calculateAllowedTimeInSeconds(**kwargs):
        secs = 0.0
        if kwargs.has_key('numOfDays'):
            numOfDays = kwargs['numOfDays']
            secs = secs + (numOfDays*86400.0)
        if kwargs.has_key('numOfHours'):
            numOfHours = kwargs['numOfHours']
            secs = secs + (numOfHours*3600)
        if kwargs.has_key('numOfMins'):
            numOfMins = kwargs['numOfMins']
            secs = secs + (numOfMins*60)
        if kwargs.has_key('numOfSecs'):
            numOfSecs = kwargs['numOfSecs']
            secs = secs + numOfSecs
        return secs

def convertTimeToDatetime(timestruct):
    dt = datetime.datetime.fromtimestamp(time.mktime(timestruct))
    return dt



def checkTime(func):
        def innerfunc(*args,**kwargs):
            try:
                from time_monitor import TimeMonitor
                timeMonitor = TimeMonitor()
                if timeMonitor.confirmTimeIntegrity():
                    func(*args,**kwargs)
                    return True
                else:
                    QtGui.QMessageBox.information(QtGui.QMessageBox(),'Time Check',
                        'Your System time doesn\'t seem to match mine!! Please correct it'
                        '\nIf this problem persists, connect to the internet then try again!!',
                        QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                    return False
            except:
                QtGui.QMessageBox.information(QtGui.QMessageBox(),'Database Check',
                                        'Please confirm Database is running!',
                                        QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
                return False

        return innerfunc