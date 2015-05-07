__author__ = 'uleob'

from PyQt4 import QtGui
from laplace_ui import Ui_laplace

class Laplace_tab(QtGui.QWidget, Ui_laplace):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)