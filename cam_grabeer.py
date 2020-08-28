from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import copy
import time

class CameraGrabber(object):
    def __init__(self, img_width, img_height, frame_rate):
        self.image_width = img_width
        self.image_height = img_height
        self.frame_rate = frame_rate

        self.camera = PiCamera()
        self.camera.resolution = (self.image_width, self.image_height)
        self.camera.framerate = self.frame_rate
        self.rawCapture = PiRGBArray(self.camera, size=(self.image_width, self.image_height))

        print("Warming up camera...")
        time.sleep(1)
        print("Camera Grabber initialized")

    def get_image(self):
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image - this array
            # will be 3D, representing the width, height, and # of channels
            image = frame.array
            if not image is None:
                rawCapture.truncate(0)
                break

        return image

if __name__ == '__main__':
    obj = CameraGrabber()