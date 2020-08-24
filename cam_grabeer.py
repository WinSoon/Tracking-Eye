from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import copy

class CameraGrabber(object):
    def __init__(self, img_width, img_height, frame_rate):
        self.image_width = img_width
        self.image_height = img_height
        self.frame_rate = frame_rate
        
        self.camera = PiCamera()
        self.camera.resolution = (self.image_width, self.image_height)
        self.camera.framerate = self.frame_rate
        self.rawCapture = PiRGBArray(self.camera, size=(self.image_width, self.image_height))

        print("Camera Grabber initialized")

    def get_image(self):
        frame = self.camera.capture(self.rawCapture, format="bgr", use_video_port=True)
        image = copy.deepcopy(frame.array)
        self.rawCapture.truncate(0)

        return image
    
if __name__ == '__main__':
    obj = CameraGrabber()