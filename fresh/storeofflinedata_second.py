import os
import json

from bs4 import BeautifulSoup
from misc import allstrings
import allpaths


class OfflineData():

    def __init__(self):
        self.allBrandsListFileName = allstrings.list_file_name
        self.allDataDir = allpaths.ALL_DATA_PATH
        self.phoneMainUrl = allstrings.main_url
        self.allInfoFileName = allstrings.all_info_name
        self.allModelsListFileName = allstrings.model_list_file
        self.listOfAllBrands = []
        self.setUp()
        self.labelToUpdate = ''


    def setUp(self):
        self.writeAllBrandListToFile(self.allBrandsListFileName)





    def writeAllBrandListToFile(self,allBrandsTextFile):
        with open(os.path.join(self.allDataDir,allBrandsTextFile),'w') as a_file:
            for i in os.listdir(self.allDataDir):
                if not '.txt' in i:
                    self.listOfAllBrands.append(i)
                    a_file.write(i+'\n')

    def storeAllData(self,labelToUpdate):
        self.labelToUpdate = ''
        self.labelToUpdate = labelToUpdate
        d = {}

        for brand in self.listOfAllBrands:
            brandFolderPath = os.path.join(self.allDataDir,brand)
            allFilesInBrandFolder = os.listdir(brandFolderPath)
            for eachFileName in allFilesInBrandFolder:
                if 'page' in eachFileName:
                    modelDataDict = self.getModelDataDict(os.path.join(brandFolderPath,eachFileName),brand)
                    d.update(modelDataDict)
            allInfoFilePath = os.path.join(brandFolderPath,self.allInfoFileName)
            with open(allInfoFilePath,'w') as infoFile:
                json.dump(d,infoFile,indent=4)
            modelList = d.keys()
            modelListFilePath = os.path.join(brandFolderPath,self.allModelsListFileName)
            self.labelToUpdate.setText('Storing '+str(brand)+'\'s models data ')
            with open(modelListFilePath, 'w') as modelListFile:
                for i in modelList:
                    modelListFile.write(i+'\n')
                d = {}





    def getModelDataDict(self, fileName, brandName):
        d = {}
        with open(fileName, 'r') as aFile:
            txtInFile = aFile.read()
            soup = BeautifulSoup(txtInFile, 'html.parser')
            makers = soup.find('div',{'class':'makers'})
            data = makers.find_all('li')
            for i in data:
                modelLink = self.phoneMainUrl+i.find('a').get('href')
                modelName = i.get_text()
                imgLink = i.find('img').get('src')
                l = [brandName,modelLink,imgLink]
                d[modelName] = l
        return d

# if __name__ == '__main__':
#     offlineObj = OfflineData()
#     # offlineObj.storeAllData()








# # working_folder = 'all_data'
# list_file_name = allstrings.list_file_name
# all_info_name = allstrings.all_info_name
# model_list_file = allstrings.model_list_file
# main_url = allstrings.main_url
#
#
# curr_dir = os.path.dirname(__file__)
# # working_dir = os.path.join(curr_dir, working_folder)
# working_dir = allpaths.ALL_DATA_PATH
# li = os.listdir(working_dir)
#
#
# def list_all_brands():
#     with open(os.path.join(working_dir,list_file_name),'w') as a_file:
#         for i in li:
#             if not '.txt' in i:
#                 a_file.write(i+'\n')
#
#
# def store_all_data():
#     d = {}
#     for brand_name in li:
#         if not '.txt' in brand_name:
#
#             c_dir = os.path.join(working_dir,brand_name)
#             li_files = os.listdir(c_dir)
#             for j in li_files:
#                 if 'page' in j:
#                     di = get_model_data(os.path.join(c_dir,j),brand_name)
#                     d.update(di)
#             fnm = os.path.join(c_dir,all_info_name)
#             with open(fnm,'w') as b_file:
#                 print brand_name+'--'+str(len(d))
#                 json.dump(d,b_file, indent = 4)
#             modellist = d.keys()
#             modellistfilepath = os.path.join(c_dir,model_list_file)
#             with open(modellistfilepath, 'w') as c_file:
#                 for i in modellist:
#                     c_file.write(i+'\n')
#                 d = {}
#
#
#
#
# def get_model_data(file_nm, brand_nm):
#     d = {}
#     with open(file_nm, 'r') as a_file:
#         txt = a_file.read()
#         soup = BeautifulSoup(txt, 'html.parser')
#         mkers = soup.find('div',{'class':'makers'})
#         data = mkers.find_all('li')
#
#         for i in data:
#             model_link = main_url+i.find('a').get('href')
#             model_name = i.get_text()
#             imglink = i.find('img').get('src')
#             l = [brand_nm,model_link,imglink]
#             d[model_name] = l
#     return d
#
#
#
#
# if __name__ == '__main__':
#     list_all_brands()
#     store_all_data()
