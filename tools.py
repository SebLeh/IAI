# -*- coding=utf-8 -*-
__author__ = 'uleob'

import cv2
import cPickle as pickle
import os
from PyQt4 import QtGui
from filter_widget import GenerateWidget

absDirPath = os.path.dirname(__file__)

class Tools():

    def __init__(self):
        self.classes = []
        self.obj = []
        self.filters = []
        self.properties = {}
        self.contour_widget = None

    def openFile(self):
        fileopen = QtGui.QFileDialog()
        filename = fileopen.getOpenFileName(fileopen, u'Open File', '', 'Image-files (*.png *.jpg *.bmp)')
        str_filename = str(filename)
        try:
            image = cv2.imread(str_filename)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = image[:, :, :3]
            image = image.transpose((1, 0, 2))
            return image
        except Exception, e:
            print(e)
            print("No file selected?")

    def loadSettings(self, default=False):
        if default:
            str_filename = absDirPath + '/settings/default/default.pobj'
        else:
            dialog = QtGui.QFileDialog()
            filename = dialog.getOpenFileName(dialog, u'Load Settings', absDirPath + '/settings', 'Python Object Files (*.pobj)')
            str_filename = str(filename)
        file = open(str_filename, 'r')
        data = pickle.load(file)
        classes = data.get("classes", [])
        for i in xrange(classes.__len__()):
            try:
                item = classes.popitem()
            except Exception, e:
                pass
            new_filter = GenerateWidget(item[0], 'filter')
            new_filter.recent_values = item[1]
            new_filter.set()
            self.classes.append(new_filter)
        self.obj = data.get("obj", [])
        self.filters = data.get("filters", [])
        self.classes.reverse()
        self.properties = data.get("prop", [])

        contour = data.get("contour", [])
        self.contour_widget = GenerateWidget(contour["type"], 'detector')
        self.contour_widget.recent_values = contour["params"]
        self.contour_widget.set()

        pass

    def saveSettings(self, properties, loaded_classes, object_index, applied_filters, contour_widget, contour_type):
        # pickle can't handle PyQt-Widget objects, therefore objects need to be 'parsed'
        classes = {}
        contour = {}
        for i in xrange(loaded_classes.__len__()):
            classes[loaded_classes[i].num] = loaded_classes[i].recent_values
        contour["type"] = contour_type
        contour["params"] = contour_widget.recent_values
        data = dict(prop=properties, classes=classes, obj=object_index, filters=applied_filters, contour=contour)
        dialog = QtGui.QFileDialog()
        filename = dialog.getSaveFileName(dialog, u'Save Settings to file', absDirPath + '/settings', 'Python Object Files (*.pobj)')
        str_filename = str(filename)
        file = open(str_filename, 'w')
        pickle.dump(data, file)
        pass

