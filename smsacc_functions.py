
from misc import allstrings,functions
import datetime, requests

class SmsAccount():


    def __init__(self, db):
        self.db = db
        self.tableName = allstrings.smsAccTableName
        self.allAccounts = self.getAllAccounts()
        self.activeAccount = self.getActiveAccount()
        self.senderId = 'WEBTY.S'

    def getAllAccounts(self):
        d = self.db.retrieveAllVals(self.tableName)
        d = functions.dbListTupleToListDict(d,self.tableName)
        return d

    def getSenderId(self):
        return self.senderId


    def getActiveAccount(self):
        activeAcc = {}
        if self.allAccounts == []:
            return {}
        for i in self.allAccounts:
            if str(i[allstrings.sms_active_column]).lower() == 'active':
                activeAcc.update(i)
                break
        return activeAcc

    def getActiveValue(self,flag):

        if self.activeAccount == {} or flag=='':
            return ''
        if flag == '_id':
            return self.activeAccount[allstrings.allid_column]
        if flag=='username':
            return self.activeAccount[allstrings.sms_username_column]
        elif flag=='password':
            return functions.decryptSmsPassword(self.activeAccount[allstrings.sms_password_column])
        elif flag=='balance':
            return self.activeAccount[allstrings.sms_balance_column]
        elif flag=='check_balance':
            return self.activeAccount[allstrings.sms_check_balance_column]
        elif flag=='send_url':
            return self.activeAccount[allstrings.sms_send_url_column]
        elif flag=='sender_id':
            return self.activeAccount[allstrings.sms_sender_id]
        else:return ''

    def sendSms(self,senderId,number,message):
        senderId = functions.cleanMessage(senderId)
        message = functions.cleanMessage(message)

        url = self.getActiveSendUrl()
        newUrl = url.replace('@@sender@@',senderId)
        newUrl = newUrl.replace('@@recipient@@',number)
        newUrl = newUrl.replace('@@message@@',message)
        r = requests.get(newUrl)
        return r.content


    def getActiveSendUrl(self):
        url = self.getActiveValue('send_url')
        strToReplace = '@@password@@'
        password = self.getActiveValue('password')
        newUrl = url.replace(strToReplace,password)
        return newUrl

    def getActiveCheckBalanceUrl(self):
        url = self.getActiveValue('check_balance')
        strToReplace = '@@password@@'
        password = self.getActiveValue('password')
        newUrl = url.replace(strToReplace,password)
        return newUrl



    def saveData(self,username,password):
        data = {}
        data[allstrings.sms_username_column] = str(username)
        data[allstrings.sms_password_column] = functions.encryptSmsPassword(str(password))
        data[allstrings.sms_check_balance_column] = \
            'http://www.nigerianbulksms.com/components/com_spc/smsapi.php?username='+\
              str(username)+'&password=@@password@@&balance=true&'
        data[allstrings.sms_send_url_column] = 'http://www.nigerianbulksms.com/components/com_spc/smsapi.php?' \
                                               'username='+str(username)\
                                               +'&password=@@password@@&sender=@@sender@@&recipient=@@recipient@@&message=@@message@@&'
        data[allstrings.sms_sender_id] = self.senderId
        data[allstrings.date_added_column] = datetime.datetime.now()


        if self.db.duplicateIsAvailable(self.tableName,
                                        {allstrings.sms_username_column:data[allstrings.sms_username_column]}):
            pass
        else:
            self.db.insertNewRecord(self.tableName, data)
        return True

    def activateAcc(self,username,senderId):
        allAccounts = self.getAllAccounts()
        if allAccounts == []:
            return
        for i in allAccounts:
            if i[allstrings.sms_username_column]==str(username):
                i[allstrings.sms_active_column] = 'active'
                i[allstrings.sms_sender_id] = senderId.upper()
            else:
                i[allstrings.sms_active_column] = ''
            self.db.updateRecord(self.tableName, i,i[allstrings.allid_column])
        return True

#
# if __name__=='__main__':
#     from misc.dbfunctions import WebtyDb
#     db = WebtyDb()
#     smsObj = SmsAccount(db)



