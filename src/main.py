import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode

DELAY = 0.001  
BTN = Button.left
START_KEY = KeyCode(char='a')
STOP_KEY = KeyCode(char='b')
EXIT_KEY = KeyCode(char='e') 

mouse = MouseController()
clicking = False
active = True

class Clicker(threading.Thread):
    def run(self):
        while active:
            while clicking:
                mouse.click(BTN)
                time.sleep(DELAY)
            time.sleep(0.1)

def on_press(key):
    global clicking, active
    if key == START_KEY:
        clicking = True
    elif key == STOP_KEY:
        clicking = False
    elif key == EXIT_KEY:
        active = False
        listener.stop()

click_thread = Clicker()
click_thread.start()

listener = Listener(on_press=on_press)
listener.start()
listener.join()

print("Auto click pausado")