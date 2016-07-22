import logging,allpaths
import logging.handlers


class LoggingWebty():


    def __init__(self,loggerName):
        allpaths.createFoldersIfNotExist()
        self.logger = logging.getLogger(loggerName)
        logging.basicConfig(format='%(asctime)s %(message)s',
                                 datefmt='%Y/%m/%d %H:%M:%S',level=logging.INFO)
        self.setUpLogHandlers()



    def setUpLogHandlers(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.infoFile = allpaths.getInfoLogFilePath()
        self.debugFile = allpaths.getDebugLogFilePath()
        self.warningFile = allpaths.getWarningLogFilePath()
        self.errorFile = allpaths.getErrorLogFilePath()

        self.handlerInfo = logging.handlers.TimedRotatingFileHandler(self.infoFile,when='D',interval=1,backupCount=5)
        self.handlerDebug = logging.handlers.TimedRotatingFileHandler(self.debugFile,when='D',interval=1,backupCount=5)
        self.handlerWarning = logging.handlers.TimedRotatingFileHandler(self.warningFile,when='D',interval=1,backupCount=5)
        self.handlerError = logging.handlers.TimedRotatingFileHandler(self.errorFile,when='D',interval=1,backupCount=5)

        self.handlerInfo.setFormatter(formatter)
        self.handlerDebug.setFormatter(formatter)
        self.handlerWarning.setFormatter(formatter)
        self.handlerError.setFormatter(formatter)

        self.handlerInfo.setLevel(logging.INFO)
        self.handlerDebug.setLevel(logging.DEBUG)
        self.handlerWarning.setLevel(logging.WARN)
        self.handlerError.setLevel(logging.ERROR)

        self.logger.addHandler(self.handlerInfo)
        self.logger.addHandler(self.handlerDebug)
        self.logger.addHandler(self.handlerWarning)
        self.logger.addHandler(self.handlerError)


    def info(self,msg):
        self.logger.info(msg)
    def debug(self,msg):
        self.logger.debug(msg)
    def warn(self,msg):
        self.logger.warn(msg)
    def error(self,msg,excinfo=False):
        self.logger.error(msg,exc_info=excinfo)
