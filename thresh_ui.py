# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thresh_tab.ui'
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

class Ui_thresh_tab(object):
    def setupUi(self, thresh_tab):
        thresh_tab.setObjectName(_fromUtf8("thresh_tab"))
        thresh_tab.resize(360, 140)
        self.gridLayout = QtGui.QGridLayout(thresh_tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comb_thresh = QtGui.QComboBox(thresh_tab)
        self.comb_thresh.setObjectName(_fromUtf8("comb_thresh"))
        self.gridLayout.addWidget(self.comb_thresh, 4, 0, 1, 2)
        self.in_value = QtGui.QSpinBox(thresh_tab)
        self.in_value.setMaximum(255)
        self.in_value.setProperty("value", 127)
        self.in_value.setObjectName(_fromUtf8("in_value"))
        self.gridLayout.addWidget(self.in_value, 5, 1, 1, 1)
        self.in_max = QtGui.QSpinBox(thresh_tab)
        self.in_max.setMaximum(255)
        self.in_max.setProperty("value", 255)
        self.in_max.setObjectName(_fromUtf8("in_max"))
        self.gridLayout.addWidget(self.in_max, 6, 1, 1, 1)
        self.label_2 = QtGui.QLabel(thresh_tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label = QtGui.QLabel(thresh_tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.note = QtGui.QLabel(thresh_tab)
        self.note.setObjectName(_fromUtf8("note"))
        self.gridLayout.addWidget(self.note, 7, 0, 1, 2)

        self.retranslateUi(thresh_tab)
        QtCore.QMetaObject.connectSlotsByName(thresh_tab)

    def retranslateUi(self, thresh_tab):
        thresh_tab.setWindowTitle(_translate("thresh_tab", "Form", None))
        self.comb_thresh.setToolTip(_translate("thresh_tab", "select Type of Threshold", None))
        self.label_2.setText(_translate("thresh_tab", "Max. Value:", None))
        self.label.setText(_translate("thresh_tab", "Threshold:", None))
        self.note.setText(_translate("thresh_tab", "<html><head/><body><p>Please Note: Image sould be grayscale.<br/>The source image will be converted.</p></body></html>", None))

