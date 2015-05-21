# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobel_tab.ui'
#
# Created: Thu May 21 17:46:20 2015
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

class Ui_sobel(object):
    def setupUi(self, sobel):
        sobel.setObjectName(_fromUtf8("sobel"))
        sobel.resize(400, 263)
        self.gridLayout = QtGui.QGridLayout(sobel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(sobel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)
        self.dY = QtGui.QCheckBox(sobel)
        self.dY.setObjectName(_fromUtf8("dY"))
        self.gridLayout.addWidget(self.dY, 1, 0, 1, 1)
        self.dX = QtGui.QCheckBox(sobel)
        self.dX.setChecked(True)
        self.dX.setObjectName(_fromUtf8("dX"))
        self.gridLayout.addWidget(self.dX, 0, 0, 1, 1)
        self.label = QtGui.QLabel(sobel)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.size = QtGui.QSpinBox(sobel)
        self.size.setMinimum(-1)
        self.size.setMaximum(7)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(sobel)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.depth = QtGui.QComboBox(sobel)
        self.depth.setObjectName(_fromUtf8("depth"))
        self.gridLayout.addWidget(self.depth, 3, 1, 1, 1)

        self.retranslateUi(sobel)
        QtCore.QMetaObject.connectSlotsByName(sobel)

    def retranslateUi(self, sobel):
        sobel.setWindowTitle(_translate("sobel", "Form", None))
        self.label_2.setText(_translate("sobel", "<html><head/><body><p>If Kernel size equals -1, Scharr filter is used:</p><p>[-3 0 3] <br/>[-10 0 10] <br/>[-3 0 3]<br/>instead of Sobel<br/>[-1 0 1]<br/>[-2 0 2]<br/>[-1 0 1]</p></body></html>", None))
        self.dY.setText(_translate("sobel", "derivate Y", None))
        self.dX.setText(_translate("sobel", "derivate X", None))
        self.label.setText(_translate("sobel", "Kernel Size:", None))
        self.label_3.setText(_translate("sobel", "Depth of destination image (bit)", None))

