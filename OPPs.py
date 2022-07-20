import random
class Computer:
    def __init__(self):
        self.name = "stephen"
        self.age = 29


com = Computer()

print(com.name)
print(com.age)

#f = open("smallchrome.PNG", "rb")
#f1 = open("newchrome.PNG", "wb")

#for i in f:
 #   f1.write(i)
def linear_search():
    list1 = [2, 3, 4, 5, 7, 4, 9, 10, 11, 12]
    n = 12

    for i in range(0, len(list1)):
        if list1[i] == n:
            print("found")
            break
    else:
        print("Not found")


pos = -1


def binary_search(list1, a):
    l = 0
    u = len(list1)-1

    while l <= u:
        mid = (l + u)//2
        if list1[mid] == u:
            globals()["pos"] = mid
            return True

        else:
            if list1[mid] < a:
                l = mid+1
            else:
                u = mid-1

    return False


    list = [2, 3, 4, 6, 8, 98, 23, 34]
    list = list.sort()
    n = 98
    if binary_search(list, n):
        print("found at {}".format(pos+1))
    else:
        print("not found")


def bubble_sort():
    list = [3, 2, 4, 6, 8, 98, 7, 34]
    num = len(list)
    for j in range(num-1, 0, -1):
        print(j)
        for i in range(j):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp


    print(list)


#bubble_sort()


list = [3, 2, 4, 6, 8, 98, 7, 34]


def selection_sort(list):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

    print(list)


selection_sort(list)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


sam = Person("sammy", 18)

print(sam.get_name())


class Pet:
    def __init__(self, name="No name", age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def speak(self):
        print("i dont no what to say")


class Dog(Pet):
    def speak(self):
        print("bark")


class Cat(Pet):
    def speak(self):
        print("meow")


d = Dog()
d.speak()
print(d.get_name())

class Guess:
    def __init__(self, number, min=0, max=100):
        self.number = number
        self.min = min
        self.max = max

    def get_guess(self):
        ur_guess = input("please guess your number between {} and {}\n>>".format(self.min, self.max))
        if self.validate1(ur_guess):
            return int(ur_guess)
        else:
            print("Please enter a valid number")
            self.get_guess()

    def validate1(self, strin):
        val = True
        try:
            num = int(strin)
        except:
            val = False
        return val

    def play(self):
        count = 1
        guess = self.get_guess()
        while True:
            if guess == self.number:
                print("you are right!\nYou won the game")
                print("you guessed {} times".format(count))
                break
            elif guess > self.number:
                print("Your guess is greater than the number")
                guess = self.get_guess()
            elif guess < self.number:
                print("Your guess is less than the number")
                guess = self.get_guess()
            count += 1


ran = random.randint(a=0, b=100)
g = Guess(ran)
g.play()