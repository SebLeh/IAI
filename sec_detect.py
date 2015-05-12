# -*- coding=utf-8 -*-
__author__ = 'uleob'

import pyqtgraph as pg
import cv2
import sys
import array
import PyQt4
from PyQt4 import QtGui, QtCore
from sec_detect_ui import Ui_MainWindow

from empty_ui import Ui_emptyTab

possibleFilters = {
    '1':{'text': 'Threshold',               'index': 1,     'module_name': 'thresh',     'class': 'Thresh_tab'},
    '2':{'text': 'Image Smoothing',         'index': 2,     'module_name': 'smooth',     'class': 'Smooth_tab'},
    '3':{'text': 'Gaussian Filter',         'index': 3,     'module_name': 'gauss',      'class': 'Gauss_tab'},
    '4':{'text': 'Median Filter',           'index': 4,     'module_name': 'median',     'class': 'Median_tab'},
    '5':{'text': 'Bilateral Filter',        'index': 5,     'module_name': 'bilateral',  'class': 'Bilateral_tab'},
    '6':{'text': 'Erosion',                 'index': 6,     'module_name': 'erosion',    'class': 'Erosion_tab'},
    '7':{'text': 'Dilation',                'index': 7,     'module_name': 'dilation',   'class': 'Dilation_tab'},
    '8':{'text': 'Morphological Gradient',  'index': 8,     'module_name': 'morph',      'class': 'Morph_tab'},
    '9':{'text': 'Sobel Operator',          'index': 9,     'module_name': 'sobel',      'class': 'Sobel_tab'},
    '10':{'text': 'Laplace Derivate',       'index': 10,    'module_name': 'laplace',    'class': 'Laplace_tab'},
    '11':{'text': 'Canny Edge Detection',   'index': 11,    'module_name': 'canny',      'class': 'Canny_tab'}
}

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    update = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        self.filename = None
        self.image = None
        self.grey_img = None
        self.img_item = pg.ImageItem()
        self.label.addItem(self.img_item)

        self.tabContextMenu = QtGui.QMenu()

        self.connect(self.actionOpen, QtCore.SIGNAL('triggered()'), self.openFile)
        self.connect(self.scale, QtCore.SIGNAL('valueChanged(double)'), self.updateImage)
        self.connect(self.cb_grey, QtCore.SIGNAL('stateChanged(int)'), self.updateImage)
        # self.connect(self.tabWidget, QtCore.SIGNAL('currentChanged(int)'), self.setTab)
        self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested(int)'), self.closeTab)

        self.initTabs()

    def openFile(self):
        fileopen = QtGui.QFileDialog()
        filename = fileopen.getOpenFileName(fileopen, u'Datei öffnen', '', 'Bild-Dateien (*.png *.jpg *.bmp)')
        self.filename = str(filename)
        try:
            self.image = cv2.imread(self.filename)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.image = self.image[:, :, :3]
            self.image = self.image.transpose((1, 0, 2))
            # self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.grey_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.img_item.setImage(self.image)
            """
            scaledWidth = self.scale.value() * self.image.shape[0]
            scaledHeight = self.scale.value() *  self.image.shape[1]
            self.img_item.setRect(QtCore.QRect(0, 0, scaledWidth, scaledHeight))
            self.label.setFixedSize(scaledWidth, scaledHeight)

            if not self.updateImageThread.isRunning():
                self.ImageThreadRunning = True
                self.updateImageThread.run()
            """
            self.updateImage()
        except Exception, e:
            print(e)
            print("No file selected?")

    def updateImage(self):
        # if self.image != None:
        scaledWidth = self.scale.value() * self.image.shape[0]
        scaledHeight = self.scale.value() * self.image.shape[1]
        self.img_item.setRect(QtCore.QRect(0, 0, scaledWidth, scaledHeight))
        self.label.setFixedSize(scaledWidth, scaledHeight)

        if self.cb_grey.isChecked():
            self.img_item.setImage(self.grey_img)
        else:
            self.img_item.setImage(self.image)

    def addTab(self, index):
        if self.tabWidget.tabText(index) == '+':
            items = QtCore.QStringList()
            for i in possibleFilters:
                items.append(possibleFilters[str(i)]['text'])
            item, ok = QtGui.QInputDialog.getItem(QtGui.QComboBox(), 'New Filter', 'Select a Filter', items, editable=False)
            if ok:
                ### first remove the "+"-tab
                self.tabWidget.removeTab(self.tabWidget.count() - 1)
                ### then add the new Tab of the chosen Filter-Type
                i = 0
                for j in possibleFilters:
                    if possibleFilters[str(j)]['text'] == item:
                        module = __import__(possibleFilters[str(j)]['module_name'])
                        tab_class = getattr(module, possibleFilters[str(j)]['class'])
                        new_tab = tab_class()
                        self.connect(new_tab, QtCore.SIGNAL('valueUpdated(int)'), self.updateImage)
                        i = j
                # thresh_tab = Thresh_tab()
                self.tabWidget.addTab(new_tab, possibleFilters[str(i)]['text'])
                ### then add the "+"-tab again
                empty_tab = Empty_tab()
                self.tabWidget.addTab(empty_tab, "+")
                ### set active Tab to new Filter
                self.tabWidget.setCurrentIndex(self.tabWidget.count() - 2)
        else:
            self.tabWidget.setCurrentIndex(index)

    def setTab(self, index):
        #if index == self.tabWidget.count() - 1:
        if self.tabWidget.tabText(index) == '+':
            self.addTab()

    def closeTab(self, index):
        count = self.tabWidget.count()
        if (index != count - 1) & (index != 0):
            # the last tab should not be closed, it's the "+"-Tab
            self.tabWidget.removeTab(index)
            # self.tabWidget.setCurrentIndex(index - 1)


    def initTabs(self):
        self.tabWidget.tabBar().installEventFilter(self)

        self.tabContextMenu.addAction(QtGui.QIcon.fromTheme("edit-delete", QtGui.QIcon("ressources/delete.png")),
                                      "remove Filter", lambda: self.closeTab(self.tabWidget.currentIndex()))

        # self.previousTabIndex = -1
        # self.tabBar.tabButton(self.tabWidget.count() - 1).hide()
        # tab3 = Tab3()
        # self.tabWidget.addTab(tab3, 'Tab 3')

    def eventFilter(self, object, event):
        if object == self.tabWidget.tabBar() and event.type() in \
            [QtCore.QEvent.MouseButtonPress, QtCore.QEvent.MouseButtonRelease] and \
            event.button() == QtCore.Qt.RightButton:
            index = object.tabAt(event.pos())
            object.setCurrentIndex(index)
            self.onTabRightClick(object.tabAt(event.pos()))
            """
            tabIndex = object.tabAt(event.pos())
            if event.type == QtCore.QEvent.MouseButtonPress:
                self.previousTabIndex = tabIndex
            else:
                if tabIndex != -1 and tabIndex == self.previousTabIndex:
                    self.onTabRightClick(tabIndex)
                self.previousTabIndex = -1
            """
            return True
        elif object == self.tabWidget.tabBar() and event.type() in \
            [QtCore.QEvent.MouseButtonPress, QtCore.QEvent.MouseButtonRelease] and \
            event.button() == QtCore.Qt.LeftButton:
            self.addTab(object.tabAt(event.pos()))
            return True
        return False

    def onTabRightClick(self, index):
        count = self.tabWidget.count()
        if (index != count-1) & (index != 0):
            self.tabContextMenu.exec_(QtGui.QCursor.pos())

class Empty_tab(QtGui.QWidget, Ui_emptyTab):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
