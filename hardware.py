import math
from gpiozero import Servo, PWMOutputDevice

class Motor:
    def __init__(self, pin, multiplier=1):
        self.servo_control = Servo(pin, frame_width = .01)
        self.multiplier = multiplier
    def send_power(self, power):
        self.servo_control.value = power * self.multiplier
        
class Chassis:
    def __init__(self, left, right):
        self.left_motor = Motor(left)
        self.right_motor = Motor(right,-1)
    def mix(self, drive, rotate):
        # variables to determine the quadrants
        maximum = max(abs(drive), abs(rotate))
        total, difference = drive + rotate, drive - rotate
        left, right = 0

        # set speed according to the quadrant that the values are in
        if drive >= 0:
            if rotate >= 0:  # I quadrant
                left = maximum
                right = difference
            else:            # II quadrant
                left = total
                right = maximum
        else:
            if rotate >= 0:  # IV quadrant
                left = total
                right = -maximum
            else:            # III quadrant
                left = -maximum
                right = difference
                
        
        return {
            'left' : math.round(left,1), 
            'right' : math.round(right,1)
            }
    def drive(self, drive, rotate):
        motor_vals = self.mix(drive,rotate)
        self.left_motor.send_power(motor_vals['left'])
        self.right_motor.send_power(motor_vals['right'])