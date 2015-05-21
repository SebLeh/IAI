__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from morph_ui import Ui_morph

class Morph_tab(QtGui.QWidget, Ui_morph):

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