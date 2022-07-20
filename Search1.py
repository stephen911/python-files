import pyautogui
import time
print("*" * 70)
print("THIS PROGRAM SEARCHES THROUGH YOUR PC TO FIND YOUR SEARCH TERM.\nPRODUCED BY: STEDAP COMPANY LTD.")
print("*" * 70)

while True:
    search = input("PLEASE ENTER YOUR SEARCH TERM\n>>")
    pyautogui.moveTo(71, 742)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(search)
    time.sleep(1)
    pyautogui.press("enter")