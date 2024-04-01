#!/home/blackweldera/venv/bin/python3
import pygame
import math
from controller import Controller
from gpiozero import Servo, PWMOutputDevice
import time
from evdev import InputDevice, categorize, ecodes

pygame.init()


left_motor = Servo(21, frame_width=.01-.00000002)
right_motor = Servo(20, frame_width=.01-.00000002)

def round(input):
    return int(input * 10)/10
def mix(x,y):
    # +y is forward, -y is backward, +x is left, -x is right... change if needed
    mag = math.sqrt(x**2 + y**2)
    angle = math.atan2(y,x)
    left = mag * math.sin(angle) + mag * math.cos(angle)
    right = mag * math.sin(angle) - mag * math.cos(angle)
    return (round(right), round(left))
    
    
    

def main():
    gamepad = Controller()

    done = False
    while not done:
        gamepad.process_events()
        gps = gamepad.get_controller(0)
        
        motor_vals = (round(gps["x1_axis"]), round(gps["x2_axis"]))
        right_motor.value = round(motor_vals[0])
        left_motor.value = round(motor_vals[1])
        print(motor_vals[0])
        print(motor_vals[1])
        print("\n")
	


