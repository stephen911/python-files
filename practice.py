import mysql.connector


def connect():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="Student")

    mycursor = mydb.cursor()
    mycursor.execute("show databases")
    for i in mycursor:
        print(i)


def rect():
    print("This program takes the length and breath of rectangle and calculates the area and perimeter")
    lenght = int(input("Enter the lenght of the rectangle(cm)\n>>"))
    breath = int(input("Enter the breath of the rectangle(cm)\n>>"))
    if lenght == breath:
        print("...'")
    else:
        area = lenght * breath
        perimeter = (2*lenght) + (2*breath)
        print("The area of the rectangle is " + str(area) + "cm2")
        print("The perimeter of the rectangle is " + str(perimeter) + "cm")


def while_loop():
    count = 0
    while count < 5:
        print("hello amina")
        count = count + 1


def collapse():
    print("This program tells if a triangle is a collapse triangle")
    first = int(input("Enter the value of the first side\n>>"))
    second = int(input("Enter the value of the second side\n>>"))
    third = int(input("Enter the value of the third side\n>>"))

    if first + second == third:
        print("The triangle is a collapse triangle")
    elif first + third == second:
        print("The triangle is a collapse triangle")
    elif second + third == first:
        print("The triangle is a collapse triangle")
    else:
        print("The triangle is not a collapse triangle")


def right_angle():
    print("This program tells if a triangle is a right-angle triangle")
    first = int(input("Enter the value of the opposite\n>>"))
    second = int(input("Enter the value of the adjacent\n>>"))
    third = int(input("Enter the value of the hypotanous\n>>"))
    if first**2 + second**2 == third**2:
        print("Triangle is a right-triangle")
    else:
        print("Triangle is not a right-triangle")


def find():
    print("This program find the hypotanous, opposite or adjacent")
    select = input("Select which side you want to find\n1. Hypotaneous\n2. Opposite\n3. Adjacent\n>>")
    if select == "1":
        first = int(input("Enter the value of the opposite\n>>"))
        second = int(input("Enter the value of the adjacent\n>>"))
        hyp = (first**2 + second**2)**0.5
        print("The hypotaneous is ", str(hyp))

    elif select == "2":
        first = int(input("Enter the value of the hypotaneous\n>>"))
        second = int(input("Enter the value of the adjacent\n>>"))
        opp = (first**2 - second**2)**0.5
        print("The opposite is ", str(opp))

    elif select == "3":
        first = int(input("Enter the value of the opposite\n>>"))
        second = int(input("Enter the value of the hypotaneous\n>>"))
        adj = (second**2 - first**2)**0.5
        print("The adjacent is", str(adj))

def count_dit_alpha():
    text = input("Enter your text\n>>")
    count2 = 0
    count = 0
    for i in text:
        if i.isdigit():
            count = count + 1

        elif i.isalpha():
            count2 = count2+1
    print("The number of alphabets in the text entered is", str(count))
    print("The number of digits in the text entered is", str(count2))


#print("This program finds the factorial of a number")
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

    # try:
    #     n = int(input("Enter the number\n>>"))
    #     print("The factorial is ", factorial(n))
    # except:
    #     print("invalid number")











