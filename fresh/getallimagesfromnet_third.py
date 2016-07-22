import os,json,allpaths
from PyQt4 import QtGui
from urllib import urlretrieve
from misc import functions,allstrings




class StoreImages():

    def __init__(self):
        self.allImagesFolderName = allstrings.all_images_folder
        self.allDataDir = allpaths.ALL_DATA_PATH
        self.allInfoJson = allstrings.all_info_name
        self.unwantedImageNameCharacters = allstrings.unwanted_imagename_chars
        self.setUp()


    def setUp(self):
        self.listOfAllBrands = [x for x in os.listdir(self.allDataDir) if not '.txt' in x]


    def processAllImages(self,labelToUpdate):
        self.labelToUpdate = ''
        self.labelToUpdate = labelToUpdate
        for brand in self.listOfAllBrands:
            brandFolder = os.path.join(self.allDataDir,brand)
            brandImagesFolderPath = os.path.join(brandFolder,self.allImagesFolderName)
            if not os.path.exists(brandImagesFolderPath):
                os.mkdir(brandImagesFolderPath)
            with open(os.path.join(brandFolder,self.allInfoJson), 'r') as infoFile:
                modelsDicts = json.loads(infoFile.read())
                models = modelsDicts.keys()
                for eachModel in models:
                    imageLink = modelsDicts[eachModel][2]
                    imageExtension = functions.getImageExtension(imageLink)
                    for weedChar in self.unwantedImageNameCharacters:
                        if weedChar in eachModel:
                            eachModel = eachModel.replace(weedChar,'_')
                    pathUsedToStoreImage = os.path.join(brandImagesFolderPath,eachModel+imageExtension)
                    if not os.path.exists(pathUsedToStoreImage) or os.path.getsize(pathUsedToStoreImage)<1:
                        if self.retrieveAndStoreImageFromNet(imageLink,pathUsedToStoreImage):
                            self.labelToUpdate.setText('Downloading image for '+str(brand)+' '+str(eachModel))
                        else:
                            raise Exception
        self.labelToUpdate.setText('All Images updated!!')



    def retrieveAndStoreImageFromNet(self,imageUrl, pathToStoreImage):
        try:
            urlretrieve(imageUrl,pathToStoreImage)
            return True
        except:
            return False






if __name__ == '__main__':
    imgs = StoreImages()
    imgs.processAllImages()












#
#
#
# imgfolder = 'all_images'
# # all_data_folder = 'all_data'
# json_fl = 'all_info.json'
# unwanted_chars = ['/', '\\', '*',':)']
# curr_dir = os.path.dirname(__file__)
# # working_dir = os.path.join(curr_dir, all_data_folder)
# working_dir = allpaths.ALL_DATA_PATH
#
#
# main_image_url = 'http://cdn2.gsmarena.com/vv/pics/'
#
# li = [x for x in os.listdir(working_dir) if not '.txt' in x]
#
#
# for i in li:
#     f_dir = os.path.join(working_dir,i)
#     imgpath = os.path.join(f_dir, imgfolder)
#     if not os.path.exists(imgpath):
#         os.mkdir(imgpath)
#     with open(os.path.join(f_dir,json_fl),'r') as the_file:
#         d = json.loads(the_file.read())
#         l = d.keys()
#         for j in l:
#             mg = d[j][2]
#             imageExtension = functions.getImageExtension(mg)
#
#             for z in unwanted_chars:
#                 if z in j:
#                     j= j.replace(z,'_')
#             p = os.path.join(imgpath, j+imageExtension)
#             if not os.path.exists(p):
#                 functions.retrieveAndStoreImageFromNet(mg,p)
