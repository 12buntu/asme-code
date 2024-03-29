#!/home/blackweldera/venv/bin/python3
import pygame
import math
from gpiozero import Servo, PWMOutputDevice
import time
from evdev import InputDevice, categorize, ecodes

pygame.init()


left_motor = Servo(21, frame_width=.01-.00000002)
right_motor = Servo(20, frame_width=.01-.00000002)



# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
# class TextPrint:
#     def __init__(self):
#         self.reset()
#         self.font = pygame.font.Font(None, 25)

#     def tprint(self, screen, text):
#         text_bitmap = self.font.render(text, True, (0, 0, 0))
#         screen.blit(text_bitmap, (self.x, self.y))
#         self.y += self.line_height

#     def reset(self):
#         self.x = 10
#         self.y = 10
#         self.line_height = 15

#     def indent(self):
#         self.x += 10

#     def unindent(self):
#         self.x -= 10

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
    # Set the width and height of the screen (width, height), and name the window.
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get ready to print.
    #text_print = TextPrint()

    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.
            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")
            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        #text_print.reset()

        # Get count of joysticks.
        joystick_count = pygame.joystick.get_count()

        #text_print.tprint(screen, f"Number of joysticks: {joystick_count}")
        for joystick in joysticks.values():
################################### IMPORTANT STUFF ##################################################################            
            x1_axis = joystick.get_axis(0)
            y1_axis = joystick.get_axis(1)
            x2_axis = joystick.get_axis(3)
            y2_axis = joystick.get_axis(4)
            r_axis = joystick.get_axis(2) # for r and l axis, -1 is all the way up, 1 is all the way down
            l_axis = joystick.get_axis(5)
            
            b_x = joystick.get_button(0)
            b_o = joystick.get_button(1)
            b_sq = joystick.get_button(3)
            b_tr = joystick.get_button(2)
            #motor_vals = mix(x1_axis, y1_axis)
            # right_motor.value = motor_vals[0]
            # left_motor.value = motor_vals[1]
            motor_vals = (x1_axis, x2_axis)
            print(motor_vals[0])
            print(motor_vals[1])
            print("\n")
        
        
            
################################################################################################
        # Go ahead and update the screen with what we've drawn.
        #pygame.display.flip()

        # Limit to 30 frames per second.
        clock.tick(30)
	
if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


