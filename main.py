from cam_grabeer import CameraGrabber
from shape_detector import ShapeDetector
from grid_splitter_algorithm import GridSplitterAlgorithm
from actuator import Actuator

import cv2

# System configuration
image_width = 640
image_height = 480
framerate = 32
minimum_area = 250
maximum_area = 100000

# Objects initialization
cam = CameraGrabber(image_width, image_height, framerate)
detector = ShapeDetector()
grid = GridSplitterAlgorithm(image_width, image_height, 3, 3)
actuators = Actuator()
# Initialialing with negative numbers will produce always an update
old_grid_pos = [-1,-1]

while True:
    image = cam.get_image()
    contours = detector.detect_contours(image)

    ball_location = detector.detect_circle()
    if ball_location:
        if (ball_location[0] > minimum_area) and (ball_location[0] < maximum_area):
            new_grid_pos = grid.find_grid_position(ball_location[1], ball_location[2])
            update_required = grid.check_change(ball_location[1], ball_location[2], old_grid_pos, new_pos)
            if update_required:
                actuators.update_output(new_grid_pos[1], new_grid_pos[0])

        elif (ball_location[0] < minimum_area):
            print("Target isn't large enough, searching")
        else:
            print("Target large enough, stopping")

    cv2.namedWindow("Frames", cv2.WINDOW_NORMAL)
    cv2.imshow("Frames", image)
	
    key=cv2.waitKey(1)
    if key == 27:
	    break