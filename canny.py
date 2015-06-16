__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from canny_ui import Ui_canny

class Canny_tab(QtGui.QWidget, Ui_canny):

    valueUpdated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.size.valueChanged.connect(self.update)
        self.low_thresh.valueChanged.connect(self.update)
        self.high_thresh.valueChanged.connect(self.update)
        self.auto_thresh.stateChanged.connect(self.update)

        self.recent_size = -1

    def update(self):

        if self.auto_thresh.isChecked():
            self.low_thresh.setDisabled(True)
            self.high_thresh.setDisabled(True)
        else:
            self.low_thresh.setEnabled(True)
            self.high_thresh.setEnabled(True)

        self.emit(QtCore.SIGNAL('valueUpdated()'))

    def value(self):
        try:
            self.recent_size = self.size.value()
            return self.size.value()
        except Exception, e:
            return self.recent_size

    def valueLow(self):
        return self.low_thresh.value()

    def valueHigh(self):
        return self.high_thresh.value()