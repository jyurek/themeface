#!/usr/bin/env python3

import picamera
import numpy as np

class Camera(object):

    def __init__(self, resolution, camera_index=0):
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.output_buffer = np.empty((240, 320, 3), dtype=np.uint8)

    def capture(self):
        self.camera.capture(self.output_buffer, format="bgr")
        return self.output_buffer

    def release(self):
        "Ok, cool."
