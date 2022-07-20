list_of_nums = []

num = ""
while num != -1:
    try:
        num = int(input("enter a number:"))
    except Exception as e:
        print(e)
    if num == -1:
        pass
    else:
        list_of_nums.append(num)

print("The maximum number is {}".format(max(list_of_nums)))
print("The minimum number is {}".format(min(list_of_nums)))


