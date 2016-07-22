import os

from bs4 import BeautifulSoup
from misc import allstrings,functions
import allpaths


class DataFromNet():

    def __init__(self):
        self.phoneDataHomeUrl = allstrings.main_url
        self.phoneDataBaseUrl = allstrings.base_url
        self.currentDir = allpaths.ALL_DATA_PATH
        self.setUpMainDir()
        self.labelToUpdate = ''

    def setUpMainDir(self):
        if not os.path.exists(self.currentDir):
            os.mkdir(self.currentDir)

    #function to extract html from site and store in text doc
    def pageTextToFile(self,pageLink, filepath):
        try:
            r = functions.getSiteRequests(pageLink)
            with open(filepath,'w') as the_file:
                the_file.write(r.content)
            return True
        except:
            return False

    def getHtmlTextFromFile(self,filePath):
        txt = ""
        if os.path.exists(filePath):
            with open(filePath,"r") as the_file:
                txt = the_file.read()
        return txt


    def fetchAndStoreEachPage(self,filePath):
        sublink = ""
        step = 1
        filedir = os.path.dirname(filePath)
        list_links = {}

        with open(filePath,'r') as a_file:
            sublink = a_file.read()
        list_links['sub_main'] = sublink

        while(sublink <>'#1'):
            filename = os.path.join(filedir,"page_"+str(step)+".txt")
            if step <> 1:
                sublink = self.phoneDataHomeUrl+sublink
            self.pageTextToFile(sublink,filename)
            txt = self.getHtmlTextFromFile(filename)
            s = BeautifulSoup(txt, 'html.parser')
            if(s.find('a',{'class':'pages-next'}) ==  None):
                break
            sublink = s.find('a',{'class':'pages-next'}).get('href')
            step += 1


    def process_html(self,labelToUpdate):
        self.labelToUpdate = ''
        self.labelToUpdate = labelToUpdate
        self.labelToUpdate.setText('Getting new data from net...')
        f = os.path.join(self.currentDir, 'main_html.txt')
        if not os.path.exists(f):
            self.labelToUpdate.setText('No default file located')
            self.pageTextToFile(self.phoneDataBaseUrl,f)
        self.labelToUpdate.setText("Getting data from default file ...")
        content = self.getHtmlTextFromFile(f)
        soup = BeautifulSoup(content, "html.parser")
        main_phone_div = soup.find('div',{'class':'st-text'})
        self.labelToUpdate.setText("OK")
        f = [x for x in main_phone_div.table.find_all('tr')]
        for i in f:
            r = i.find_all('td')
            for h in r:
                self.labelToUpdate = ''
                self.labelToUpdate = labelToUpdate
                tx = h.a.get_text()
                link = h.a.get('href')
                if tx <>"":
                    brand_name = tx[0:tx.index("phones")-1]
                    curr_brand_path = os.path.join(self.currentDir,brand_name)
                    if not os.path.exists(curr_brand_path):
                        self.labelToUpdate.setText("Creating "+brand_name+" folder ...")
                        os.mkdir(curr_brand_path)
                        self.labelToUpdate.setText("OK")
                    w_dir = os.path.join(self.currentDir, brand_name)
                    txt_file = os.path.join(w_dir, brand_name+"_link.txt")
                    if not os.path.exists(txt_file):
                        self.labelToUpdate.setText("Writing link to "+brand_name+" link file")
                        with open(txt_file,'w') as the_file:
                            the_file.write(self.phoneDataHomeUrl+link)
                            self.labelToUpdate.setText("OK")
                    self.labelToUpdate.setText("Storing data to "+brand_name+"'s folder")
                    self.fetchAndStoreEachPage(txt_file)
                    self.labelToUpdate.setText("OK")

















#
#
#
# home_url = allstrings.main_url
# base_url = "http://www.gsmarena.com/makers.php3"
# sub_dir = os.path.dirname(__file__)
# sub_folder = "all_data"
# # curr_dir = os.path.join(sub_dir, sub_folder)
# curr_dir = allpaths.ALL_DATA_PATH
#
#
# #function to extract html from site and store in text doc
# def store_html_text_from_net(link, p):
#     print "Getting data from "+link
#     r = functions.getSiteRequests(link)
#     print "OK"
#     print " Creating new default file..."
#     with open(p,'w') as the_file:
#         print "Writing content to file..."
#         the_file.write(r.content)
#         print "OK"
#
#
# #function to get html from stored doc
# def get_html_text(p):
#     txt = ""
#     if os.path.exists(p):
#         with open(p,"r") as the_file:
#             txt = the_file.read()
#     return txt
#
#
#
#
#
# def store_each_page(f):
#     sublink = ""
#     step = 1
#     filedir = os.path.dirname(f)
#     list_links = {}
#
#     with open(f,'r') as a_file:
#         sublink = a_file.read()
#     list_links['sub_main'] = sublink
#
#     while(sublink <>'#1'):
#         filename = os.path.join(filedir,"page_"+str(step)+".txt")
#         if step <> 1:
#             sublink = home_url+sublink
#         store_html_text_from_net(sublink,filename)
#         txt = get_html_text(filename)
#         s = BeautifulSoup(txt, 'html.parser')
#         if(s.find('a',{'class':'pages-next'}) ==  None):
#             break
#         sublink = s.find('a',{'class':'pages-next'}).get('href')
#         step += 1
#
#
# def process_html():
#     print 'Getting new data from net...'
#     f = os.path.join(curr_dir, 'main_html.txt')
#     if not os.path.exists(f):
#         print 'No default file located'
#         store_html_text_from_net(base_url,f)
#     print "Getting data from default file ..."
#     content = get_html_text(f)
#     soup = BeautifulSoup(content, "html.parser")
#     main_phone_div = soup.find('div',{'class':'st-text'})
#     print "OK"
#     f = [x for x in main_phone_div.table.find_all('tr')]
#     for i in f:
#         r = i.find_all('td')
#         for h in r:
#             tx = h.a.get_text()
#             link = h.a.get('href')
#             if tx <>"":
#                 brand_name = tx[0:tx.index("phones")-1]
#                 curr_brand_path = os.path.join(curr_dir,brand_name)
#                 if not os.path.exists(curr_brand_path):
#                     print "Creating "+brand_name+" folder ..."
#                     os.mkdir(curr_brand_path)
#                     print "OK"
#                 w_dir = os.path.join(curr_dir, brand_name)
#                 txt_file = os.path.join(w_dir, brand_name+"_link.txt")
#                 if not os.path.exists(txt_file):
#                     print "Writing link to "+brand_name+" link file"
#                     with open(txt_file,'w') as the_file:
#                         the_file.write(home_url+link)
#                         print "OK"
#                 print "Storing data to "+brand_name+"'s folder"
#                 store_each_page(txt_file)
#                 print "OK"

# if __name__ == "__main__":
#     if not os.path.exists(curr_dir):
#         os.mkdir(curr_dir)
#     process_html()
#     print "JOB FINISHED"

if __name__ == "__main__":
    dNet = DataFromNet()
    dNet.process_html()
    print "JOB FINISHED"
