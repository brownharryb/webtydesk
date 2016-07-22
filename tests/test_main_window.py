import sys,unittest
import main_window
from PyQt4 import QtGui,QtCore,QtTest

class TestMain(unittest.TestCase):

    def setUp(self):
        self.mainApp = main_window.MainApp()

    def test_startApp(self):
        self.assertTrue(self.mainApp.startMain())

    def test_showSplash(self):
        self.assertTrue(self.mainApp.splashWindow.isVisible())
        self.assertTrue(self.mainApp.labelChecking.isVisible())
        self.assertEqual(self.mainApp.labelChecking.text(),'Checking Database..')



# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     unittest.main()
#     app.exec_()
