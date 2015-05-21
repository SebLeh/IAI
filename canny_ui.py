# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'canny_tab.ui'
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

class Ui_canny(object):
    def setupUi(self, canny):
        canny.setObjectName(_fromUtf8("canny"))
        canny.resize(400, 300)
        self.label = QtGui.QLabel(canny)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(canny)
        QtCore.QMetaObject.connectSlotsByName(canny)

    def retranslateUi(self, canny):
        canny.setWindowTitle(_translate("canny", "Form", None))
        self.label.setText(_translate("canny", "Canny Edge Detection", None))

