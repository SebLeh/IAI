# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gauss_tab.ui'
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

class Ui_gauss(object):
    def setupUi(self, gauss):
        gauss.setObjectName(_fromUtf8("gauss"))
        gauss.resize(391, 212)
        self.gridLayout = QtGui.QGridLayout(gauss)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sigmaY = QtGui.QDoubleSpinBox(gauss)
        self.sigmaY.setDecimals(4)
        self.sigmaY.setSingleStep(0.1)
        self.sigmaY.setObjectName(_fromUtf8("sigmaY"))
        self.gridLayout.addWidget(self.sigmaY, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(gauss)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.size = QtGui.QSpinBox(gauss)
        self.size.setMinimum(1)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.sigmaX = QtGui.QDoubleSpinBox(gauss)
        self.sigmaX.setDecimals(4)
        self.sigmaX.setSingleStep(0.1)
        self.sigmaX.setObjectName(_fromUtf8("sigmaX"))
        self.gridLayout.addWidget(self.sigmaX, 1, 1, 1, 1)
        self.label = QtGui.QLabel(gauss)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(gauss)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(gauss)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)

        self.retranslateUi(gauss)
        QtCore.QMetaObject.connectSlotsByName(gauss)

    def retranslateUi(self, gauss):
        gauss.setWindowTitle(_translate("gauss", "Form", None))
        self.label_2.setText(_translate("gauss", "Sigma X", None))
        self.label.setText(_translate("gauss", "Kernel Size:", None))
        self.label_3.setText(_translate("gauss", "Sigma Y", None))
        self.label_4.setText(_translate("gauss", "<html><head/><body><p>If only Sigma X is specified (Sigma Y equals 0), <br/>Sigma Y is taken as equal to Sigma X.</p><p>If both, X and Y, equal 0, they are calculated by the kernel size.</p></body></html>", None))

