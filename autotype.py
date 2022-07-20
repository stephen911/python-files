import pyautogui as p
import time


# time.sleep(5)
# for i in range(100):
#     for k in range(3):
#         p.press("down")
#     for t in range(7):
#         p.press("right")
#     for f in range(10):
#         p.press("backspace")
    # p.press("backspace")
    # for t in range(3):
    #     p.press("left")
    # for f in range(4):
    #     p.press("backspace")
    # p.typewrite(", ")
    # p.press("down")
    # print(i)


# for w in range(40):
#     for h in range(6):
#         p.press("down")
#     for f in range(5):
#         p.press("backspace")
time.sleep(10)
file = open("co_ord.txt", "r")
cou = 0
for i in file:
    for h in range(11):
        p.press("down")
        p.press("end")
    p.typewrite(i)
    cou += 1
print(i)

print(cou)

