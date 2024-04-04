#!/home/blackweldera/venv/bin/python3
import pygame
from controller import Controller
from hardware import Chassis

pygame.init()

def main():
    gamepad = Controller(0)
    chassis = Chassis(19,21)
    done = False
    while not done:
        gamepad.process_events()
        gps = gamepad.get_controller()
        
        chassis.drive(-gps["y1_axis"], gps["x1_axis"])
        print(round(-gps["y1_axis"],1), round(gps["x1_axis"],1))
        
        
if __name__ == "__main__":
    main()