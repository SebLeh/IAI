# -*- coding=utf-8 -*-
__author__ = 'uleob'

from PyQt4 import QtGui, QtCore
from parameters import filter_parameters


class GenerateWidget(QtGui.QWidget):
    def __init__(self, num, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.grid = QtGui.QGridLayout(self)
        self.recent_values = {}
        self.num = str(num)
        self.params = {}
        self.setup()

    def update(self):
        for i in xrange(self.params.__len__()):
            self.recent_values[str(self.params[str(i)].accessibleName())] = self.params[str(i)].value()

    def set(self):
        for i in xrange(self.params.__len__()):
            self.params[str(i)].setValue(self.recent_values[str(self.params[str(i)].accessibleName())])

    def setup(self):
        """
        label = QtGui.QLabel()
        label.setText(filter_parameters[self.num]['name'])
        self.grid.addWidget(label, 1, 0, 1, 1)
        """

        for i in xrange(filter_parameters[self.num]['params'].__len__()):

            if filter_parameters[self.num]['params'][str(i)]['display'] == 'NONE':
                continue
            if not filter_parameters[self.num]['params'][str(i)]['type'] == 'bool':
                param_lbl = QtGui.QLabel(filter_parameters[self.num]['params'][str(i)]['display'])
                self.grid.addWidget(param_lbl, i+1, 0)

            param = None
            if filter_parameters[self.num]['params'][str(i)]['type'] == 'int':
                param = QtGui.QSpinBox()
                param.setAccessibleName(filter_parameters[self.num]['params'][str(i)]['name'])
                try:
                    param.setSingleStep(filter_parameters[self.num]['params'][str(i)]['step'])
                except Exception, e:
                    pass
            elif filter_parameters[self.num]['params'][str(i)]['type'] == 'double':
                param = QtGui.QDoubleSpinBox()
                param.setAccessibleName(filter_parameters[self.num]['params'][str(i)]['name'])
            elif filter_parameters[self.num]['params'][str(i)]['type'] == 'bool':
                param = QtGui.QCheckBox()
                param.setText(filter_parameters[self.num]['params'][str(i)]['display'])
                param.setChecked(filter_parameters[self.num]['params'][str(i)]['value'])
                param.setAccessibleName(filter_parameters[self.num]['params'][str(i)]['name'])
            try:
                param.setMinimum(filter_parameters[self.num]['params'][str(i)]['min'])
            except Exception, e:
                pass
            try:
                param.setMaximum(filter_parameters[self.num]['params'][str(i)]['max'])
            except Exception, e:
                pass
            try:
                param.setValue(filter_parameters[self.num]['params'][str(i)]['value'])
            except Exception, e:
                pass
            self.recent_values[filter_parameters[self.num]['params'][str(i)]['name']] = param.value()
            self.params[str(i)] = param
            self.grid.addWidget(param, i+1, 1)

            param.valueChanged.connect(self.update)
