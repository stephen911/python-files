# import os
# import shutil
#
# path = os.path.abspath("deans.png")
# print(path)
# os.chdir(r"C:\\")
# shutil.copy(r"C:\\Users\\Stephen Dapaah\\Documents\\sunday", r'C:\\Users\\Stephen Dapaah\\Desktop\\junks')
import pyautogui, time, random, os

# for i in range(1, 6):
#     print("*" * i)
# for k in range(6, 0, -1):
#     print("*" * k)
#
# n = "stephen"
# m = len(n)
# counter = -1
# for i in range(m):
#     print(n[counter], end="")
#     counter -= 1
# print()
#
# #fabinocci
# x, y = 0, 1
# while y < 50:
#     print(y)
#     x, y = y, x + y

x = []
y = []
search = "excel"
print("*" * 80)
print("This program takes X-values and their corresponding Y-values to draw a graph")
print("*" * 80)
num = int(input("How many X-value would you like to enter?\n>>"))
print("NOTE: Enter one value at a time. Press enter after each value entered")
for i in range(0, num):
    xvalues = input("Enter your X-Values\n>>")
    # #v = random.randrange(1, 20)
    # pyautogui.typewrite("2")
    # time.sleep(0.2)
    # pyautogui.press("enter")
    # pyautogui.typewrite("2")
    x.append(xvalues)
print("*" * 55)
print("Enter their corresponding Y-values in the same order")
print("*" * 55)
for t in range(0, num):
    yvalues = input("Enter your y-values\n>>")
    y.append(yvalues)
time.sleep(1)
# pyautogui.moveTo(71, 742)
# pyautogui.click()
# time.sleep(0.5)
# pyautogui.typewrite(search)
# time.sleep(1)
# pyautogui.press("enter")
# time.sleep(7)
os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
time.sleep(2)
try:
    pyautogui.locateOnScreen("snip_excel.PNG")
    pyautogui.click("snip_excel.PNG")
except Exception as e:
    print("Couldn't find the image(snip excel): " + str(e))
    quit()
time.sleep(2.5)
try:
    pyautogui.locateOnScreen("snip_exbox.PNG")
    pyautogui.click("snip_exbox.PNG")
except Exception as e:
    print("Couldn't find the image(snip exbox): " + str(e))
    quit()
time.sleep(0.2)
x.reverse()
y.reverse()
u = num
while num > 0:
    pyautogui.typewrite(x[num-1])
    pyautogui.press("down")
    num -= 1
pyautogui.locateOnScreen("snip_B.PNG")
pyautogui.click("snip_B.PNG")
while u > 0:
    pyautogui.typewrite(y[u-1])
    pyautogui.press("down")
    u -= 1
pyautogui.press("up")
pyautogui.hotkey("ctrl", "a")
time.sleep(2)
try:
    pyautogui.locateOnScreen("snip_insert.PNG")
    pyautogui.click("snip_insert.PNG")
except Exception as e:
    print("Couldn't find the image(snip insert): " + str(e))
    quit()
time.sleep(3)
try:
    pyautogui.locateOnScreen("snip_scatter.PNG")
    pyautogui.click("snip_scatter.PNG")
except Exception as e:
    print("Couldn't find the image(snip scatter): " + str(e))
    quit()
time.sleep(3)
pyautogui.moveRel(100, 400)
time.sleep(2)
pyautogui.click()
pyautogui.moveTo(430, 315)
time.sleep(2)
pyautogui.click()
pyautogui.moveRel(400, 0, duration=0.5)
pyautogui.click()
time.sleep(1.5)
try:
    pyautogui.locateOnScreen("snip_okay.PNG")
    pyautogui.click("snip_okay.PNG")
except Exception as e:
    print("Couldn't find the image(snip okay): " + str(e))
    quit()
time.sleep(2)
try:
    pyautogui.locateOnScreen("snip_plus.PNG")
    pyautogui.click("snip_plus.PNG")
except Exception as err:
    print("cant find trendline: {}".format(err))
    quit()
time.sleep(0.5)
pyautogui.moveTo(997, 490)
time.sleep(1)
pyautogui.click()
confirm = pyautogui.confirm("Do you want to print or save the Graph?", "Print Command", buttons=["Print", "Save", "Cancel"])
if confirm == "Print":
    pyautogui.hotkey("ctrl", "p")
elif confirm == "Save":
    pyautogui.hotkey("ctrl", "s")
else:
    pass

