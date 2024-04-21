import pygame
import math
import time
from evdev import InputDevice, categorize, ecodes

class Controller:
    joysticks = {}
    clock = pygame.time.Clock()
    done = False
    screen = pygame.display.set_mode((500,700))
    pygame.display.set_caption("SDC!")
    def __init__(self, controller_index):
        self.joystick = pygame.joystick.Joystick(controller_index)
            
        

        
    def process_events(self):
        self.clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.
            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                self.joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")
            if event.type == pygame.JOYDEVICEREMOVED:
                del self.joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
    
    def get_controller(self):
        return {
            "x1_axis" : self.joystick.get_axis(0),
            "y1_axis" : self.joystick.get_axis(1),
            "x2_axis" : self.joystick.get_axis(3),
            "y2_axis" : self.joystick.get_axis(4),
            "r_axis" : self.joystick.get_axis(2), # for r and l axis, -1 is all the way up, 1 is all the way down
            "l_axis" : self.joystick.get_axis(5),
            
            "b_x"  :  self.joystick.get_button(0),
            "b_o"  :  self.joystick.get_button(1),
            "b_sq" :  self.joystick.get_button(3),
            "b_tr" :  self.joystick.get_button(2),
            "b_share" : self.joystick.get_button(8),
            "b_opt" : self.joystick.get_button(9),
            "bump_r" : self.joystick.get_button(5),
            "bump_l" : self.joystick.get_button(4),
            "x_hat" : self.joystick.get_hat(0,0),
            "y_hat" : self.joystick.get_hat(0,1),

        }
        