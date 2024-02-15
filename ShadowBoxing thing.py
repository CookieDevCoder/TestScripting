import pyautogui
import keyboard
import time
import random

ison = False

while keyboard.is_pressed('y') == False :
    ranint = random.randint(1, 4)
    if (ranint == 1) :
        pyautogui.press('up')
        time.sleep(0.25)
        print("pressed up")
    elif (ranint == 2) :
        pyautogui.press('down')
        print("pressed down")
    elif (ranint == 3) :
        pyautogui.press('right')
        print("pressed right")
    else :
        pyautogui.press('left')
        print("pressed left")
    
    
    time.sleep(0.25)
    if keyboard.is_pressed('y') :
        exit()

