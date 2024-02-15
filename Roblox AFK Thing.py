import pyautogui
import keyboard
import time

ison = False

while keyboard.is_pressed('y') == False :
    pyautogui.press('w')
    print("pressed moved")
    time.sleep(60)
    if keyboard.is_pressed('y') :
        exit()

