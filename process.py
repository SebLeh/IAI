__author__ = 'uleob'

import cv2
import numpy as np
from PyQt4 import QtGui

class Image():
    def __init__(self):
        self.image = None
        self.grey_img = None

    def update(self, image, grey, object_index, applied_filters, loaded_classes):

        if grey:
            self.grey_img = image
        else:
            self.image = image

        length = object_index.__len__()
        for i in xrange(length):     #contains order of filters to be applied
            object_no = -1
            try:
                object_no = applied_filters[object_index[i]] #see parameters list possibleFilters
            except Exception, e:
                ### current filter was removed, continue with next
                ### should not occur; all lists are cleared properly
                continue
            index = applied_filters.index(object_no)

            if object_no == '0':  #threshold
                # set image to greyscale if not already applied
                # self.cb_grey.setChecked(True)
                if grey:
                # thresh_type = loaded_classes[index].thresh_type()
                    thresh_type = 3
                    value = loaded_classes[index].recent_values['low_thr']
                    max_value = loaded_classes[index].recent_values['high_thr']
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
                else:
                    # show message
                    raise ValueError('Image not greyscale')
                    # message = QtGui.QMessageBox("Image not greyscale", "Threshold can only be applied on greyscale images.")
                    # message.show()
                    # continue

            elif object_no == '1': #smoothing
                size = loaded_classes[index].recent_values['size']
                if grey:
                    self.grey_img = cv2.blur(self.grey_img, (size, size))
                else:
                    self.image = cv2.blur(self.image, (size, size))

            elif object_no == '2': #gauss
                size = loaded_classes[index].recent_values['size']
                sigmaX = loaded_classes[index].recent_values['sigmaX']
                sigmaY = loaded_classes[index].recent_values['SigmaY']
                if sigmaY == 0:
                    sigmaY = sigmaX
                if grey:
                    self.grey_img = cv2.GaussianBlur(self.grey_img, (size, size), sigmaX=sigmaX, sigmaY=sigmaY)
                else:
                    self.image = cv2.GaussianBlur(self.image, (size, size), sigmaX=sigmaX, sigmaY=sigmaY)

            elif object_no == '3': #median
                size = loaded_classes[index].recent_values['size']
                if grey:
                    self.grey_img = cv2.medianBlur(self.grey_img, size)
                else:
                    self.image = cv2.medianBlur(self.image, size)

            elif object_no == '4': #bilateral
                size = loaded_classes[index].recent_values['size']
                sigmaSpace = loaded_classes[index].recent_values['space']
                sigmaColor = loaded_classes[index].recent_values['color']
                if grey:
                    self.grey_img = cv2.bilateralFilter(self.grey_img, size, sigmaColor, sigmaSpace)
                else:
                    self.image = cv2.bilateralFilter(self.image, size, sigmaColor, sigmaSpace)

            elif object_no == '5': #opening
                size = loaded_classes[index].recent_values['size']
                iterations = loaded_classes[index].recent_values['iterations']
                kernel = np.ones((size, size), np.uint8)
                self.grey_img = cv2.morphologyEx(self.grey_img, cv2.MORPH_OPEN, kernel, iterations=iterations)
                self.image = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel, iterations=iterations)

            elif object_no == '6': #closing
                size = loaded_classes[index].recent_values['size']
                iterations = loaded_classes[index].recent_values['iterations']
                kernel = np.ones((size, size), np.uint8)
                if grey:
                    self.grey_img = cv2.morphologyEx(self.grey_img, cv2.MORPH_CLOSE, kernel, iterations=iterations)
                else:
                    self.image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel, iterations=iterations)

            elif object_no == '7': #morph gradient
                size = loaded_classes[index].recent_values['size']
                iterations = loaded_classes[index].recent_values['iterations']
                kernel = np.ones((size, size), np.uint8)
                if grey:
                    self.grey_img = cv2.morphologyEx(self.grey_img, cv2.MORPH_GRADIENT, kernel, iterations=iterations)
                else:
                    self.image = cv2.morphologyEx(self.image, cv2.MORPH_GRADIENT, kernel, iterations=iterations)

            elif object_no == '8': #sobel
                size = loaded_classes[index].recent_values['size']
                dX = loaded_classes[index].recent_values['dX']
                dY = loaded_classes[index].recent_values['dY']

                depth = cv2.CV_64F
                if dX:
                    greyX = cv2.Sobel(self.grey_img, depth, 1, 0, ksize=size)
                    imgX = cv2.Sobel(self.image, depth, 1, 0, ksize=size)
                    if grey:
                        self.grey_img = greyX
                    else:
                        self.image = imgX
                if dY:
                    greyY = cv2.Sobel(self.grey_img, depth, 0, 1, ksize=size)
                    imgY = cv2.Sobel(self.image, depth, 0, 1, ksize=size)
                    if grey:
                        self.grey_img = greyX
                    else:
                        self.image = imgX
                if dX & dY:
                    if grey:
                        self.grey_img = cv2.add(greyX, greyY)
                    else:
                        self.image = cv2.add(imgX, imgY)

            elif object_no == '9': #laplace
                size = loaded_classes[index].recent_values['size']
                depth = cv2.CV_64F
                if grey:
                    self.grey_img = cv2.Laplacian(self.grey_img, depth, ksize=size)
                else:
                    self.image = cv2.Laplacian(self.image, depth, ksize=size)

            elif object_no == '10': #canny
                size = loaded_classes[index].recent_values['size']
                low_thr = loaded_classes[index].recent_values['low_thr']
                high_thr = loaded_classes[index].recent_values['high_thr']
                """
                if loaded_classes[index].auto_thresh.isChecked():
                    val, thr_otsu = cv2.threshold(self.grey_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                    self.grey_img = cv2.Canny(self.grey_img, val*0.5, val, apertureSize=size)
                    self.image = cv2.Canny(self.image, val*0.5, val, apertureSize=size)
                    loaded_classes[index].low_thresh.setProperty("value", val*0.5)
                    loaded_classes[index].high_thresh.setProperty("value", val)

                else:
                """
                if grey:
                    self.grey_img = cv2.Canny(self.grey_img, low_thr, high_thr, apertureSize=size)
                else:
                    self.image = cv2.Canny(self.image, low_thr, high_thr, apertureSize=size)

        if grey:
            return self.grey_img
        else:
            return self.image