
from PyQt4 import QtGui,QtCore

class FaderWidget(QtGui.QWidget):

    def __init__(self,newWidget):
        QtGui.QWidget.__init__(self, newWidget)
        self.newWidget = newWidget
        # self.new_pix = QtGui.QPixmap(self.newWidget.size())
        self.new_pix = QtGui.QPixmap(1000,200)
        self.pix_opacity = 0
        # self.render(self.newWidget)
        self.timeline = QtCore.QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(1000)
        self.timeline.start()
        self.show()

    def paintEvent(self, event):
        self.painter = QtGui.QPainter()
        self.painter.begin(self)
        self.painter.setOpacity(self.pix_opacity)
        self.painter.drawPixmap(0,0,self.new_pix)
        self.painter.end()


    def animate(self, value):
        self.pix_opacity = self.pix_opacity + (value/2)
        self.repaint()



