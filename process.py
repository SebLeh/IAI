__author__ = 'uleob'

import cv2

class Image():
    def __init__(self):
        self.image = None
        self.grey_img = None

    def update(self, image, object_index, applied_filters, loaded_classes):
        return self.image