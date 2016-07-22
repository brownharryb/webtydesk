
import unittest


def runtest(pattern = None):
    print 'Running tests...'
    if pattern == None:
        tests = unittest.defaultTestLoader.discover("tests")
    else:
        patter_with_glob = "%s"%(pattern)
        tests = unittest.defaultTestLoader.discover("tests",pattern=patter_with_glob)
    runner = unittest.TextTestRunner()
    runner.run(tests)

if __name__=='__main__':
    from PyQt4 import QtGui
    import sys
    app = QtGui.QApplication(sys.argv)
    if len(sys.argv) == 1:
        runtest()
    else:
        runtest(pattern=sys.argv[1])
    app.exec_()




