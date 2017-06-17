#!/usr/bin/env python3

import picamera
import numpy as np

class Camera(object):

    def __init__(self, resolution, camera_index=0):
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.output_buffer = np.empty((240, 320, 3), dtype=np.uint8)

    def capture_frame(self):
        self.camera.capture(self.output_buffer, format="bgr")
        return self.output_buffer

    def rotate(self, image, rotation=0):
        if rotation == 90:
            out = np.transpose(image)
            return np.fliplr(out)
        elif rotation == 180:
            out = np.flipud(image)
            return np.fliplr(out)
        elif rotation == 270:
            out = np.transpose(image)
            return np.flipud(out)
        else:
            return image

    def release(self):
        self.camera.close()
