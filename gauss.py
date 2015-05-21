__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from gauss_ui import Ui_gauss

class Gauss_tab(QtGui.QWidget, Ui_gauss):

    valueUpdated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.size.valueChanged.connect(self.update)
        self.sigmaX.valueChanged.connect(self.update)
        self.sigmaY.valueChanged.connect(self.update)

    def update(self):
        self.emit(QtCore.SIGNAL('valueUpdated()'))

    def value(self):
        return self.size.value()

    def valueX(self):
        return self.sigmaX.value()

    def valueY(self):
        return self.sigmaY.value()