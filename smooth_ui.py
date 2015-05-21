# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smooth_tab.ui'
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

class Ui_smooth(object):
    def setupUi(self, smooth):
        smooth.setObjectName(_fromUtf8("smooth"))
        smooth.resize(269, 38)
        self.horizontalLayout = QtGui.QHBoxLayout(smooth)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(smooth)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.smooth_size = QtGui.QSpinBox(smooth)
        self.smooth_size.setMinimum(1)
        self.smooth_size.setSingleStep(2)
        self.smooth_size.setProperty("value", 3)
        self.smooth_size.setObjectName(_fromUtf8("smooth_size"))
        self.horizontalLayout.addWidget(self.smooth_size)

        self.retranslateUi(smooth)
        QtCore.QMetaObject.connectSlotsByName(smooth)

    def retranslateUi(self, smooth):
        smooth.setWindowTitle(_translate("smooth", "Form", None))
        self.label.setText(_translate("smooth", "Kernel Size:", None))

