__author__ = 'uleob'

from PyQt4 import QtGui
from sobel_ui import Ui_sobel

class Sobel_tab(QtGui.QWidget, Ui_sobel):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)