__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from bilateral_ui import Ui_bilateral

class Bilateral_tab(QtGui.QWidget, Ui_bilateral):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)