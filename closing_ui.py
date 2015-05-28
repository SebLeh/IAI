# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'closing_tab.ui'
#
# Created: Tue May 26 11:15:51 2015
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

class Ui_closing(object):
    def setupUi(self, closing):
        closing.setObjectName(_fromUtf8("closing"))
        closing.resize(388, 138)
        self.gridLayout = QtGui.QGridLayout(closing)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(closing)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.size = QtGui.QSpinBox(closing)
        self.size.setMinimum(1)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(closing)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.label_3 = QtGui.QLabel(closing)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.iterations = QtGui.QSpinBox(closing)
        self.iterations.setProperty("value", 1)
        self.iterations.setObjectName(_fromUtf8("iterations"))
        self.gridLayout.addWidget(self.iterations, 1, 1, 1, 1)

        self.retranslateUi(closing)
        QtCore.QMetaObject.connectSlotsByName(closing)

    def retranslateUi(self, closing):
        closing.setWindowTitle(_translate("closing", "Form", None))
        self.label.setText(_translate("closing", "Kernel Size:", None))
        self.label_2.setText(_translate("closing", "Dilation followed by Erosion", None))
        self.label_3.setText(_translate("closing", "Iterations", None))

