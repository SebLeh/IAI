__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from thresh_ui import Ui_thresh_tab

class Thresh_tab(QtGui.QWidget, Ui_thresh_tab):

    valueUpdated = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setup()

    def setup(self):
        itemList = QtCore.QStringList()
        itemList.append("Binary Threshold")
        itemList.append("Binary Threshold, inverted")
        itemList.append("Adaptive Threshold, mean")
        itemList.append("Adaptive Threshold, Gaussian")
        itemList.append("Otsu Threshold")
        self.comb_thresh.addItems(itemList)

        self.in_value.valueChanged.connect(self.update)

    def update(self):
        self.emit(QtCore.SIGNAL('valueUpdated(int)'), self.in_value.value())

    def return_values(self):
        return self.in_value.value()
