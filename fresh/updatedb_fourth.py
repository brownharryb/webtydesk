from misc.dbfunctions import WebtyDb
from misc import allstrings,functions
import allpaths

class DbHandler():


    def __init__(self):
        self.db = WebtyDb()


    def updatePhones(self):
        self.phoneBrandList = functions.getBrandList()
        for i in self.phoneBrandList:
            modelAndLinkDict = functions.getModelAndLinkDict(i)

            for eachModel in modelAndLinkDict.keys():
                imageExtension = functions.getImageExtension(modelAndLinkDict[eachModel][2])
                self.db.modifyPhones({allstrings.phone_name_column:str(i)+" | "+eachModel,
                                      allstrings.phone_extra_info_column:' ',
                                      allstrings.phone_page_link_column:modelAndLinkDict[eachModel][1],
                                      allstrings.phone_pic_location_column:allpaths.getRelativeImagePath(i,eachModel,
                                                                                                             imageExtension)})

    def updateStaffsFromSqlFile(self):
        pass

    def updateCustomersFromSqlFile(self):
        pass

    def updateSparePartsFromSqlFile(self):
        pass



if __name__ == '__main__':
    db = DbHandler()
    db.updatePhones()