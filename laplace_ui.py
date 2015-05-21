# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laplace_tab.ui'
#
# Created: Thu May 21 14:46:08 2015
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
        laplace.resize(400, 300)
        self.label = QtGui.QLabel(laplace)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(laplace)
        QtCore.QMetaObject.connectSlotsByName(laplace)

    def retranslateUi(self, laplace):
        laplace.setWindowTitle(_translate("laplace", "Form", None))
        self.label.setText(_translate("laplace", "Laplace Derivate", None))

