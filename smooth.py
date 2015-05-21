__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from smooth_ui import Ui_smooth

class Smooth_tab(QtGui.QWidget, Ui_smooth):

    valueUpdated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.smooth_size.valueChanged.connect(self.update)

    def update(self):
        self.emit(QtCore.SIGNAL('valueUpdated()'))

    def value(self):
        return self.smooth_size.value()