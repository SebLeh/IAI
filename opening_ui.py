# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opening_tab.ui'
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

class Ui_opening(object):
    def setupUi(self, opening):
        opening.setObjectName(_fromUtf8("opening"))
        opening.resize(400, 93)
        self.gridLayout = QtGui.QGridLayout(opening)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(opening)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.size = QtGui.QSpinBox(opening)
        self.size.setMinimum(1)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.label = QtGui.QLabel(opening)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(opening)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.iterations = QtGui.QSpinBox(opening)
        self.iterations.setProperty("value", 1)
        self.iterations.setObjectName(_fromUtf8("iterations"))
        self.gridLayout.addWidget(self.iterations, 1, 1, 1, 1)

        self.retranslateUi(opening)
        QtCore.QMetaObject.connectSlotsByName(opening)

    def retranslateUi(self, opening):
        opening.setWindowTitle(_translate("opening", "Form", None))
        self.label_2.setText(_translate("opening", "Erosion followed by Dilation", None))
        self.label.setText(_translate("opening", "Kernel Size:", None))
        self.label_3.setText(_translate("opening", "Iterations", None))

