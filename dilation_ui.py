# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dilation_tab.ui'
#
# Created: Tue May 12 09:17:17 2015
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

class Ui_dilation(object):
    def setupUi(self, dilation):
        dilation.setObjectName(_fromUtf8("dilation"))
        dilation.resize(400, 300)
        self.label = QtGui.QLabel(dilation)
        self.label.setGeometry(QtCore.QRect(20, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(dilation)
        QtCore.QMetaObject.connectSlotsByName(dilation)

    def retranslateUi(self, dilation):
        dilation.setWindowTitle(_translate("dilation", "Form", None))
        self.label.setText(_translate("dilation", "Dilation", None))

