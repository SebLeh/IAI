# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laplace_tab.ui'
#
# Created: Thu May 21 17:46:20 2015
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

class Ui_laplace(object):
    def setupUi(self, laplace):
        laplace.setObjectName(_fromUtf8("laplace"))
        laplace.resize(400, 82)
        self.gridLayout = QtGui.QGridLayout(laplace)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.size = QtGui.QSpinBox(laplace)
        self.size.setMinimum(1)
        self.size.setMaximum(31)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.label = QtGui.QLabel(laplace)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(laplace)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.depth = QtGui.QComboBox(laplace)
        self.depth.setObjectName(_fromUtf8("depth"))
        self.gridLayout.addWidget(self.depth, 1, 1, 1, 1)

        self.retranslateUi(laplace)
        QtCore.QMetaObject.connectSlotsByName(laplace)

    def retranslateUi(self, laplace):
        laplace.setWindowTitle(_translate("laplace", "Form", None))
        self.label.setText(_translate("laplace", "Kernel Size: ", None))
        self.label_2.setText(_translate("laplace", "Depth of destination image (bit)", None))

