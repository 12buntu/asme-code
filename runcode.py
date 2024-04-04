#!/home/blackweldera/venv/bin/python3
import pygame
from controller import Controller
from hardware import Chassis

pygame.init()

def main():
    gamepad = Controller(0)
    chassis = Chassis()
    done = False
    while not done:
        gamepad.process_events()
        gps = gamepad.get_controller(0)
        
        chassis.drive(-gps["y1_axis"], gps["x1_axis"])
        
        
if __name__ == "__main__":
    main()