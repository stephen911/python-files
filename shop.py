from time import time
from datetime import datetime
from random import randint, random, choices
from math import fsum
letters = ["a", "b", "c", "d", "e"]
ran = randint(10000, 10000000)
ordn = randint(1000, 10000)
time1 = datetime.today().ctime()
items = []
quantities = []
total = []
prices = {"milo": 3, "milk": 4, "coke": 1, "fanta": 2, "tomtom": 1}

num = int(input("how many item do u want to enter?\n>>"))
num1 = num
cash = float(input("Cash paid by customer\n>>"))
for i in range(0, num):
    item = input("enter the item\n>>")
    items.append(item)
    quantity = input("enter the quantity\n>>")
    quantities.append(quantity)

print("Nyameb3ky3r3 Enterprise")
print("Amasaman - Obeyeyie")
print("0274846911 / 0245544577")
print("Receipt No.: {}".format(ran))
print("{}".format(time1))
print("User: Nana")
print("Order No.: {}".format(ordn))
print("Item\tQuantity\tPrice(Ghc)\tAmount(Ghc)")
for k, j in items, quantities:
    for key, value in prices.items():
        while num >= 1:
            if key == k:
                print(key, k)
                amount = int(value) * int(quantity)
                total.append(amount)
                print("{}\t{}\t\t\t{}.00\t\t{}.00".format(k, quantity, value, amount))
            num -= 1
print(total)
sum = fsum(total)
print("Items count: {}".format(num1))
print("Subtotal: Ghc{}".format(sum))
print("TOTAL: Ghc{}".format(sum))
print("Cash: Ghc{}".format(cash))
print("Paid amount: Ghc{}".format(cash))
change = cash - sum
print("Change: Ghc{}".format(change))
print("MOMO No# 0245544577")
print("Thank you for doing business with us.\n    GOODS SOLD ARE NOT RETURNABLE")