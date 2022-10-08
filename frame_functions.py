
from pyautogui import screenshot

from mss import mss
# sct = mss()
# sct.shot()

from grab_screen import grab_screen

if __name__ == "__main__":
    for i in range(10):
        grab_screen('ssss.png')