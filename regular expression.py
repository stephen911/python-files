import re, os, shutil
pattern = re.compile(r"(\d{4})-(\d{3})-(\d{3})")
match = pattern.search("my number is 0244-107-754")
try:
    print("match found: " + match.group())
    print(match.group(1) + match.group(2) + match.group(3))
except Exception:
    print("Match not found")

"""The ? matches zero or one of the preceding group. 
•	The * matches zero or more of the preceding group. 
•	The + matches one or more of the preceding group. 
•	The {n} matches exactly n of the preceding group. 
•	The {n,} matches n or more of the preceding group. 
•	The {,m} matches 0 to m of the preceding group. 
•	The {n,m} matches at least n and at most m of the preceding group. 
•	{n,m}? or *? or +? performs a nongreedy match of the preceding group. 
•	^spam means the string must begin with spam. 
•	spam$ means the string must end with spam. 
•	The . matches any character, except newline characters. 
•	\d, \w, and \s match a digit, word, or space character, respectively. 
•	\D, \W, and \S match anything except a digit, word, or space character, respectively. 
•	[abc] matches any character between the brackets (such as a, b, or c). 
•	[^abc] matches any character that isn’t between the brackets."""

#os.chdir(r"C:\Users\Stephen Dapaah\PycharmProjects\hello")
#shutil.copy(r"C:\Users\Stephen Dapaah\PycharmProjects\hello\amina.py", r"C:\Users\Stephen Dapaah\PycharmProjects\hello\me")
#shutil.copytree() #copies the everything in the folder
#shutil.move()

check = re.compile(r"[a-zA-Z0-9]")
mat = check.search("a")
if mat:
    print("found a match")
else:
    print("match not found")

#Lowercase letters hoined with a n underscore
checka = re.compile(r"a-z_a-z")
mat2 = checka.search("this man is ac_ds")
if mat2:
    print("found a match")
else:
    print("match not found")

#upper case letter followed by lower case letters
check3 = re.compile("^food")
mat3 = check3.search("food man is adsbsafsd")
if mat3:
    print("found a match")
else:
    print("match not found")

#a program that matches a string that has an "a" followed by anything ending with "b"
check4 = re.compile(r"a\w*b$")
mat4 = check4.search("food man is adsbsafsdb")
if mat4:
    print("found a match")
else:
    print("match not found")

#matches a word at end of string with at least one
check5 = re.compile(r"\w[,\.\?]+")
mat5 = check5.search("food man is adsbsafsdb?")
if mat5:
    print("found a match")
else:
    print("match not found")
#remove leading zeros from an ip address
ip = "0000000000192.168.1.10"
check6 = re.compile("^0+")
mat6 = check6.search(ip)
if mat6:
    print("found a match")
else:
    print("match not found")

print(mat6.group())
c = len(mat6.group())
print(c)
new = ip[c:]
print(new)