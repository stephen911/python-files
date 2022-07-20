from pyautogui import click
from time import sleep
import time
from tkinter import *
import csv
import matplotlib.pyplot as plt
import collections
import sys
import datetime
def autoclick():
    sleep(5)
    count = 0
    while count < 1:
        click()
        sleep(0.5)
        count += 1

# def tick():
#     time_string = time.strftime("%H:%M:%S")
#     clock.config(text=time_string)
#     clock.after(200, tick)
#
#
# root = Tk()
# clock = Label(root, font=("calibra", 250, "bold"), bg="white")
# clock.grid(row=0, column=1)
# tick()
# root.mainloop()
lans = []
dict1 = dict()
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for line in csv_reader:
        lang = line[1]
        lang = str(lang)
        each_lang = lang.split(";")
        #print(each_lang)
        for lan in each_lang:
            lans.append(lan)



#print(lans)

for i in lans:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

print(dict1)
print(len(lans))
keys = []
values = []
for item in dict1:
    #print(item)
    #print(dict1[item])
    keys.append(item)
    values.append(dict1[item])

print(keys)
print(values)

plt.plot(values, keys)
plt.tight_layout()
plt.show()