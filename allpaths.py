import os
from misc import allstrings

currentPath = os.path.join(os.path.dirname(__file__))
ALL_DATA_PATH = os.path.join(os.path.dirname(__file__), allstrings.all_data_name)
ALL_BRANDS_FILENAME = os.path.join(ALL_DATA_PATH, allstrings.list_file_name)

def get_model_list_filepath(brandname):
    a = os.path.join(ALL_DATA_PATH,brandname)
    b = os.path.join(a, allstrings.model_list_file)
    return b

def get_model_image_pathname(brandname, model_name,imageExtension):
    image_name = allstrings.remove_unwanted_chars_in_string(model_name)
    a = os.path.join(ALL_DATA_PATH, brandname,allstrings.all_images_folder)
    b = os.path.join(a, image_name+imageExtension)
    return b

def getRelativeImagePath(brandname, model_name,imageExtension):
    image_name = allstrings.remove_unwanted_chars_in_string(model_name)
    return os.path.join(allstrings.all_data_name,brandname,allstrings.all_images_folder, image_name+imageExtension)


def getAllInfoJsonFileForBrand(brandName):
    return os.path.join(ALL_DATA_PATH,brandName,allstrings.all_info_name)

def getActualPicPathFromDb(picPathFromDb):
    pass

def getAnimatedLoaderPath(imageName):
    pt = os.path.join(currentPath,'forms','ui_files','images','animated',imageName)
    return pt

def createFoldersIfNotExist():
        paths = ['debug','error','info','warn']
        for i in paths:
            p = os.path.join(currentPath,'log',i)
            if not os.path.exists(p):
                os.mkdir(p)

def getInfoLogFilePath():
    return os.path.join(currentPath,'log','info','webty_info.log')

def getDebugLogFilePath():
    return os.path.join(currentPath,'log','debug','webty_debug.log')

def getWarningLogFilePath():
    return os.path.join(currentPath,'log','warn','webty_warning.log')

def getErrorLogFilePath():
    return os.path.join(currentPath,'log','error','webty_error.log')