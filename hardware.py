import math
from gpiozero import Servo, Device

from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory()

# from gpiozero.pins.mock import MockFactory
# Device.pin_factory = MockFactory()

class Motor:
    def __init__(self, pin, multiplier=1):
        self.servo_control = Servo(pin, frame_width = .01)
        self.multiplier = multiplier
    def send_power(self, power):
        self.servo_control.value = power * self.multiplier
        
class Solenoid:
    def __init__(self, pin):
        self.solenoid = None # find gpiozero solenoid pin controller
        self.state = 0
    def toggle(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0
        self.solenoid.set_state(self.state) # this isn't a real function, you should probably fix that when you find out
        
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