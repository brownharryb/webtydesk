import sys
from forms.animation_test import Ui_animationTest
from custom_widgets.custom_notify import FaderWidget
from PyQt4 import QtGui,QtCore

class AnimationTest():

    def __init__(self):
        self.animui = Ui_animationTest()
        self.window = QtGui.QMainWindow()
        self.animui.setupUi(self.window)

    def showWindow(self):
        self.window.show()

        self.put3()

    def putObj(self):
        self.movie = QtGui.QMovie('forms\\ui_files\\images\\animated\\loading.gif')
        self.label = QtGui.QLabel()
        self.layout = QtGui.QHBoxLayout()
        self.label.setMovie(self.movie)
        # self.label.setStyleSheet('background-color:#000000;')
        self.layout.addWidget(self.label)
        self.animui.centralwidget.setLayout(self.layout)
        self.movie.start()

    def put2(self):
        self.layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel()
        self.layout.addWidget(self.label)
        self.animui.centralwidget.setLayout(self.layout)
    def put3(self):
        self.layout = QtGui.QVBoxLayout()
        self.progres = QtGui.QProgressBar(self.window)
        self.progres.setMaximumHeight(20)
        # self.progres.setValue(50)
        # self.fader = FaderWidget(self.progres)
        self.layout.addWidget(self.progres)
        self.animui.centralwidget.setLayout(self.layout)

        self.e = QtGui.QGraphicsOpacityEffect()
        self.progres.setGraphicsEffect(self.e)
        self.o = QtCore.QPropertyAnimation(self.e,'opacity')
        self.o.setDuration(5000)
        self.o.setEasingCurve(QtCore.QEasingCurve.InBack)
        self.o.setStartValue(1)
        self.o.setEndValue(0)

        self.o.start()






if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    anim = AnimationTest()
    anim.showWindow()
    app.exec_()