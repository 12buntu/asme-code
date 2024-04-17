import math
from gpiozero import Servo, Device, PWMOutputDevice

from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory()

# from gpiozero.pins.mock import MockFactory
# Device.pin_factory = MockFactory()

class Motor:
    def __init__(self, pin, multiplier=1, width=.01, min = .001, max=.002):
        self.servo_control = Servo(pin, frame_width = width, min_pulse_width=min, max_pulse_width=max)
        self.multiplier = multiplier
    def send_power(self, power):
        self.servo_control.value = power * self.multiplier
#class genMotor:
    # def __init__(self, pin, multiplier=1, width=.01, frequency=100):
    #     self.pwm_dev = PWMOutputDevice(pin,True,0,frequency)
        
class Solenoid:
    def __init__(self, pin):
        self.solenoid = Motor(pin,1,.01)
        self.state = -1
    def toggle(self):  
        if self.state == -1:
            self.state = 1
        else:
            self.state = -1
        self.solenoid.send_power(self.state)
        
class Chassis:
    def __init__(self, left, right):
        self.left_motor = Motor(left)
        self.right_motor = Motor(right,-1)
    def mix(self, drive, rotate):
        # variables to determine the quadrants
        maximum = max(abs(drive), abs(rotate))
        total, difference = drive + rotate, drive - rotate
        left = 0
        right = 0

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
            'left' : .2 * round(left/.2), 
            'right' : .2 * round(right/.2)
            }
    def drive(self, drive, rotate):
        motor_vals = self.mix(drive,rotate)
        self.left_motor.send_power(motor_vals['left'])
        self.right_motor.send_power(motor_vals['right'])
  
    
##