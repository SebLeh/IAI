__author__ = 'uleob'

from PyQt4 import QtCore, QtGui
from opening_ui import Ui_opening

class Opening_tab(QtGui.QWidget, Ui_opening):

    valueUpdated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.size.valueChanged.connect(self.update)
        self.iterations.valueChanged.connect(self.update)

    def update(self):
        self.emit(QtCore.SIGNAL('valueUpdated()'))

    def value(self):
        return self.size.value()

    def valueIterations(self):
        return self.iterations.value()
