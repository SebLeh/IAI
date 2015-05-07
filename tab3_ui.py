# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab3.ui'
#
# Created: Tue Apr 28 14:28:15 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(140, 50, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 140, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.radioButton.setText(_translate("Form", "RadioButton", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
        self.label.setText(_translate("Form", "TextLabel", None))

