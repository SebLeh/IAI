# -*- coding=utf-8 -*-
__author__ = 'uleob'

import pyqtgraph as pg
import cv2
import sys
import array
import PyQt4
from PyQt4 import QtGui, QtCore
from sec_detect_ui import Ui_MainWindow

# from thresh_ui import Ui_thresh_tab
from empty_ui import Ui_emptyTab

possibleFilters = {
    '1':{'text': 'Threshold',               'index': 1,     'module_name': 'thresh',        'class': 'Thresh_tab'},
    '2':{'text': 'Image Smoothing',         'index': 2,     'module_name': 'smooth_ui',     'class': 'Ui_smooth_tab'},
    '3':{'text': 'Gaussian Filter',         'index': 3,     'module_name': 'gauss_ui',      'class': 'Ui_gauss_tab'},
    '4':{'text': 'Median Filter',           'index': 4,     'module_name': 'median_ui',     'class': 'Ui_median_tab'},
    '5':{'text': 'Bilateral Filter',        'index': 5,     'module_name': 'bilateral_ui',  'class': 'Ui_bilateral_tab'},
    '6':{'text': 'Erosion',                 'index': 6,     'module_name': 'erosion_ui',    'class': 'Ui_erosion_tab'},
    '7':{'text': 'Dilation',                'index': 7,     'module_name': 'dilation_ui',   'class': 'Ui_dilation_tab'},
    '8':{'text': 'Morphological Gradient',  'index': 8,     'module_name': 'morph_ui',      'class': 'Ui_morph_tab'},
    '9':{'text': 'Sobel Operator',          'index': 9,     'module_name': 'sobel_ui',      'class': 'Ui_sobel_tab'},
    '10':{'text': 'Laplace Derivate',       'index': 10,    'module_name': 'laplace_ui',    'class': 'Ui_laplace_tab'},
    '11':{'text': 'Canny Edge Detection',   'index': 11,    'module_name': 'canny_ui',      'class': 'Ui_canny_tab'}
}

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        self.filename = None
        self.image = None
        self.grey_img = None
        self.img_item = pg.ImageItem()
        self.label.addItem(self.img_item)

        self.tabContextMenu = QtGui.QMenu()

        # self.updateImageThread = ImageThread(self)
        # self.ImageThreadRunning = True

        self.connect(self.actionOpen, QtCore.SIGNAL('triggered()'), self.openFile)
        self.connect(self.scale, QtCore.SIGNAL('valueChanged(double)'), self.updateImage)
        self.connect(self.cb_grey, QtCore.SIGNAL('stateChanged(int)'), self.updateImage)
        self.connect(self.tabWidget, QtCore.SIGNAL('currentChanged(int)'), self.setTab)
        self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested(int)'), self.closeTab)
        # self.connect(self.updateImageThread, QtCore.SIGNAL('update()'), self.updateImage)
        # self.updateImageThread.update.connect(self.updateImage)

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

    def addTab(self):
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
                    i = j
            # thresh_tab = Thresh_tab()
            self.tabWidget.addTab(new_tab, possibleFilters[str(i)]['text'])
            ### then add the "+"-tab again
            empty_tab = Empty_tab()
            self.tabWidget.addTab(empty_tab, "+")
            ### set active Tab
            self.tabWidget.setCurrentIndex(self.tabWidget.count() - 2)

    def setTab(self, index):
        #if index == self.tabWidget.count() - 1:
        if self.tabWidget.tabText(index) == '+':
            self.addTab()

    def closeTab(self, index):
        if index != self.tabWidget.count() - 1 & index != 1:
            # the last tab should not be closed, it's the "+"-Tab
            self.tabWidget.removeTab(index)


    def initTabs(self):
        self.tabWidget.tabBar().installEventFilter(self)

        self.tabContextMenu.addAction(QtGui.QIcon.fromTheme("edit-delete", QtGui.QIcon("ressources/delete.png")), "remove Filter")
        # self.previousTabIndex = -1
        # self.tabBar.tabButton(self.tabWidget.count() - 1).hide()
        # tab3 = Tab3()
        # self.tabWidget.addTab(tab3, 'Tab 3')

    def eventFilter(self, object, event):
        if object == self.tabWidget.tabBar() and event.type() in \
            [QtCore.QEvent.MouseButtonPress, QtCore.QEvent.MouseButtonRelease] and \
            event.button() == QtCore.Qt.RightButton:
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
        return False

    def onTabRightClick(self, index):
        if index != self.tabWidget.count()-1:
            self.tabContextMenu.exec_(QtGui.QCursor.pos())

class Empty_tab(QtGui.QWidget, Ui_emptyTab):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

"""
class Thresh_tab(QtGui.QWidget, Ui_thresh_tab):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.setup()

    def setup(self):
        itemList = QtCore.QStringList()
        itemList.append("Binary Threshold")
        itemList.append("Binary Threshold, inverted")
        itemList.append("Adaptive Threshold, mean")
        itemList.append("Adaptive Threshold, Gaussian")
        itemList.append("Otsu Threshold")
        self.comb_thresh.addItems(itemList)
"""
"""
class ImageThread(QtCore.QThread):
    update = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.parent = parent

    def run(self):
        self.update.emit()
        # QtCore.QThread.run(self)
        # self.emit(QtCore.SIGNAL('update()'))
        parent = self.parent
        while parent.ImageThreadRunning:
            self.emit(QtCore.SIGNAL('update()'))
        self.quit()
        try:
            self.emit(QtCore.SIGNAL('update()'))
        except Exception, e:
            print('=> ERROR from ImageThread:' + str(e))


    def __del__(self):
        print('ImageThread deleted')
        self.terminate()
"""

def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
