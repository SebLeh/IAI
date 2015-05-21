__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from bilateral_ui import Ui_bilateral

class Bilateral_tab(QtGui.QWidget, Ui_bilateral):

    valueUpdated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.size.valueChanged.connect(self.update)
        self.sigmaSpace.valueChanged.connect(self.update)
        self.sigmaColor.valueChanged.connect(self.update)

    def update(self):
        self.emit(QtCore.SIGNAL('valueUpdated()'))

    def value(self):
        return self.size.value()

    def valueSpace(self):
        return self.sigmaSpace.value()

    def valueColor(self):
        return self.sigmaColor.value()
