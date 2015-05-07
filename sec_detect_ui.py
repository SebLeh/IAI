# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sec_detect.ui'
#
# Created: Thu May 07 10:42:56 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(697, 425)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = GraphicsView(self.centralwidget)
        # self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.lbl_scale = QtGui.QLabel(self.tab_1)
        self.lbl_scale.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.lbl_scale.setObjectName(_fromUtf8("lbl_scale"))
        self.scale = QtGui.QDoubleSpinBox(self.tab_1)
        self.scale.setGeometry(QtCore.QRect(110, 10, 62, 22))
        self.scale.setMaximum(3.0)
        self.scale.setSingleStep(0.25)
        self.scale.setProperty("value", 0.5)
        self.scale.setObjectName(_fromUtf8("scale"))
        self.cb_grey = QtGui.QCheckBox(self.tab_1)
        self.cb_grey.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.cb_grey.setObjectName(_fromUtf8("cb_grey"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuFilter_Settings = QtGui.QMenu(self.menuFile)
        self.menuFilter_Settings.setObjectName(_fromUtf8("menuFilter_Settings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ressources/open_file-icon.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave_Settings = QtGui.QAction(MainWindow)
        self.actionSave_Settings.setObjectName(_fromUtf8("actionSave_Settings"))
        self.actionLoad_settings = QtGui.QAction(MainWindow)
        self.actionLoad_settings.setObjectName(_fromUtf8("actionLoad_settings"))
        self.actionRestore_Default = QtGui.QAction(MainWindow)
        self.actionRestore_Default.setObjectName(_fromUtf8("actionRestore_Default"))
        self.menuFilter_Settings.addAction(self.actionSave_Settings)
        self.menuFilter_Settings.addAction(self.actionLoad_settings)
        self.menuFilter_Settings.addSeparator()
        self.menuFilter_Settings.addAction(self.actionRestore_Default)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuFilter_Settings.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Section Detector", None))
        self.lbl_scale.setText(_translate("MainWindow", "Scale:", None))
        self.cb_grey.setText(_translate("MainWindow", "Greyscale", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Display settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "+", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "add new filter", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuFilter_Settings.setTitle(_translate("MainWindow", "Filter Settings", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setToolTip(_translate("MainWindow", "open image file", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings", None))
        self.actionLoad_settings.setText(_translate("MainWindow", "Load settings", None))
        self.actionRestore_Default.setText(_translate("MainWindow", "Restore Default", None))

from pyqtgraph import GraphicsView
