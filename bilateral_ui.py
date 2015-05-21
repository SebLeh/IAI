# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bilateral_tab.ui'
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

class Ui_bilateral(object):
    def setupUi(self, bilateral):
        bilateral.setObjectName(_fromUtf8("bilateral"))
        bilateral.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(bilateral)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(bilateral)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(bilateral)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.sigmaSpace = QtGui.QSpinBox(bilateral)
        self.sigmaSpace.setMaximum(255)
        self.sigmaSpace.setProperty("value", 75)
        self.sigmaSpace.setObjectName(_fromUtf8("sigmaSpace"))
        self.gridLayout.addWidget(self.sigmaSpace, 1, 1, 1, 1)
        self.size = QtGui.QSpinBox(bilateral)
        self.size.setMinimum(1)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.label = QtGui.QLabel(bilateral)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        self.label_4 = QtGui.QLabel(bilateral)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.sigmaColor = QtGui.QSpinBox(bilateral)
        self.sigmaColor.setMaximum(255)
        self.sigmaColor.setProperty("value", 75)
        self.sigmaColor.setObjectName(_fromUtf8("sigmaColor"))
        self.gridLayout.addWidget(self.sigmaColor, 2, 1, 1, 1)

        self.retranslateUi(bilateral)
        QtCore.QMetaObject.connectSlotsByName(bilateral)

    def retranslateUi(self, bilateral):
        bilateral.setWindowTitle(_translate("bilateral", "Form", None))
        self.label_3.setText(_translate("bilateral", "Sigma Space", None))
        self.label_2.setText(_translate("bilateral", "Kernel Size:", None))
        self.label.setText(_translate("bilateral", "<html><head/><body><p>Reduces noise, while preserving edges.<br/>Needs more computation and therefor is slower.</p><p>For real-time applications size shouldn\'t be &gt;5.<br/>If size equals 0, it will be computed from Sigma Space.</p><p>Sigma Space: A larger value of the parameter means that farther pixels<br/>will influence each other as long as their colors are close enough</p><p>Sigma Color: A larger value of the parameter means that farther colors within<br/>the pixel neighborhood (Sigma Space) will be mixed together, <br/>resulting in larger areas of semi-equal color.</p></body></html>", None))
        self.label_4.setText(_translate("bilateral", "Sigma Color", None))

