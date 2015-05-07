__author__ = 'uleob'

from PyQt4 import QtGui
from canny_ui import Ui_canny

class Canny_tab(QtGui.QWidget, Ui_canny):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)