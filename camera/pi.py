#!/usr/bin/env python3

import picamera
import numpy as np

class Camera(object):

    def __init__(self, resolution):
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.output_buffer = np.empty((240, 320, 3), dtype=np.uint8)

    def capture(self):
        self.camera.capture(self.output, format="bgr")
        self.output

    def release():
        "Ok, cool."
