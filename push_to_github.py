# import subprocess
import pyautogui as pg
# import os
# os.chdir(r"C:\Users\Stephen Dapaah\Desktop\BackUp_13_09_2019\python files\python zip files\Student-Management-System-Project-In-Python-master")


# pg.mouseInfo()

with open(r"C:\Users\Stephen Dapaah\Desktop\new.txt", "r") as file:
    for i in file:
        pg.moveTo(637, 742)
        pg.click()
        pg.sleep(1)
        pg.write(i)
        pg.hotkey("ctrl", "s")
        pg.sleep(1)
        pg.click(681, 742)
        pg.write("git add .")
        pg.press("enter")
        pg.sleep(1)
        pg.write("git commit -m 'new'")
        pg.press("enter")
        pg.sleep(1)
        pg.write("git push origin main")
        pg.press("enter")
        pg.sleep(2)


        # data = subprocess.check_output(["git", "add", "."]).decode("utf-8").split("\n")
        # # pg.sleep(3)
        # data = subprocess.check_output(["git", "commit", "-m", "new"]).decode("utf-8").split("\n")
        # # pg.sleep(3)
        # # data = subprocess.check_output(["git", "config", "--global", "rebase.autoStash", "true"]).decode("utf-8").split("\n")
        # pg.sleep(3)
        # data = subprocess.check_output(["git", "stash"]).decode("utf-8").split("\n")
        #
        # subprocess.check_output(["git", "pull", "--rebase", "--continue", "origin", "main"]).decode("utf-8").split("\n")
        # # subprocess.check_output(["git", "pull", "--rebase"]).decode("utf-8").split("\n")
        # subprocess.check_output(["git", "stash", "pop"]).decode("utf-8").split("\n")
        #
        #
        # pg.sleep(3)
        # data = subprocess.check_output(["git", "push", "origin", "main"]).decode("utf-8").split("\n")
