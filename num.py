import re
delimiter = ","
file = open("nums.txt", "r")
list1 = []
f = open("frest.txt", "w")
count = 0
n = 0
for line in file:
    m = line.split(delimiter)
    for num in m:
        if "+9" in num:
            count += 1
        else:
            n += 1
            f.write(num)
            print(num, end=",")
print()
print("{} gh numbers".format(count))
print("{} foreign numbers".format(n))
tot = n + count
print("{} numbers altogether".format(tot))






