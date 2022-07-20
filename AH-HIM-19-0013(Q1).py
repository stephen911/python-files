num = ""
total = 0
count = 0
while num != "done":
    try:
        num = input("Enter a number:")
        if num.isdigit():
            int(num)
        else:
            pass
        total = total + int(num)
        count = count + 1
    except Exception as e:
        print("Enter a valid number")


try:
    average = total / count
except ZeroDivisionError as e:
    average = 0

print("The average of the numbers is {}".format(average))
print("The sum of the numbers is {}".format(total))
print("The total numbers entered is {}".format(count))
