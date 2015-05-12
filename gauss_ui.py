# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gauss_tab.ui'
#
# Created: Tue May 12 09:17:16 2015
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
        gauss.resize(400, 300)
        self.label = QtGui.QLabel(gauss)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(gauss)
        QtCore.QMetaObject.connectSlotsByName(gauss)

    def retranslateUi(self, gauss):
        gauss.setWindowTitle(_translate("gauss", "Form", None))
        self.label.setText(_translate("gauss", "Gaussian Filter", None))

