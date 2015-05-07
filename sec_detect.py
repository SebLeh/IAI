# -*- coding=utf-8 -*-
__author__ = 'uleob'

import pyqtgraph as pg
import cv2
import sys
import array
import PyQt4
from PyQt4 import QtGui, QtCore
from sec_detect_ui import Ui_MainWindow
from tab3_ui import Ui_Form

possibleFilters = {
    '1':{'text': 'Threshold', 'index': 1, 'used': False},
    '2':{'text': 'Image Smoothing', 'index': 2, 'used': False},
    '3':{'text': 'Gaussian Filter', 'index': 3, 'used': False},
    '4':{'text': 'Median Filter', 'index': 4, 'used': False},
    '5':{'text': 'Bilateral Filter', 'index': 5, 'used': False},
    '6':{'text': 'Erosion', 'index': 6, 'used': False},
    '7':{'text': 'Dilation', 'index': 7, 'used': False},
    '8':{'text': 'Morphological Gradient', 'index': 8, 'used': False},
    '9':{'text': 'Sobel Operator', 'index': 9, 'used': False},
    '10':{'text': 'Laplace Derivate', 'index': 10, 'used': False},
    '11':{'text': 'Canny Edge Detection', 'index': 11, 'used': False}
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

        # self.updateImageThread = ImageThread(self)
        # self.ImageThreadRunning = True

        self.connect(self.actionOpen, QtCore.SIGNAL('triggered()'), self.openFile)
        self.connect(self.scale, QtCore.SIGNAL('valueChanged(double)'), self.updateImage)
        self.connect(self.cb_grey, QtCore.SIGNAL('stateChanged(int)'), self.updateImage)
        self.connect(self.tabWidget, QtCore.SIGNAL('currentChanged(int)'), self.setTab)
        # self.connect(self.updateImageThread, QtCore.SIGNAL('update()'), self.updateImage)
        # self.updateImageThread.update.connect(self.updateImage)

        # self.initTabs()

    def openFile(self):
        fileopen = QtGui.QFileDialog()
        filename = fileopen.getOpenFileName(fileopen, u'Datei öffnen', '', 'Bild-Dateien (*.png *.jpg *.bmp)')
        self.filename = str(filename)
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
        # indices = array('i')
        for i in possibleFilters:
            if not possibleFilters[str(i)]['used']:
                items.append(possibleFilters[str(i)]['text'])
                # indices[i] = int(possibleFilters[str(i)]['index'])
        item, ok = QtGui.QInputDialog.getItem(QtGui.QComboBox(), 'New Filter', 'Select a Filter', items)
        tab4 = Tab3()

    def setTab(self, index):
        if index == self.tabWidget.count() - 1:
            self.addTab()

    def initTabs(self):
        tab3 = Tab3()
        self.tabWidget.addTab(tab3, 'Tab 3')

class Tab3(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

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
    # if mainWindow.image != None:
    #     mainWindow.updateImage()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
