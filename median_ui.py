# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'median_tab.ui'
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

class Ui_median(object):
    def setupUi(self, median):
        median.setObjectName(_fromUtf8("median"))
        median.resize(368, 80)
        self.gridLayout = QtGui.QGridLayout(median)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(median)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.size = QtGui.QSpinBox(median)
        self.size.setMinimum(1)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.label = QtGui.QLabel(median)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.retranslateUi(median)
        QtCore.QMetaObject.connectSlotsByName(median)

    def retranslateUi(self, median):
        median.setWindowTitle(_translate("median", "Form", None))
        self.label_2.setText(_translate("median", "Kernel Size:", None))
        self.label.setText(_translate("median", "Reduces \"salt and pepper\" noise", None))

