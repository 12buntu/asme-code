#!/home/blackweldera/venv/bin/python3
import pygame
from subprocess import Popen
from time import sleep
from os import execl
import sys
from controller import Controller
from hardware import Chassis

pygame.init()
Popen('sudo pigpiod', shell=True)
sleep (2.5)

def main():

    gamepad = Controller(0)
    chassis = Chassis(20,21)
    done = False
    while not done:
        gamepad.process_events()
        gps = gamepad.get_controller()
        
        chassis.drive(gps["y1_axis"], gps["x1_axis"])
        print(round(gps["y1_axis"],1), -round(gps["x1_axis"],1))
        if gps["b_x"]: 
            Popen('git pull', shell=True)
            sleep(2.5)
            execl(sys.executable, sys.executable, *sys.argv)
        
if __name__ == "__main__":
    main()