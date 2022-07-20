import pyautogui as p
import os as o

a = "mark"
b = 2
c  = True
d = 4.3
e = [1, "mark", 3]
f = [3, 5, 2, 6, 8, 6]


if a == "mark" or b == 3:
    print("I am mark")
    if b == 2:
        print(b)
    else:
        print("unknown number")
else:
    print("i dont my name")

for i in e:
    print(i)

for i in range(10):
    print(i)

min1 = min(f)
print("the min value is " + str(min1))
print("the min value is {}".format(min1))


def add(x, y):
    n = x + y
    print(n)


add(2, 3)

for i in range(2):
    for k in range(3):
        print(i*k)
#p.sleep(3)
#p.typewrite("the boy is going to school", 0.5)

o.startfile(r"C:\Users\Stephen Dapaah\Desktop\recent downloads\bella_ciao.mp3")