# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erosion_tab.ui'
#
# Created: Thu May 07 15:26:42 2015
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

class Ui_erosion(object):
    def setupUi(self, erosion):
        erosion.setObjectName(_fromUtf8("erosion"))
        erosion.resize(400, 300)

        self.retranslateUi(erosion)
        QtCore.QMetaObject.connectSlotsByName(erosion)

    def retranslateUi(self, erosion):
        erosion.setWindowTitle(_translate("erosion", "Form", None))

