__author__ = 'uleob'

possibleFilters = {
    '0':{'text': 'Threshold simple'},
    '1':{'text': 'Threshold adaptive'},
    '2':{'text': 'Image Smoothing'},
    '3':{'text': 'Gaussian Blur'},
    '4':{'text': 'Median Filter'},
    '5':{'text': 'Bilateral Filter'},
    '6':{'text': 'Opening'},
    '7':{'text': 'Closing'},
    '8':{'text': 'Morphological Gradient'},
    '9':{'text': 'Sobel Operator'},
    '10':{'text': 'Laplace Derivate'},
    '11':{'text': 'Canny Edge Detection'},
    # '11':{'text': 'Watershed'}
}

filter_parameters = {
    '0':    {'name': 'Threshold simple', 'module': 'cv2', 'funcName': 'threshold',
             'params':  {'0':    {'display': 'Threshold Type', 'name': 'type', 'type': 'drop-down', 'value': 0, 'values':
                                        {0: 'Binary', 1: 'Binary inverted', 2: 'Otsu'} },
                         '1':    {'display': 'Low Threshold', 'name': 'low_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 140},
                         '2':    {'display': 'Max. Threshold', 'name': 'high_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 255},
                         '3':    {'display': 'Invert Output', 'name': 'invert', 'type': 'bool', 'value': False}
                        }
            },
    '1':    {'name': 'Threshold adaptive', 'module': 'cv2', 'funcName': 'threshold',
             'params':  {# '0':   {'display': 'Low Threshold', 'name': 'low_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 127},
                         '0':    {'display': 'Threshold Type', 'name': 'type', 'type': 'drop-down', 'value': 0, 'values':
                                        {0: 'Adaptive Mean', 1: 'Adaptive Gaussian'} },
                         '1':    {'display': 'Threshold Value', 'name': 'high_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 255},
                         '2':    {'display': 'Invert Output', 'name': 'invert', 'type': 'bool', 'value': False}
                        }
            },
    '2':    {'name': 'Image Smoothing', 'module': 'cv2', 'funcName': 'blur',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2}
                        }
            },
    '3':    {'name': 'Gaussian Blur', 'module': 'cv2', 'funcName': 'GaussianBlur',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Sigma X', 'name': 'sigmaX', 'type': 'double', 'min': 0, 'max': 99.99, 'value': 0},
                         '2':   {'display': 'Sigma Y', 'name': 'sigmaY', 'type': 'double', 'min': 0, 'max': 99.99, 'value': 0}
                        }
            },
    '4':    {'name': 'Median Blur', 'module': 'cv2', 'funcName': 'medianBlur',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2}
                        }
            },
    '5':    {'name': 'Bilateral Filter', 'module': 'cv2', 'funcName': 'bilateralFilter',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Sigma Space', 'name': 'space', 'type': 'int', 'min': 0, 'max': 9999, 'value': 75},
                         '2':   {'display': 'Sigma Color', 'name': 'color', 'type': 'int', 'min': 0, 'max': 9999, 'value': 75}
                        }
            },
    '6':    {'name': 'Opening', 'module': 'cv2', 'funcName': 'morphologyEx',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Iterations', 'name': 'iterations', 'type': 'int', 'min': 0, 'max': 99, 'value': 1},
                         '2':   {'display': 'NONE', 'name': 'MORPH_OPEN', 'type': 'cv2'}
                        }
            },
    '7':    {'name': 'Closing', 'module': 'cv2', 'funcName': 'morphologyEx',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Iterations', 'name': 'iterations', 'type': 'int', 'min': 0, 'max': 99, 'value': 1},
                         '2':   {'display': 'NONE', 'name': 'MORPH_CLOSE', 'type': 'cv2'}
                        }
            },
    '8':    {'name': 'Morphological Gradient', 'module': 'cv2', 'funcName': 'morphologyEx',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Iterations', 'name': 'iterations', 'type': 'int', 'min': 0, 'max': 99, 'value': 1},
                         '2':   {'display': 'NONE', 'name': 'MORPH_GRADIENT', 'type': 'cv2'}
                        }
            },
    '9':    {'name': 'Sobel Operator', 'module': 'cv2', 'funcName': 'Sobel',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': -1, 'max': 7, 'value': 3, 'step': 2},
                         '1':   {'display': 'derivate X', 'name': 'dX', 'type': 'bool', 'value': True},
                         '2':   {'display': 'derivate Y', 'name': 'dY', 'type': 'bool', 'value': False}
                        }
            },
    '10':    {'name': 'Laplace Derivate', 'module': 'cv2', 'funcName': 'Laplacian',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 31, 'value': 3, 'step': 2}
                        }
            },
    '11':   {'name': 'Canny Edge Detector', 'module': 'cv2', 'funcName': 'Canny',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 3, 'max': 7, 'value': 3, 'step': 2},
                         '1':    {'display': 'Low Threshold', 'name': 'low_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 100},
                         '2':    {'display': 'High Threshold', 'name': 'high_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 200},
                         '3':    {'display': 'Invert Output', 'name': 'invert', 'type': 'bool', 'value': False}
                         }
            }
}

possibleDetectors = {
    '0':{'text': 'OpenCV-Contours'},
    '1':{'text': 'Prob. Hough Lines'},
    '2':{'text': 'Hough Lines'}
    # '2':{'text': 'Watershed + Contours'}
}

detector_parameters = {
    '0':    {'name': 'CV2 Contour Detector', 'module': 'cv2', 'funcName': 'findContours',
             'params':  {'0': {'display': 'No. of Results (biggest contours)', 'name': 'results', 'type': 'int', 'min': 1, 'value': 20},
                         '1': {'display': 'Find rectangles', 'name': 'rectangles', 'type': 'bool', 'value': False}
                        }

            },
    '1':    {'name': 'Prob. Hough Lines', 'module': 'cv2', 'funcName': 'HoughLinesP',
             'params':  {# '0': {'display': 'Negate Image', 'name': 'negative', 'type': 'bool', 'value': False},
                         '0': {'display': 'rho (Pixel Step Size)', 'name': 'rho', 'type': 'int', 'min': 1, 'max': 9999, 'value': 1},
                         '1': {'display': 'theta (Measured Angles)', 'name': 'theta', 'type': 'int', 'min': 1, 'max': 180, 'value': 180},
                         '2': {'display': 'threshold ("Line Votes")', 'name': 'thresh', 'type': 'int', 'min': 2, 'max': 99999, 'value': 20},
                         '3': {'display': 'Min. Line Length', 'name': 'minLength', 'type': 'int', 'min': 2, 'max': 99999, 'value': 100},
                         '4': {'display': 'Max. Line Gap', 'name': 'maxGap', 'type': 'int', 'min': 1, 'max': 99999, 'value': 100}
                        }
             },
    '2':    {'name': 'Hough Lines', 'module': 'cv2', 'funcName': 'HoughLines',
             'params':  {# '0': {'display': 'Negate Image', 'name': 'negative', 'type': 'bool', 'value': False},
                         '0': {'display': 'rho (Pixel Step Size)', 'name': 'rho', 'type': 'int', 'min': 1, 'max': 9999, 'value': 1},
                         '1': {'display': 'theta (Measured Angles)', 'name': 'theta', 'type': 'int', 'min': 1, 'max': 180, 'value': 180},
                         '2': {'display': 'threshold ("Line Votes")', 'name': 'thresh', 'type': 'int', 'min': 2, 'max': 99999, 'value': 200}
                        }
             }
}