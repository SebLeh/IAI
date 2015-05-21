# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morph_tab.ui'
#
# Created: Thu May 21 17:46:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_morph(object):
    def setupUi(self, morph):
        morph.setObjectName(_fromUtf8("morph"))
        morph.resize(400, 116)
        self.gridLayout = QtGui.QGridLayout(morph)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(morph)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.size = QtGui.QSpinBox(morph)
        self.size.setMinimum(1)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(morph)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.iterations = QtGui.QSpinBox(morph)
        self.iterations.setProperty("value", 1)
        self.iterations.setObjectName(_fromUtf8("iterations"))
        self.gridLayout.addWidget(self.iterations, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(morph)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.retranslateUi(morph)
        QtCore.QMetaObject.connectSlotsByName(morph)

    def retranslateUi(self, morph):
        morph.setWindowTitle(_translate("morph", "Form", None))
        self.label.setText(_translate("morph", "Kernel Size:", None))
        self.label_3.setText(_translate("morph", "Iterations", None))
        self.label_2.setText(_translate("morph", "Difference between Dilation and Erosion", None))

