# -*- coding=utf-8 -*-
__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from parameters import filter_parameters, detector_parameters


class GenerateWidget(QtGui.QWidget):
    def __init__(self, num, kind, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.grid = QtGui.QGridLayout(self)
        self.recent_values = {}
        self.num = str(num)
        self.kind = kind
        self.params = {}
        self.setup()

    def update(self):
        for i in xrange(self.params.__len__()):
            try:
                self.recent_values[str(self.params[str(i)].accessibleName())] = self.params[str(i)].value()
            except Exception, e:
                # checkbox has no "value" that can be read
                try:
                    self.recent_values[str(self.params[str(i)].accessibleName())] = self.params[str(i)].isChecked()
                except Exception, e:
                    self.recent_values[str(self.params[str(i)].accessibleName())] = self.params[str(i)].currentIndex()


    def set(self):
        for i in xrange(self.params.__len__()):
            try:
                self.params[str(i)].setValue(self.recent_values[str(self.params[str(i)].accessibleName())])
            except Exception, e:
                # checkbox has no "value" that can be set
                try:
                    self.params[str(i)].setChecked(self.recent_values[str(self.params[str(i)].accessibleName())])
                except Exception, e:
                    self.params[str(i)].setCurrentIndex(self.recent_values[str(self.params[str(i)].accessibleName())])

    def setup(self):
        """
        label = QtGui.QLabel()
        label.setText(filter_parameters[self.num]['name'])
        self.grid.addWidget(label, 1, 0, 1, 1)
        """
        parameters = {}
        if self.kind == 'filter':
            parameters = filter_parameters
        elif self.kind == 'detector':
            parameters = detector_parameters

        for i in xrange(parameters[self.num]['params'].__len__()):

            if parameters[self.num]['params'][str(i)]['display'] == 'NONE':
                continue
            if not parameters[self.num]['params'][str(i)]['type'] == 'bool':
                param_lbl = QtGui.QLabel(parameters[self.num]['params'][str(i)]['display'])
                self.grid.addWidget(param_lbl, i+1, 0)

            param = None
            if parameters[self.num]['params'][str(i)]['type'] == 'int':
                param = QtGui.QSpinBox()
                param.setAccessibleName(parameters[self.num]['params'][str(i)]['name'])
                try:
                    param.setSingleStep(parameters[self.num]['params'][str(i)]['step'])
                except Exception, e:
                    pass
            elif parameters[self.num]['params'][str(i)]['type'] == 'double':
                param = QtGui.QDoubleSpinBox()
                param.setAccessibleName(parameters[self.num]['params'][str(i)]['name'])
            elif parameters[self.num]['params'][str(i)]['type'] == 'bool':
                param = QtGui.QCheckBox()
                param.setText(parameters[self.num]['params'][str(i)]['display'])
                param.setChecked(parameters[self.num]['params'][str(i)]['value'])
                param.setAccessibleName(parameters[self.num]['params'][str(i)]['name'])
            elif parameters[self.num]['params'][str(i)]['type'] == 'drop-down':
                param = QtGui.QComboBox()
                param.setAccessibleName(parameters[self.num]['params'][str(i)]['name'])
                for j in xrange(parameters[self.num]['params'][str(i)]['values'].__len__()):
                    param.addItem(parameters[self.num]['params'][str(i)]['values'][j])
            try:
                param.setMinimum(parameters[self.num]['params'][str(i)]['min'])
            except Exception, e:
                pass
            try:
                param.setMaximum(parameters[self.num]['params'][str(i)]['max'])
            except Exception, e:
                pass
            try:
                param.setValue(parameters[self.num]['params'][str(i)]['value'])
            except Exception, e:
                pass
            try:
                self.recent_values[parameters[self.num]['params'][str(i)]['name']] = param.value()
                param.valueChanged.connect(self.update)
            except Exception, e:
                # checkbox has no "value"
                try:
                    self.recent_values[parameters[self.num]['params'][str(i)]['name']] = param.isChecked()
                    param.stateChanged.connect(self.update)
                except Exception, e:
                    self.recent_values[parameters[self.num]['params'][str(i)]['name']] = param.currentIndex()
                    param.currentIndexChanged.connect(self.update)
            self.params[str(i)] = param
            self.grid.addWidget(param, i+1, 1)

            # param.valueChanged.connect(self.update)
