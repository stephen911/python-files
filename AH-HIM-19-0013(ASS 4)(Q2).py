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


print("{} is the maximum number".format(max(list_of_nums)))
print("{} is the minimum number".format(min(list_of_nums)))