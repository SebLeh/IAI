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
from PIL import Image as im
from PIL import ImageOps

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
        self.roi_image = None
        self.roi_offset = {0, 0}

        self.filename = None
        self.image = None
        self.grey_img = None
        self.initial_image = None
        self.img_item = pg.ImageItem()
        self.init_image_item = pg.ImageItem()
        self.label.addItem(self.img_item)
        self.label_3.addItem(self.init_image_item)

        self.contour_widget = GenerateWidget('1', 'detector')

        self.RemoveIcon = im.fromarray(cv2.imread('ressources/delete.png'))
        self.RemoveIcon = QtGui.QIcon(self.RemoveIcon)

        # self.tabContextMenu = QtGui.QMenu()

        self.setup()

        self.connect(self.actionOpen, QtCore.SIGNAL('triggered()'), self.openFile)
        self.connect(self.scale, QtCore.SIGNAL('valueChanged(double)'), self.updateImage)
        self.connect(self.cb_grey, QtCore.SIGNAL('stateChanged(int)'), self.updateImage)
        self.connect(self.cb_inv, QtCore.SIGNAL('stateChanged(int)'), self.updateImage)
        self.connect(self.btn_apply, QtCore.SIGNAL('clicked()'), self.updateImage)
        # self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested(int)'), self.closeTab)
        self.connect(self.btn_add, QtCore.SIGNAL('clicked()'), self.addFilter)
        self.connect(self.cb_roi, QtCore.SIGNAL('stateChanged(int)'), self.roiUpdate)
        self.connect(self.sortList, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem *)'), self.itemDoubleClicked)
        # self.connect(self.sortList, QtCore.SIGNAL('customContextMenuRequested(QPoint *)'), self.itemRightClicked)
        self.connect(self.combbox_detector, QtCore.SIGNAL('currentIndexChanged(int)'), self.setDetector)

        self.sortList.itemPressed.connect(self.listClick)
        self.sortList.installEventFilter(self)
        self.sortList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

    def setup(self):
        items = QtCore.QStringList()
        for i in xrange(possibleDetectors.__len__()):
            items.append(possibleDetectors[str(i)]['text'])
        self.combbox_detector.addItems(items)

        self.combbox_detector.setCurrentIndex(1)

        self.detector_area.setWidget(self.contour_widget)

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

        self.roiUpdate()

        self.image = self.initial_image
        self.grey_img = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

        scaledWidth = self.scale.value() * self.image.shape[0]
        scaledHeight = self.scale.value() * self.image.shape[1]
        self.img_item.setRect(QtCore.QRect(0, 0, scaledWidth, scaledHeight))
        self.init_image_item.setRect(QtCore.QRect(0, 0, scaledWidth, scaledHeight))
        self.label.setFixedSize(scaledWidth, scaledHeight)
        self.label_3.setFixedSize(scaledWidth, scaledHeight)

        if self.cb_inv.isChecked():
            img255 = np.empty_like(self.image)
            img255.fill(255)
            inverted = img255 - self.image
            self.image = inverted
            img255 = np.empty_like(self.grey_img)
            img255.fill(255)
            inverted = img255 - self.grey_img
            self.grey_img = inverted

            """
            inv_image = ImageOps.invert(self.image)
            self.image = inv_image
            inv_image = ImageOps.invert(self.grey_img)
            self.grey_img = inv_image
            """

        if self.cb_grey.isChecked():
            self.grey_img = self.imageProcess.update(self.grey_img, True, self.object_index, self.applied_filters, self.loaded_classes)
        else:
            try:
                self.image = self.imageProcess.update(self.image, False, self.object_index, self.applied_filters, self.loaded_classes)
            except Exception, e:
                msg = QtGui.QMessageBox.warning(self, 'Image not Greyscale', 'Image should be Greayscale for applying Threshold-Filter.')

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
                    new_filter = GenerateWidget(str(j), 'filter')
                    self.loaded_classes.append(new_filter)
                    self.object_index.append(self.object_index.__len__())
                    self.applied_filters.append(j)
                    self.connect(self.loaded_classes[self.loaded_classes.__len__() - 1], QtCore.SIGNAL('valueUpdated()'), self.updateImage)
                    i = j
                    self.filter_area.setWidget(self.loaded_classes[self.loaded_classes.__len__() - 1])
        self.setList()

    def eventFilter(self, object, event):
        if object == self.sortList and event.type() == QtCore.QEvent.ChildRemoved:
            self.listDragDrop()
            return True
        if object == self.sortList and event.type() == QtCore.QEvent.ContextMenu:
            self.itemRightClicked()
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
                    self.object_index[i + self.clickedListItem] = self.object_index[i + self.clickedListItem + 1]
                self.object_index[self.sortList.currentRow()] = clicked
                # self.object_index[self.clickedListItem] = self.object_index[self.sortList.currentRow()]
            elif self.clickedListItem > self.sortList.currentRow(): # drop-position < drag-position
                # index = self.sortList.currentRow()
                clicked = self.object_index[self.clickedListItem]
                for i in xrange(self.clickedListItem - self.sortList.currentRow()):
                # for i in xrange(self.sortList.currentRow() + 1, self.clickedListItem + 1):
                    self.object_index[self.clickedListItem - i] = self.object_index[self.clickedListItem - i - 1]
                self.object_index[self.sortList.currentRow()] = clicked
        # self.updateImage()

    def listClick(self):
        self.clickedListItem = self.sortList.currentRow()

    def roiUpdate(self):
        if self.cb_roi.isChecked():
            if self.roi not in self.label.items():
                self.label.addItem(self.roi)
            if self.cb_grey.isChecked():
                self.roi_image = self.roi.getArrayRegion(self.grey_img, self.img_item)
            else:
                self.roi_image = self.roi.getArrayRegion(self.image, self.img_item)
            self.roi_offset = self.roi.pos()
            self.roi_offset[0] = int(self.roi_offset[0] / self.scale.value())
            self.roi_offset[1] = int(self.roi_offset[1] / self.scale.value())
            # X, Y is switched n this tuple
            x = self.roi_offset[1]
            self.roi_offset[1] = self.roi_offset[0]
            self.roi_offset[0] = x
        else:
            if self.roi in self.label.items():
                self.label.removeItem(self.roi)

    def rectDetect(self):

        if self.cb_roi.isChecked():
            image = self.roi_image
            image = np.asarray(image, dtype=np.uint8)
            # image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            # image.shape = self.roi.size()
        else:
            image = self.grey_img
        # image = cv2.cvtColor(im, cv2.CV_8U)

        # image should be binary: threshold or canny edge
        if '0' in self.applied_filters or '1' in self.applied_filters or '11' in self.applied_filters:
            bla =  np.array(self.initial_image.copy())
            if self.combbox_detector.currentIndex() == 0:
                # find countours
                (contours, _) = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                contours = sorted(contours, key=cv2.contourArea, reverse=True) # sort found contours by size

                if self.cb_roi.isChecked():
                    for c in contours:
                        for i in xrange(c.__len__()):
                            c[i] = c[i] + self.roi_offset


                for c in contours:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

                    i = 0
                    if self.contour_widget.recent_values['rectangles']:
                        if len(approx) == 4: # contour has 4 points (edges)
                            display_contour = approx
                            cv2.drawContours(bla, display_contour, -1, (0, 255, 0), 10)
                            value = self.contour_widget.recent_values['results']
                            if i == value:
                                break
                    else:
                        display_contour = approx
                        cv2.drawContours(bla, display_contour, -1, (0, 255, 0), 10)
                        value = self.contour_widget.recent_values['results']
                        if i == value:
                            break

                            # cv2.drawContours(self.grey_img, display_contour, -1, (0, 255, 0), 3)

            elif self.combbox_detector.currentIndex() == 1:
                # probabilistic Hough Lines

                # if self.contour_widget.recent_values['negative'] == True:
                #     image = ImageOps.invert(image)

                rho = self.contour_widget.recent_values['rho']
                theta = self.contour_widget.recent_values['theta']
                thresh = self.contour_widget.recent_values['thresh']
                minLength = self.contour_widget.recent_values['minLength']
                maxGap = self.contour_widget.recent_values['maxGap']
                lines = cv2.HoughLinesP(image, rho, np.pi/theta, thresh, minLength, maxGap)
                bla = np.array(self.initial_image.copy())
                for x1, y1, x2, y2 in lines[0]:
                    if self.cb_roi.isChecked():
                        cv2.line(bla, (x1 + int(self.roi_offset[0]), y1 + int(self.roi_offset[1])),
                             (x2 + int(self.roi_offset[0]), y2 + int(self.roi_offset[1])), (0, 255, 0), 3)
                    else:
                        cv2.line(bla, (x1, y1), (x2, y2), (0, 255, 0), 3)

            elif self.combbox_detector.currentIndex() == 2:
                # Hough Lines

                rho = self.contour_widget.recent_values['rho']
                theta = self.contour_widget.recent_values['theta']
                thresh = self.contour_widget.recent_values['thresh']

                lines = cv2.HoughLines(image, rho, np.pi/theta, thresh)
                for rho, theta in lines[0]:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))

                    if self.cb_roi.isChecked():
                        cv2.line(bla, (x1 + int(self.roi_offset[0]), y1 + int(self.roi_offset[1])),
                             (x2 + int(self.roi_offset[0]), y2 + int(self.roi_offset[1])), (0, 255, 0), 3)
                    else:
                        cv2.line(bla, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # cv2.line(bla, (0, 0), (200, 200), (0, 255, 255), 5)
            self.init_image_item.setImage(bla)
            # self.initial_image = bla.copy()
            # cv2.imshow("Probabilistic Hough Transform", bla)
            # cv2.waitKey(0)
        else:
            self.init_image_item.setImage(self.initial_image)
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
    def itemDoubleClicked(self):
        index = self.object_index[self.sortList.currentRow()]
        obj_no = self.applied_filters[index]
        tempWidget = GenerateWidget(obj_no, 'filter')
        tempWidget.recent_values = self.loaded_classes[index].recent_values
        tempWidget.set()

        self.filter_area.setWidget(tempWidget)
        self.loaded_classes[self.object_index[index]] = tempWidget

    def itemRightClicked(self):
        itemIndex = self.sortList.currentRow()
        self.itemMenu = QtGui.QMenu(self)
        delAction = self.itemMenu.addAction(self.RemoveIcon, "Remove")

        action = self.itemMenu.exec_(QtGui.QCursor.pos())
        if action == delAction:
            self.removeItem(itemIndex)
        pass

    def setDetector(self):
        index = self.combbox_detector.currentIndex()
        self.contour_widget = GenerateWidget(str(index), 'detector')

        self.detector_area.setWidget(self.contour_widget)
        # pass

    def removeItem(self, index):
        # need to find correct index for operation, depending on possible rearranging of Items
        i = self.object_index[index]
        if self.loaded_classes[i] == self.filter_area.widget():
            self.filter_area.setWidget(QtGui.QWidget())
        del(self.loaded_classes[i])     # destroy object so filter is not applied anymore
        del(self.applied_filters[i])    # remove the list item
        self.object_index.remove(i)     # remove item which contains the index
        self.sortList.takeItem(index)

def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
