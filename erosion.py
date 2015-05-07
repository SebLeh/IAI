__author__ = 'uleob'

from PyQt4 import QtCore, QtGui
from erosion_ui import Ui_erosion

class Erosion_tab(QtGui.QWidget, Ui_erosion):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)