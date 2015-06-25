__author__ = 'uleob'

possibleFilters = {
    '0':{'text': 'Threshold',               'index': 0,     'module_name': 'thresh',     'class': 'Thresh_tab'},
    '1':{'text': 'Image Smoothing',         'index': 1,     'module_name': 'smooth',     'class': 'Smooth_tab'},
    '2':{'text': 'Gaussian Blur',           'index': 2,     'module_name': 'gauss',      'class': 'Gauss_tab'},
    '3':{'text': 'Median Filter',           'index': 3,     'module_name': 'median',     'class': 'Median_tab'},
    '4':{'text': 'Bilateral Filter',        'index': 4,     'module_name': 'bilateral',  'class': 'Bilateral_tab'},
    '5':{'text': 'Opening',                 'index': 5,     'module_name': 'opening',    'class': 'Opening_tab'},
    '6':{'text': 'Closing',                 'index': 6,     'module_name': 'closing',    'class': 'Closing_tab'},
    '7':{'text': 'Morphological Gradient',  'index': 7,     'module_name': 'morph',      'class': 'Morph_tab'},
    '8':{'text': 'Sobel Operator',          'index': 8,     'module_name': 'sobel',      'class': 'Sobel_tab'},
    '9':{'text': 'Laplace Derivate',        'index': 9,     'module_name': 'laplace',    'class': 'Laplace_tab'},
    '10':{'text': 'Canny Edge Detection',   'index': 10,    'module_name': 'canny',      'class': 'Canny_tab'}
    # '11':{'text': 'Watershed',              'index': 11,    'module_name': 'watershed',  'class': 'Watershed_tab'}
}

possibleDetectors = {
    '0':{'text': 'OpenCV-Contours'},
    '1':{'text': 'Prob. Hough Lines'},
    '2':{'text': 'Watershed + Contours'}
}

filter_parameters = {
    '0':    {'name': 'Threshold', 'module': 'cv2', 'funcName': 'threshold',
             'params':  {'0':   {'display': 'Low Threshold', 'name': 'low_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 127},
                         '1':    {'display': 'Max. Threshold', 'name': 'high_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 255}
                        }
            },
    '1':    {'name': 'Image Smoothing', 'module': 'cv2', 'funcName': 'blur',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2}
                        }
            },
    '2':    {'name': 'Gaussian Blur', 'module': 'cv2', 'funcName': 'GaussianBlur',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Sigma X', 'name': 'sigmaX', 'type': 'double', 'min': 0, 'max': 99.99, 'value': 0},
                         '2':   {'display': 'Sigma Y', 'name': 'sigmaY', 'type': 'double', 'min': 0, 'max': 99.99, 'value': 0}
                        }
            },
    '3':    {'name': 'Median Blur', 'module': 'cv2', 'funcName': 'medianBlur',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2}
                        }
            },
    '4':    {'name': 'Bilateral Filter', 'module': 'cv2', 'funcName': 'bilateralFilter',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Sigma Space', 'name': 'space', 'type': 'int', 'min': 0, 'max': 9999, 'value': 75},
                         '2':   {'display': 'Sigma Color', 'name': 'color', 'type': 'int', 'min': 0, 'max': 9999, 'value': 75}
                        }
            },
    '5':    {'name': 'Opening', 'module': 'cv2', 'funcName': 'morphologyEx',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Iterations', 'name': 'iterations', 'type': 'int', 'min': 0, 'max': 99, 'value': 1},
                         '2':   {'display': 'NONE', 'name': 'MORPH_OPEN', 'type': 'cv2'}
                        }
            },
    '6':    {'name': 'Closing', 'module': 'cv2', 'funcName': 'morphologyEx',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Iterations', 'name': 'iterations', 'type': 'int', 'min': 0, 'max': 99, 'value': 1},
                         '2':   {'display': 'NONE', 'name': 'MORPH_CLOSE', 'type': 'cv2'}
                        }
            },
    '7':    {'name': 'Morphological Gradient', 'module': 'cv2', 'funcName': 'morphologyEx',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 99, 'value': 3, 'step': 2},
                         '1':   {'display': 'Iterations', 'name': 'iterations', 'type': 'int', 'min': 0, 'max': 99, 'value': 1},
                         '2':   {'display': 'NONE', 'name': 'MORPH_GRADIENT', 'type': 'cv2'}
                        }
            },
    '8':    {'name': 'Sobel Operator', 'module': 'cv2', 'funcName': 'Sobel',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': -1, 'max': 7, 'value': 3, 'step': 2},
                         '1':   {'display': 'derivate X', 'name': 'dX', 'type': 'bool', 'value': True},
                         '2':   {'display': 'derivate Y', 'name': 'dY', 'type': 'bool', 'value': False}
                        }
            },
    '9':    {'name': 'Laplace Derivate', 'module': 'cv2', 'funcName': 'Laplacian',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 1, 'max': 31, 'value': 3, 'step': 2}
                        }
            },
    '10':   {'name': 'Canny Edge Detector', 'module': 'cv2', 'funcName': 'Canny',
             'params':  {'0':   {'display': 'Kernel Size', 'name': 'size', 'type': 'int', 'min': 3, 'max': 7, 'value': 3, 'step': 2},
                         '1':    {'display': 'Low Threshold', 'name': 'low_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 100},
                         '2':    {'display': 'High Threshold', 'name': 'high_thr', 'type': 'double', 'min': 0, 'max': 255, 'value': 200}
                        }
            }
}