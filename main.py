#!/home/blackweldera/venv/bin/python3
import pygame
from subprocess import Popen
from time import sleep
from os import execl
import sys
from controller import Controller
from hardware import Chassis, Motor, Solenoid, GenMotor


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
    flywheel = GenMotor(16,19) #one above 20
    linact = GenMotor(6,12)
    spinny = Motor(5,width=.02)
    bonk = Solenoid(13) 
    done = False
    while not done:
        gamepad.process_events()
        gps = gamepad.get_controller()
        ###
        flywheel.send_power((round((gps["l_axis"]) + 1) / 2)-(round((gps["r_axis"]) + 1) / 2))
        chassis.drive(gps["y1_axis"], gps["x1_axis"])
        spinny.send_power(gps["x2_axis"])
        linact.send_power(gps["y1_axis"])
        if gps["b_opt"]: 
            Popen('git pull', shell=True)
            sleep(2.5)
            print("restart!")
            execl(sys.executable, sys.executable, *sys.argv)
        if gps["b_x"]: bonk.toggle()
        if gps["bump_l"]: linact.send_power(1)
        if gps["bump_r"]: linact.send_power(-1)
       # if not (gps["bump_l"] or gps["bump_r"]): linact.send_power(0)
    
        
if __name__ == "__main__":
    main()