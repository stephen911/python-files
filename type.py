import pyautogui as p
import time
time.sleep(5)
counter = 0
#make sure the mirror share is at the leftmost part of the screen for this to work
#Do well to the click in the type bar after running the program
while counter < 10:
    p.typewrite("hello")
    time.sleep(0.2)
    p.moveTo(331, 583, 0.5)
    p.click()
    counter += 1
#p.mouseInfo(hello)

