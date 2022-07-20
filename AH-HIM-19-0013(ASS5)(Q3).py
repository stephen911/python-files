
# Declaring variables
# digit = 0
# letter = 0
#
# # Taking input(sentence) from the user
# sentence = input("Enter a sentence\n>>")
#
# # A for loop for check if an item in sentence is a letter or a digit
# for i in sentence:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         letter += 1
#     else:
#         pass
#
#
# # printing out the results
# print("LETTERS {}".format(letter))
# print(letter)
# print("LETTERS", letter)
# print("Letters " + str(letter))
# print("DIGITS {}".format(digit))


# def sum2(a, b):
#     sum1 = a + b
#     print("the sum of", a, "and", b, "is", sum1)
#
#
# input1 = int(input("Enter your first score\n"))
#
# input2 = int(input("Enter your second score\n"))
# sum2(input1, input2)
import time
first = time.time()
numbers = [17, 28, 54, 25]
flag=False
for b in range(4):
    print(numbers[b] == 3)
    if numbers[b] == 3:

        flag=True

    elif numbers[b] == 25:
        flag = True

    else:
        pass
if flag:
    print("found")
else:
    print("n/a")
time.sleep(2)
second = time.time()
final = second - first
print(final)



