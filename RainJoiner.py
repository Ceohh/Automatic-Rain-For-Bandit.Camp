from pyautogui import *
import pyautogui
import time
import keyboard
import random
import threading

def press_ctrl_r():
    while True:
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(120)  # 2 minutes

# Create a new thread to run the CTRL + R pressing function
ctrl_r_thread = threading.Thread(target=press_ctrl_r)
ctrl_r_thread.start()

# Your main script can continue running here
while True:
    if pyautogui.locateOnScreen('Rain.png', confidence=0.7) != None:
        pyautogui.click(98, 865)
        time.sleep(0.5)
        print("Rain Collected :) - Liquid")
