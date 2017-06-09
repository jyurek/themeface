#!/usr/bin/env python

import cv2

class Camera(object):

    def __init__(self, resolution):
        self.camera = cv2.VideoCapture(0)
        self.resolution = resolution

    def capture(self):
        ret, frame = self.camera.read()
        return cv2.resize(frame, self.resolution)

    def release():
        self.camera.release()
