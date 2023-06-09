import pyautogui
import time

limit = 50
start = 0

time.sleep(5)

while start < limit:
    pyautogui.write("heyy....")
    pyautogui.press("enter")
    start = start + 1
