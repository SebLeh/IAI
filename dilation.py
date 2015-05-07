__author__ = 'uleob'

from PyQt4 import QtGui
from dilation_ui import Ui_dilation

class Dilation_tab(QtGui.QWidget, Ui_dilation):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)