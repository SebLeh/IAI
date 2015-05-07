__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from median_ui import Ui_median

class Median_tab(QtGui.QWidget, Ui_median):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)