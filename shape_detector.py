import cv2
import numpy as np 

class ShapeDetector(object):
    def __init__(self):
        self.lower_color = np.array([35,74,6])
        self.upper_color = np.array([64, 255, 255])
        print("Shape detector initialized")
        
    def detect_contours(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange(hsv, self.lower_color, self.upper_color)
        contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def detect_circle(self, contours):
        object_area = 0
        object_x = 0
        object_y = 0

        for contour in contours:
            x, y, width, height = cv2.boundingRect(contour)
            found_area = width * height
            center_x = x + (width / 2.0)
            center_y = y + (height / 2.0)
            if object_area < found_area:
                object_area = found_area
                object_x = center_x
                object_y = center_y
        if object_area > 0:
            ball_location = [object_area, object_x, object_y]
        else:
            ball_location = None
            
        return ball_location
    
if __name__ == '__main__':
    obj = ShapeDetector()
    img = cv2.imread('./ball.png', cv2.COLOR_BGR2HSV)
    cv2.namedWindow('Loaded image', cv2.WINDOW_NORMAL)
    cv2.imshow('Loaded image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cont = obj.detect_contours(img)
    print(obj.detect_circle(cont))