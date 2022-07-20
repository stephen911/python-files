# print("This program sums up a list of numbers")
# try:
#     numbers = int((input("How many numbers do you want to sum up?")))
#     list = []
#     for number in range(0, numbers):
#         num = int(input("Enter the number:"))
#         list.append(num)
#     total = 0
#     for i in list:
#         total += i
#
#     print("The sum of the numbers is ", total)
#
# except ValueError:
#     print("Invalid figure")


number1 = int(input("how many numbers do you want to sum up?\n"))
a = []
for numbers in range(0, number1):
    response1 = int(input("enter number\n"))
    a.append(response1)
print(a)

sum=0
for i in a:
    sum=sum + i
    i = i+1
print(sum)