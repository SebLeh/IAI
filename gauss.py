__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from gauss_ui import Ui_gauss

class Gauss_tab(QtGui.QWidget, Ui_gauss):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)