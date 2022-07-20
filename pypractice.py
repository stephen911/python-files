import random
import collections, pprint


def random1():
    char_list = ["a", "e", "i", "o", "u"]
    while True:
        random.shuffle(char_list)
        print("".join(char_list))

def freq():
    file = input("file Name: ")
    with open(file, "r") as info:
        count = collections.Counter(info.read().upper())
        value = pprint.pformat(count)
    print(value)

#random1()
freq()