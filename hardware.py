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
        self.right_motor = Motor(right)