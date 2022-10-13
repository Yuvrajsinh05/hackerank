from bdb import GENERATOR_AND_COROUTINE_FLAGS
from itertools import count
import pyautogui
import time
time.sleep(4)
count=0
while count<=200:
    pyautogui.typewrite("spam eeeeey gandU")
    pyautogui.press("enter")
    count=count+1
