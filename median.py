__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from median_ui import Ui_median

class Median_tab(QtGui.QWidget, Ui_median):

    valueUpdated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.size.valueChanged.connect(self.update)

    def update(self):
        self.emit(QtCore.SIGNAL('valueUpdated()'))

    def value(self):
        return self.size.value()