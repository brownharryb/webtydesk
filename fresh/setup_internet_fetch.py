
import time
from misc.dbfunctions import WebtyDb
from getalldatafromnet_first import DataFromNet
from storeofflinedata_second import OfflineData
from getallimagesfromnet_third import StoreImages
from PyQt4 import QtGui,QtCore
from log.logging_webty import LoggingWebty


class StartUp():


    def __init__(self):
        self.webtyLog = LoggingWebty(__name__)
        self.setupObj()
        self.labelToUpdate = ''


    def setupObj(self):
        self.fetchFromNet = DataFromNet()
        self.offlineData = OfflineData()
        self.storeImages = StoreImages()

    def setUpThread(self,labelToUpdate,mainFrontObj):
        self.threadToUse = FetchThread(first = self.fetchFromNet,second = self.offlineData,third = self.storeImages,fifth=self)
        self.mainFrontObj = mainFrontObj
        self.labelToUpdate = labelToUpdate



    def updateLabel(self,txt):
        self.labelToUpdate.setText(txt)


class FetchThread(QtCore.QThread):

    def __init__(self,**kwargs):
        QtCore.QThread.__init__(self)
        self.first = kwargs['first']
        self.second = kwargs['second']
        self.third = kwargs['third']
        self.startUpObj = kwargs['fifth']

    def run(self):
        try:
            self.first.process_html(self.startUpObj.labelToUpdate)
            self.second.storeAllData(self.startUpObj.labelToUpdate)
            self.third.processAllImages(self.startUpObj.labelToUpdate)
        except:
            self.startUpObj.labelToUpdate.setText('There might be a problem with your internet!!... exiting')
            time.sleep(2)
            self.startUpObj.mainFrontObj.stopUpdatingInternetData()


