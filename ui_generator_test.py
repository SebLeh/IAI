# -*- coding=utf-8 -*-
__author__ = 'uleob'

from PyQt4 import QtGui
import sys

parameters = {
    '1':{'name': 'Canny Edge Detector', 'module': 'cv2', 'func name': 'Canny',
         'params':{'0':{'display': 'Kernel Size', 'name': 'size', 'type':'int', 'min': 3, 'max': 7, 'value': 3, 'step': 2},
                   '1':{'display': 'Low Threshold', 'name': 'low_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 100},
                   '2':{'display': 'High Threshold', 'name': 'high_thr', 'type': 'double', 'min': 0, 'max': 255}
                   }
         }
}

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setObjectName(u"MainWindow")
        self.resize(474, 429)

        self.centralWidget =  QtGui.QWidget()

        self.embedded = GeneratedWidget()

        self.setup()

    def setup(self):

        self.area = QtGui.QScrollArea()

        self.area.setWidget(self.embedded)

        self.layout =  QtGui.QGridLayout(self.centralWidget)
        self.layout.addWidget(self.area, 0, 0, 0, 0)

        self.setCentralWidget(self.centralWidget)

class GeneratedWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.grid = QtGui.QGridLayout(self)
        self.recent_values = {}
        self.setup()

    def setup(self):
        label = QtGui.QLabel()
        label.setText(parameters['1']['name'])
        self.grid.addWidget(label, 1, 0, 1, 1)

        for i in xrange(parameters['1']['params'].__len__()):
            param_lbl = QtGui.QLabel(parameters['1']['params'][str(i)]['display'])
            self.grid.addWidget(param_lbl, i+2, 0)

            param = None
            if parameters['1']['params'][str(i)]['type'] == 'int':
                param = QtGui.QSpinBox()
                try:
                    param.setSingleStep(parameters['1']['params'][str(i)]['step'])
                except Exception, e:
                    pass
            elif parameters['1']['params'][str(i)]['type'] == 'double':
                param = QtGui.QDoubleSpinBox()
            try:
                param.setMinimum(parameters['1']['params'][str(i)]['min'])
            except Exception, e:
                pass
            try:
                param.setMaximum(parameters['1']['params'][str(i)]['max'])
            except Exception, e:
                pass
            try:
                param.setValue(parameters['1']['params'][str(i)]['value'])
                self.recent_values[param.objectName()] = param.value()
            except Exception, e:
                pass
            self.grid.addWidget(param, i+2, 1)

def main():

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



