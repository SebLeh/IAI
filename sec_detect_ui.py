# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sec_detect.ui'
#
# Created: Tue Jun 16 13:51:27 2015
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
        MainWindow.resize(474, 431)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = GraphicsView(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = GraphicsView(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 5, 0, 1, 1)
        self.lbl_scale = QtGui.QLabel(self.groupBox)
        self.lbl_scale.setObjectName(_fromUtf8("lbl_scale"))
        self.gridLayout_3.addWidget(self.lbl_scale, 0, 0, 1, 1)
        self.scale = QtGui.QDoubleSpinBox(self.groupBox)
        self.scale.setMinimum(0.1)
        self.scale.setMaximum(3.0)
        self.scale.setSingleStep(0.1)
        self.scale.setProperty("value", 0.3)
        self.scale.setObjectName(_fromUtf8("scale"))
        self.gridLayout_3.addWidget(self.scale, 0, 1, 1, 1)
        self.cb_roi = QtGui.QCheckBox(self.groupBox)
        self.cb_roi.setObjectName(_fromUtf8("cb_roi"))
        self.gridLayout_3.addWidget(self.cb_roi, 2, 0, 1, 1)
        self.cb_grey = QtGui.QCheckBox(self.groupBox)
        self.cb_grey.setObjectName(_fromUtf8("cb_grey"))
        self.gridLayout_3.addWidget(self.cb_grey, 1, 0, 1, 1)
        self.btn_add = QtGui.QPushButton(self.groupBox)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.gridLayout_3.addWidget(self.btn_add, 5, 1, 1, 1)
        self.combbox_detector = QtGui.QComboBox(self.groupBox)
        self.combbox_detector.setObjectName(_fromUtf8("combbox_detector"))
        self.gridLayout_3.addWidget(self.combbox_detector, 8, 1, 1, 1)
        self.sortList = QtGui.QListWidget(self.groupBox)
        self.sortList.setObjectName(_fromUtf8("sortList"))
        self.gridLayout_3.addWidget(self.sortList, 6, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 8, 0, 1, 1)
        self.detector_area = QtGui.QScrollArea(self.groupBox)
        self.detector_area.setWidgetResizable(True)
        self.detector_area.setObjectName(_fromUtf8("detector_area"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 294, 67))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.detector_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.detector_area, 9, 0, 1, 2)
        self.filter_area = QtGui.QScrollArea(self.groupBox)
        self.filter_area.setWidgetResizable(True)
        self.filter_area.setObjectName(_fromUtf8("filter_area"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 294, 67))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.filter_area.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.filter_area, 7, 0, 1, 2)
        self.btn_apply = QtGui.QPushButton(self.groupBox)
        self.btn_apply.setObjectName(_fromUtf8("btn_apply"))
        self.gridLayout_3.addWidget(self.btn_apply, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 3, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 21))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Section Detector", None))
        # self.label_3.setText(_translate("MainWindow", "init", None))
        # self.label.setText(_translate("MainWindow", "img", None))
        self.label_2.setText(_translate("MainWindow", "Define the order of the filters to be applied:", None))
        self.lbl_scale.setText(_translate("MainWindow", "Scale:", None))
        self.cb_roi.setText(_translate("MainWindow", "Activate ROI", None))
        self.cb_grey.setText(_translate("MainWindow", "Greyscale", None))
        self.btn_add.setText(_translate("MainWindow", "Add new Filter", None))
        self.label_4.setText(_translate("MainWindow", "Select Type of Contour Detector", None))
        self.btn_apply.setText(_translate("MainWindow", "Apply Changes", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuFilter_Settings.setTitle(_translate("MainWindow", "Filter Settings", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setToolTip(_translate("MainWindow", "open image file", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings", None))
        self.actionLoad_settings.setText(_translate("MainWindow", "Load settings", None))
        self.actionRestore_Default.setText(_translate("MainWindow", "Restore Default", None))

from pyqtgraph import GraphicsView
