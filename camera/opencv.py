#!/usr/bin/env python

import cv2

class Camera(object):

    def __init__(self, resolution, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)
        self.resolution = resolution

    def capture(self):
        ret, frame = self.camera.read()
        # return cv2.resize(frame, self.resolution)
        return cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    def rotate(self, image, rotation=0):
        if rotation == 90:
            out = cv2.transpose(image)
            return cv2.flip(out, flipCode=1)
        elif rotation == 180:
            out = cv2.flip(image, flipCode=0)
            return cv2.flip(out, flipCode=1)
        elif rotation == 270:
            out = cv2.transpose(image)
            return cv2.flip(out, flipCode=0)
        else:
            return image

    def release(self):
        self.camera.release()
