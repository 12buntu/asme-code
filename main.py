#!/home/blackweldera/venv/bin/python3
from subprocess import Popen
from time import sleep
from os import execl
import sys
from controller import Controller
from hardware import Chassis, Motor, Solenoid, GenMotor

def main():
    # Define Pi inputs/outputs according to https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2023/03/Raspberry-Pi-Pinout-Random-Nerd-Tutorials.png?resize=1024%2C576&quality=100&strip=all&ssl=1
    gamepad = Controller() 
    
    chassis = Chassis(20,21)                            # Main Drive Motors
    flywheel = GenMotor(16,19)                          # Flywheel Motors #one above 20 
    linact = GenMotor(6,12)                             # Linear Actuator to Raise/Lower Arm
    spinny = Motor(pin=4, min=.5/1000, max=2.5/1000,width=20/1000, multiplier=1)        # 360-Continuous Servo used to rotate arm
    bonk = Solenoid(13)                                 # Solenoid used to push ball into flywheel
    n20_1 = Motor(22)                                # N-20 Motors used to load ball into flywheel
    n20_2 = Motor(23)
    
    done = False
    while not done:
        # Process inputs of controllers
        presses = gamepad.get_press()
        joystick = gamepad.get_joystick()
        ###____________________________________________________________________________________###
        
        # Main Control Scheme
        chassis.drive(joystick.lx,joystick.ly)

        # Ball Control Scheme
        n20_1.send_power(joystick.l1 - joystick.r1])
        n20_2.send_power(gps["bump_l"] - gps["bump_r"])
        flywheel.send_power((round((gps["l_axis"]) + 1) / 2)-(round((gps["r_axis"]) + 1) / 2))
        if gps["b_x"]: bonk.toggle()
        
        ### Other control layout lines --> Not currently in use

        #if gps["bump_l"]: linact.send_power(1)
        #if gps["bump_r"]: linact.send_power(-1)
        #if not (gps["bump_l"] or gps["bump_r"]): linact.send_power(0)

        # Update Code without keyboard
        if gps["b_opt"]: 
            Popen('git pull', shell=True)
            sleep(2.5)
            print("restart!")
            execl(sys.executable, sys.executable, *sys.argv)
        
def antidrift(input, factor=.2):
    return factor * round(input/factor)        
if __name__ == "__main__":
    main()