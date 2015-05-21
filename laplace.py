__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from laplace_ui import Ui_laplace

class Laplace_tab(QtGui.QWidget, Ui_laplace):

    valueUpdated = QtCore.pyqtSignal

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.init()

        self.size.valueChanged.connect(self.update)
        self.depth.currentIndexChanged.connect(self.update)

    def init(self):
        itemList = QtCore.QStringList()
        itemList.append("16 bit (CV_16S)")
        itemList.append("32 bit (CV_32F)")
        itemList.append("64 bit (CV_64F)")
        self.depth.addItems(itemList)
        self.depth.setCurrentIndex(2)

    def update(self):
        self.emit(QtCore.SIGNAL('valueUpdated()'))

    def value(self):
        return self.size.value()

    def valueDepth(self):
        return self.depth.currentIndex()