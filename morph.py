__author__ = 'uleob'

from PyQt4 import QtGui
from morph_ui import Ui_morph

class Morph_tab(QtGui.QWidget, Ui_morph):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)