# -*- coding=utf-8 -*-
__author__ = 'uleob'

import pyqtgraph as pg
import numpy as np
import cv2
import sys
# import inspect
from PyQt4 import QtGui, QtCore
from sec_detect_ui import Ui_MainWindow
from parameters import possibleFilters
from parameters import possibleDetectors
from process import Image
from filter_widget import GenerateWidget

# from empty_ui import Ui_emptyTab

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        self.imageProcess = Image()

        self.loaded_classes = []    # for all loaded widgets
        self.object_index = []      # for the order of filters
        self.applied_filters = []
        self.clickedListItem = 0

        self.roi = pg.RectROI([100, 100], [100, 100], pen=(0, 9))

        self.filename = None
        self.image = None
        self.grey_img = None
        self.initial_image = None
        self.roi_image = None
        self.img_item = pg.ImageItem()
        self.init_image_item = pg.ImageItem()
        self.label.addItem(self.img_item)
        self.label_3.addItem(self.init_image_item)

        # self.tabContextMenu = QtGui.QMenu()

        self.connect(self.actionOpen, QtCore.SIGNAL('triggered()'), self.openFile)
        # self.connect(self.scale, QtCore.SIGNAL('valueChanged(double)'), self.updateImage)
        self.connect(self.cb_grey, QtCore.SIGNAL('stateChanged(int)'), self.updateImage)
        self.connect(self.btn_apply, QtCore.SIGNAL('clicked()'), self.updateImage)
        # self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested(int)'), self.closeTab)
        self.connect(self.btn_add, QtCore.SIGNAL('clicked()'), self.addFilter)
        self.connect(self.cb_roi, QtCore.SIGNAL('stateChanged(int)'), self.roiUpdate)

        self.sortList.itemPressed.connect(self.listClick)
        self.sortList.installEventFilter(self)
        self.sortList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

        """
        widget1 = Canny_tab()
        widget2 = Canny_tab()
        self.filter_area.setWidget(widget1)
        self.detector_area.setWidget(widget2)
        print inspect.getcallargs(cv2.Canny, 1, 2, 3)
        # print inspect.getargspec(cv2.Canny, inspect.isclass(cv2))
        obj = getattr(cv2, 'Canny')
        print obj
        print obj.__name__
        arginfo = inspect.getargspec(obj)
        args = arginfo[0]
        print args

        # print self.openFile.func_code.co_varnames
        """
        # self.initTabs()

    def openFile(self):
        fileopen = QtGui.QFileDialog()
        filename = fileopen.getOpenFileName(fileopen, u'Datei öffnen', '', 'Bild-Dateien (*.png *.jpg *.bmp)')
        self.filename = str(filename)
        try:
            self.image = cv2.imread(self.filename)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.image = self.image[:, :, :3]
            self.image = self.image.transpose((1, 0, 2))
            self.initial_image = self.image
            # self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.grey_img = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
            self.img_item.setImage(self.image)
            self.init_image_item.setImage(self.initial_image)
        except Exception, e:
            print(e)
            print("No file selected?")

        self.updateImage()

    def updateImage(self):
        # if self.image != None:

        self.image = self.initial_image
        self.grey_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        scaledWidth = self.scale.value() * self.image.shape[0]
        scaledHeight = self.scale.value() * self.image.shape[1]
        self.img_item.setRect(QtCore.QRect(0, 0, scaledWidth, scaledHeight))
        self.init_image_item.setRect(QtCore.QRect(0, 0, scaledWidth, scaledHeight))
        self.label.setFixedSize(scaledWidth, scaledHeight)
        self.label_3.setFixedSize(scaledWidth, scaledHeight)

        ###
        if self.cb_grey.isChecked() == True:
            self.imageProcess.update(self.grey_img, self.object_index, self.applied_filters, self.loaded_classes)
        else:
            self.imageProcess.update(self.image, self.object_index, self.applied_filters, self.loaded_classes)
        ###


        length = self.object_index.__len__()
        for i in xrange(length):     #contains order of filters to be applied
            object_no = -1
            try:
                object_no = self.applied_filters[self.object_index[i]] #see constant list possible_filters
            except Exception, e:
                ### current filter was removed, continue with next
                ### should not occur; all lists are cleared properly
                continue
            index = self.applied_filters.index(object_no)

            if object_no == '0':  #threshold
                # set image to greyscale if not already applied
                self.cb_grey.setChecked(True)

                thresh_type = self.loaded_classes[index].thresh_type()
                value = self.loaded_classes[index].value()
                max_value = self.loaded_classes[index].max_value()
                if thresh_type == 0: #binary
                    ret, thresh = cv2.threshold(self.grey_img, value, max_value, cv2.THRESH_BINARY)
                elif thresh_type == 1: #binary inverted
                    ret, thresh = cv2.threshold(self.grey_img, value, max_value, cv2.THRESH_BINARY_INV)
                elif thresh_type == 2: #adaptive mean
                    thresh = cv2.adaptiveThreshold(self.grey_img, max_value, cv2.ADAPTIVE_THRESH_MEAN_C,
                                                        cv2.THRESH_BINARY, 11, 2)
                elif thresh_type == 3: #adaptive gaussian
                    thresh = cv2.adaptiveThreshold(self.grey_img, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                        cv2.THRESH_BINARY, 11, 2)
                elif thresh_type == 4: #otsu
                    ret, thresh = cv2.threshold(self.grey_img, 0, max_value, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

                self.grey_img = thresh

            elif object_no == '1': #smoothing
                size = self.loaded_classes[index].value()
                self.grey_img = cv2.blur(self.grey_img, (size, size))
                self.image = cv2.blur(self.image, (size, size))

            elif object_no == '2': #gauss
                size = self.loaded_classes[index].value()
                sigmaX = self.loaded_classes[index].valueX()
                sigmaY = self.loaded_classes[index].valueY()
                if sigmaY == 0:
                    sigmaY = sigmaX
                self.grey_img = cv2.GaussianBlur(self.grey_img, (size, size), sigmaX=sigmaX, sigmaY=sigmaY)
                self.image = cv2.GaussianBlur(self.image, (size, size), sigmaX=sigmaX, sigmaY=sigmaY)

            elif object_no == '3': #median
                size = self.loaded_classes[index].value()
                self.grey_img = cv2.medianBlur(self.grey_img, size)
                self.image = cv2.medianBlur(self.image, size)

            elif object_no == '4': #bilateral
                size = self.loaded_classes[index].value()
                sigmaSpace = self.loaded_classes[index].valueSpace()
                sigmaColor = self.loaded_classes[index].valueColor()
                self.grey_img = cv2.bilateralFilter(self.grey_img, size, sigmaColor, sigmaSpace)
                self.image = cv2.bilateralFilter(self.image, size, sigmaColor, sigmaSpace)

            elif object_no == '5': #opening
                size = self.loaded_classes[index].value()
                iterations = self.loaded_classes[index].valueIterations()
                kernel = np.ones((size, size), np.uint8)
                self.grey_img = cv2.morphologyEx(self.grey_img, cv2.MORPH_OPEN, kernel, iterations=iterations)
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel, iterations=iterations)

            elif object_no == '6': #closing
                size = self.loaded_classes[index].value()
                iterations = self.loaded_classes[index].valueIterations()
                kernel = np.ones((size, size), np.uint8)
                self.grey_img = cv2.morphologyEx(self.grey_img, cv2.MORPH_CLOSE, kernel, iterations=iterations)
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel, iterations=iterations)

            elif object_no == '7': #morph gradient
                size = self.loaded_classes[index].value()
                iterations = self.loaded_classes[index].valueIterations()
                kernel = np.ones((size, size), np.uint8)
                self.grey_img = cv2.morphologyEx(self.grey_img, cv2.MORPH_GRADIENT, kernel, iterations=iterations)
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_GRADIENT, kernel, iterations=iterations)

            elif object_no == '8': #sobel
                size = self.loaded_classes[index].value()
                d = self.loaded_classes[index].valueDepth()
                depth = cv2.CV_64F
                if d == 0: #16
                    depth = cv2.CV_16S
                elif d == 1: #32
                    depth = cv2.CV_32F
                elif d == 2: #64
                    depth = cv2.CV_64F
                # dX = 0
                # dY = 0
                if self.loaded_classes[index].valueDX():
                    # dX = 1
                    greyX = cv2.Sobel(self.grey_img, depth, 1, 0, ksize=size)
                    imgX = cv2.Sobel(self.image, depth, 1, 0, ksize=size)
                    self.grey_img = greyX
                    self.image = imgX
                if self.loaded_classes[index].valueDY():
                    # dY = 1
                    greyY = cv2.Sobel(self.grey_img, depth, 0, 1, ksize=size)
                    imgY = cv2.Sobel(self.image, depth, 0, 1, ksize=size)
                    self.grey_img = greyY
                    self.image = imgY
                # self.grey_img = cv2.Sobel(self.grey_img, depth, dX, dY, ksize=size)
                if self.loaded_classes[index].valueDX() & self.loaded_classes[index].valueDY():
                    self.grey_img = cv2.add(greyX, greyY)
                    self.image = cv2.add(imgX, imgY)
                    # self.grey_img = greyX + greyY
                    # self.image = imgX + imgY

            elif object_no == '9': #laplace
                size = self.loaded_classes[index].value()
                d = self.loaded_classes[index].valueDepth()
                depth = cv2.CV_64F
                if d == 0: #16
                    depth = cv2.CV_16S
                elif d == 1: #32
                    depth = cv2.CV_32F
                elif d == 2: #64
                    depth = cv2.CV_64F
                self.image = cv2.Laplacian(self.image, depth, ksize=size)

            elif object_no == '10': #canny
                size = self.loaded_classes[index].value()
                if self.loaded_classes[index].auto_thresh.isChecked():
                    val, thr_otsu = cv2.threshold(self.grey_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                    self.grey_img = cv2.Canny(self.grey_img, val*0.5, val, apertureSize=size)
                    self.image = cv2.Canny(self.image, val*0.5, val, apertureSize=size)
                    self.loaded_classes[index].low_thresh.setProperty("value", val*0.5)
                    self.loaded_classes[index].high_thresh.setProperty("value", val)

                else:
                    low_thr = self.loaded_classes[index].valueLow()
                    high_thr = self.loaded_classes[index].valueHigh()
                    self.grey_img = cv2.Canny(self.grey_img, low_thr, high_thr, apertureSize=size)
                    self.image = cv2.Canny(self.image, low_thr, high_thr, apertureSize=size)

        self.rectDetect()

        if self.cb_grey.isChecked():
            self.img_item.setImage(self.grey_img)
        else:
            self.img_item.setImage(self.image)

    def addFilter(self):
        items = QtCore.QStringList()
        for i in possibleFilters:
            items.append(possibleFilters[str(i)]['text'])
        item, ok = QtGui.QInputDialog.getItem(QtGui.QComboBox(), 'New Filter', 'Select a Filter', items, editable=False)
        if ok:
            i = 0
            for j in possibleFilters:
                if possibleFilters[str(j)]['text'] == item:
                    # module = __import__(possibleFilters[str(j)]['module_name'])
                    # tab_class = getattr(module, possibleFilters[str(j)]['class'])
                    new_filter = GenerateWidget(str(j))
                    self.loaded_classes.append(new_filter)
                    self.object_index.append(self.object_index.__len__())
                    self.applied_filters.append(j)
                    self.connect(self.loaded_classes[self.loaded_classes.__len__() - 1], QtCore.SIGNAL('valueUpdated()'), self.updateImage)
                    i = j
                    self.filter_area.setWidget(self.loaded_classes[self.loaded_classes.__len__() - 1])
        self.setList()

    """
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
                        self.loaded_classes.append(new_tab)
                        self.object_index.append(self.object_index.__len__())
                        self.applied_filters.append(j)
                        self.connect(new_tab, QtCore.SIGNAL('valueUpdated()'), self.updateImage)
                        i = j
                self.tabWidget.addTab(new_tab, possibleFilters[str(i)]['text'])
                ### then add the "+"-tab again
                empty_tab = Empty_tab()
                self.tabWidget.addTab(empty_tab, "+")
                ### set active Tab to new Filter
                self.tabWidget.setCurrentIndex(self.tabWidget.count() - 2)
        else:
            self.tabWidget.setCurrentIndex(index)

        self.setList()

    def setTab(self, index):
        if self.tabWidget.tabText(index) == '+':
            self.addTab()
            self.updateImage()

    def closeTab(self, index):
        count = self.tabWidget.count()
        if (index != count - 1) & (index != 0):
            # the must tab should not be closed, it's the "+"-Tab
            self.tabWidget.removeTab(index)
            del(self.loaded_classes[index - 1])     # destroy object so filter is not applied anymore
            del(self.applied_filters[index - 1])    # remove the list item
            self.object_index.remove(index - 1)     # remove item which contains the index

            self.updateImage()
            self.setList()

    def initTabs(self):
        self.tabWidget.tabBar().installEventFilter(self)

        self.tabContextMenu.addAction(QtGui.QIcon.fromTheme("edit-delete", QtGui.QIcon("ressources/delete.png")),
                                      "remove Filter", lambda: self.closeTab(self.tabWidget.currentIndex()))
    """

    def eventFilter(self, object, event):
        """
        if object == self.tabWidget.tabBar() and event.type() in \
            [QtCore.QEvent.MouseButtonPress, QtCore.QEvent.MouseButtonRelease] and \
            event.button() == QtCore.Qt.RightButton:
            index = object.tabAt(event.pos())
            object.setCurrentIndex(index)
            self.onTabRightClick(object.tabAt(event.pos()))
            return True
        elif object == self.tabWidget.tabBar() and event.type() in \
            [QtCore.QEvent.MouseButtonPress, QtCore.QEvent.MouseButtonRelease] and \
            event.button() == QtCore.Qt.LeftButton:
            self.addTab(object.tabAt(event.pos()))
            return True
        """
        if object == self.sortList and event.type() == QtCore.QEvent.ChildRemoved:
            self.listDragDrop()
            return True
        return False

    def onTabRightClick(self, index):
        count = self.tabWidget.count()
        if (index != count-1) & (index != 0):
            self.tabContextMenu.exec_(QtGui.QCursor.pos())

    def setList(self):
        self.sortList.clear()
        listItems = QtCore.QStringList()
        for i in xrange(self.object_index.__len__()):
            # if not (self.object_index[i] + 2) == self.tabWidget.count():
            # text = possibleFilters[]
            # text = self.tabWidget.tabText(self.object_index[i] + 1)
            text = possibleFilters[self.applied_filters[i]]['text']
            listItems.append(text)
        self.sortList.addItems(listItems)

    def listDragDrop(self):
        if self.clickedListItem != self.sortList.currentRow():  # position where item is released
            if self.clickedListItem < self.sortList.currentRow(): # drag-position < drop-position
                # index = self.sortList.currentRow()
                clicked = self.object_index[self.clickedListItem]
                for i in xrange(self.sortList.currentRow() - self.clickedListItem):
                    self.object_index[i] = self.object_index[i + 1]
                self.object_index[self.sortList.currentRow()] = clicked
                # self.object_index[self.clickedListItem] = self.object_index[self.sortList.currentRow()]
            elif self.clickedListItem > self.sortList.currentRow(): # drop-position < drag-position
                # index = self.sortList.currentRow()
                clicked = self.object_index[self.clickedListItem]
                for i in xrange(self.clickedListItem - self.sortList.currentRow()):
                # for i in xrange(self.sortList.currentRow() + 1, self.clickedListItem + 1):
                    self.object_index[self.clickedListItem - i] = self.object_index[self.clickedListItem - i - 1]
                self.object_index[self.sortList.currentRow()] = clicked
        self.updateImage()

    def listClick(self):
        self.clickedListItem = self.sortList.currentRow()

    def roiUpdate(self):
        if self.cb_roi.isChecked():
            if self.roi not in self.label.items():
                self.label.addItem(self.roi)
            if self.cb_grey.isChecked():
                self.roi_image = self.roi.getArrayRegion(self.grey_img, self.label)
            else:
                self.roi_image = self.roi.getArrayRegion(self.image, self.label)
        else:
            if self.roi in self.label.items():
                self.label.removeItem(self.roi)

    def rectDetect(self):
        if self.cb_roi.isChecked():
            image = self.roi_image
        else:
            if self.cb_grey.isChecked():
                image = self.grey_img
            else:
                image = self.image

        image = self.grey_img

        # image should be binary: threshold or canny edge
        if '0' in self.applied_filters or '10' in self.applied_filters:
            bla = None
            minLineLength = 100
            maxLineGap = 30
            lines = cv2.HoughLinesP(image, 1, np.pi/180, 50, minLineLength, maxLineGap)
            bla = np.array(self.initial_image.copy())
            for x1, y1, x2, y2 in lines[0]:
                cv2.line(bla, (x1, y1), (x2, y2), (0, 255, 0), 3)
            """
            lines = cv2.HoughLines(image, 1, np.pi/180, 200)
            for rho, theta in lines[0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))

                cv2.line(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            """
            # cv2.line(bla, (0, 0), (200, 200), (0, 255, 255), 5)
            self.init_image_item.setImage(bla)
            # self.initial_image = bla.copy()
            # cv2.imshow("Probabilistic Hough Transform", bla)
            # cv2.waitKey(0)

        """
        (contours, _) = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)

        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(approx) == 4: # contour has 4 points (edges)
                display_contour = approx
                cv2.drawContours(self.image, display_contour, -1, (0, 255, 0), 3)
                cv2.drawContours(self.grey_img, display_contour, -1, (0, 255, 0), 3)
                # break
        """

"""
class Empty_tab(QtGui.QWidget, Ui_emptyTab):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
"""

def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
