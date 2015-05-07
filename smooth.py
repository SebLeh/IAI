__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from smooth_ui import Ui_smooth

class Smooth_tab(QtGui.QWidget, Ui_smooth):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)