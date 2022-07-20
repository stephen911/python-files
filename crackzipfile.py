import zipfile
from pyautogui import sleep
charlist = "abcdefghijklmnopqrstuvwxyz"
passwords = []

for cpass in range(4):
    a = [i for i in charlist]
    for x in range(cpass):
        a = [y + i for i in charlist for y in a]
    passwords = passwords + a

z = zipfile.ZipFile("secret.zip", "r")
tries = 0
for password in passwords:
    try:
        tries += 1
        #print(password.encode("ascii"))
        z.setpassword(password.encode("ascii"))
        print(password)
        z.extract("secret.txt")
        print(f"Password was found after {tries} attempts and it is {password}")
        break
    except Exception as e:
        print(e)
        pass
