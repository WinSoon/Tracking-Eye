import gpiozero
import RPi.GPIO as GPIO

class Actuator(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # Actuators dictionaries thought to be for a grid of 3 cols and 3 rows.
        # The row position is controlled by 2 GPIOs, and other 2 GPIOs for the columns
        # position
        # Rows initialization
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        output_row_dict = {}
        output_row_dict[0] = [GPIO.LOW, GPIO.HIGH]
        output_row_dict[1] = [GPIO.HIGH, GPIO.HIGH]
        output_row_dict[2] = [GPIO.HIGH, GPIO.LOW]

        # Columns initialization
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
        output_col_dict = {}
        output_col_dict[0] = [GPIO.LOW, GPIO.HIGH]
        output_col_dict[1] = [GPIO.HIGH, GPIO.HIGH]
        output_col_dict[2] = [GPIO.HIGH, GPIO.LOW]

        print("Actuator initialized")
        
    def update_output(self, activated_row, activated_column):
        GPIO.output(18, output_row_dict[activated_row][0])
        GPIO.output(23, output_row_dict[activated_row][1])

        GPIO.output(24, output_col_dict[activated_column][0])
        GPIO.output(25, output_col_dict[activated_column][1])

if __name__ == '__main__':
    obj = Actuator()