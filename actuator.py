import gpiozero
import RPi.GPIO as GPIO
import numpy as np

class Actuator(object):
    def __init__(self, grid_size, center_cell):
        self.center_cell = np.array(center_cell)
        self.grid_size = grid_size

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Actuators dictionaries thought to be for a grid of 3 cols and 3 rows.
        # The row position is controlled by 2 GPIOs, and other 2 GPIOs for the columns
        # position
        # Rows initialization
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        self.output_row_dict = {}
        self.output_row_dict[0] = [GPIO.LOW, GPIO.HIGH]
        self.output_row_dict[1] = [GPIO.HIGH, GPIO.HIGH]
        self.output_row_dict[2] = [GPIO.HIGH, GPIO.LOW]

        # Columns initialization
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
        self.output_col_dict = {}
        self.output_col_dict[0] = [GPIO.LOW, GPIO.HIGH]
        self.output_col_dict[1] = [GPIO.HIGH, GPIO.HIGH]
        self.output_col_dict[2] = [GPIO.HIGH, GPIO.LOW]

        # We initialize the system
        starting_row = 1
        starting_col = 1
        GPIO.output(18, self.output_row_dict[starting_row][0])
        GPIO.output(23, self.output_row_dict[starting_row][1])
        GPIO.output(24, self.output_col_dict[starting_col][0])
        GPIO.output(25, self.output_col_dict[starting_col][1])

        self.last_state_set = [starting_row, starting_col]
        print("Actuator initialized")

    def update_output(self, activated_row, activated_column):
        required_state = np.array([activated_row, activated_column])
        new_state = (required_state - self.center_cell) + self.last_state_set

        # Check if the new state boundaries are correct
        if new_state[0] < 0:
            new_state[0] = 0
        elif new_state[0] >= self.grid_size[0]:
            new_state[0] = self.grid_size[0] - 1

        if new_state[1] < 0:
            new_state[1] = 0
        elif new_state[1] >= self.grid_size[1]:
            new_state[1] = self.grid_size[1] - 1

        GPIO.output(18, self.output_row_dict[new_state[0]][0])
        GPIO.output(23, self.output_row_dict[new_state[0]][1])
        GPIO.output(24, self.output_col_dict[new_state[1]][0])
        GPIO.output(25, self.output_col_dict[new_state[1]][1])

        self.last_state_set = new_state

if __name__ == '__main__':
    obj = Actuator()