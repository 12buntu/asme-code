from approxeng.input.selectbinder import ControllerResource
from time import sleep
class Controller:
    previously_connected = False
    def __init__(self, controller_index):
        return

    def get_joystick(self): #access all joystick inputs as attributes of joystick (joystick.lx, .ly, .rx, .ry)
        try:
          with ControllerResource() as joystick:   
            if not joystick.connected:
                raise IOError("joystick.connected false")
            else:
                if not self.previously_connected:
                    print("Joystick Connected")    
                    self.previously_connected = True
                return joystick
        except IOError:
            print("Connection to joystick lost")
            self.previously_connected = False
            sleep(1.0)
                            
    def get_press():
        return ControllerResource().presses
        