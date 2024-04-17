#!/home/blackweldera/venv/bin/python3
import pygame
from subprocess import Popen
from time import sleep
from os import execl
import sys
from controller import Controller
from hardware import Chassis, Motor, Solenoid


pygame.init()
surface = pygame.display.set_mode((400, 300))

def main():
    no_controller = True
    while no_controller:
        try:
            Controller(0)
        except:
            sleep(.5)
            pygame.display.set_mode((300,400))
        else:
            no_controller = False
    print("controller exists!")
    gamepad = Controller(0) 
    chassis = Chassis(20,21)
    flywheel = Motor(16) #one above 20
    bonk = Solenoid(12) #2 above 16
    done = False
    while not done:
        gamepad.process_events()
        gps = gamepad.get_controller()
        ###
        flywheel.send_power((gps["r_axis"] + 1 / 2))
        print((gps["r_axis"] + 1) / 2)
        chassis.drive(gps["y1_axis"], gps["x1_axis"])
        if gps["b_opt"]: 
            Popen('git pull', shell=True)
            surface.fill(55,44,34)
            sleep(2.5)
            execl(sys.executable, sys.executable, *sys.argv)
        if gps["b_x"]: bonk.toggle()
        
if __name__ == "__main__":
    main()