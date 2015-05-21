# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'canny_tab.ui'
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

class Ui_canny(object):
    def setupUi(self, canny):
        canny.setObjectName(_fromUtf8("canny"))
        canny.resize(408, 335)
        self.gridLayout = QtGui.QGridLayout(canny)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(canny)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.size = QtGui.QSpinBox(canny)
        self.size.setMinimum(3)
        self.size.setMaximum(7)
        self.size.setSingleStep(2)
        self.size.setProperty("value", 3)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(canny)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.low_thresh = QtGui.QDoubleSpinBox(canny)
        self.low_thresh.setMaximum(255.0)
        self.low_thresh.setProperty("value", 100.0)
        self.low_thresh.setObjectName(_fromUtf8("low_thresh"))
        self.gridLayout.addWidget(self.low_thresh, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(canny)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.high_thresh = QtGui.QDoubleSpinBox(canny)
        self.high_thresh.setMaximum(255.0)
        self.high_thresh.setProperty("value", 200.0)
        self.high_thresh.setObjectName(_fromUtf8("high_thresh"))
        self.gridLayout.addWidget(self.high_thresh, 2, 1, 1, 1)
        self.label = QtGui.QLabel(canny)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)
        self.auto_thresh = QtGui.QCheckBox(canny)
        self.auto_thresh.setObjectName(_fromUtf8("auto_thresh"))
        self.gridLayout.addWidget(self.auto_thresh, 3, 0, 1, 2)

        self.retranslateUi(canny)
        QtCore.QMetaObject.connectSlotsByName(canny)

    def retranslateUi(self, canny):
        canny.setWindowTitle(_translate("canny", "Form", None))
        self.label_4.setText(_translate("canny", "Low Threshold:", None))
        self.label_2.setText(_translate("canny", "High Threshold", None))
        self.label_3.setText(_translate("canny", "Kernel Size:", None))
        self.label.setText(_translate("canny", "<html><head/><body><p>If the edge pixel’s gradient value is <span style=\" font-style:italic;\">higher</span><br/>than the <span style=\" font-style:italic;\">high threshold</span> value, <br/>they are marked as <span style=\" font-style:italic;\">strong edge pixels</span>. </p><p>If the edge pixel’s gradient value is <span style=\" font-style:italic;\">smalle</span>r <br/>than the <span style=\" font-style:italic;\">high threshold</span> value and <span style=\" font-style:italic;\">larger</span> than the <span style=\" font-style:italic;\">low <br/>threshold</span> value, they are marked as <span style=\" font-style:italic;\">weak edge pixels</span>. </p><p>If the pixel value is <span style=\" font-style:italic;\">smaller</span> than the<span style=\" font-style:italic;\"> low threshold</span><br/>value, they will be <span style=\" font-style:italic;\">suppressed</span>. </p><p>The two threshold values are empirically determined <br/>values, which will need to be defined when applying <br/>to different images</p></body></html>", None))
        self.auto_thresh.setText(_translate("canny", "Try automatic Threshold (based on greyscale)", None))

