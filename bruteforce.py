from random import randint
from time import time
from math import floor
from winsound import Beep
start = time()
guess = ""
password = input("Password: ")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while guess != password:
    guess = ""
    for letter in password:
        guessletter = letters[randint(0, 25)]
        guess = str(guessletter + str(guess))
    print(guess)
end = time()
final = end - start
final = floor(final)
print("password cracked in " + str(final) + " seconds")
Beep(10000, 500)

