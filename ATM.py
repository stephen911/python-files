def welcome():
    print("%" * 25)
    print("*" * 25)
    print("WELCOME TO STEDAP ATM")
    print("*" * 25)
    print("%" * 25)


def menu():
    if select == "1":
        balance = 1000
        amount = input("Enter the amount you wish to deposit:")
        balance = int(balance) + int(amount)
        print("*" * 50)
        print("%" * 50)
        print("You have successfully deposited Ghc" + str(amount) + ".00 in you account")
        print("Your current balance is Ghc" + str(balance) + ".00\nThank you for using Stedap ATM")
        print("%" * 50)
        print("*" * 50)
    elif select == "2":
        balance = 1000
        withdrawal = int(input("Enter the amount you wish to withdraw:"))
        if withdrawal > balance:
            print("*" * 50)
            print("%" * 50)
            print("Your balance is insufficient. Please check your account and try again\nThank you for using Stedap ATM")
            print("%" * 50)
            print("*" * 50)
        else:
            balance = balance - withdrawal
            print("*" * 70)
            print("%" * 70)
            print("You have successfully withdrew Ghc" + str(withdrawal) +".00 from your account\nYour current balance is Ghc" + str(balance) + ".00\nThank you for using Stedap ATM")
            print("%" * 70)
            print("*" * 70)
    elif select == "3":
        balance = 1000
        print("*" * 50)
        print("%" * 50)
        print("You have Ghc" + str(balance) + ".00 in your account\nThank you for using Stedap ATM")
        print("%" * 50)
        print("*" * 50)
    elif select == "4":
        pin = int(input("Enter you old pin:"))
        if pin not in passwords:
            new_pin = int(input("Enter your new pin:"))
        else:
            print("Incorrect pin\nTry again later")
        confirm = int(input("Confirm your pin:"))
        if new_pin == confirm:
            print("*" * 50)
            print("%" * 50)
            print("You have successfully change your pin from", str(pin), "to", str(confirm), )
            print("Thank you for using Stedap ATM")
            print("%" * 50)
            print("*" * 50)
        else:
            print("*" * 50)
            print("%" * 50)
            print("Pins to not match")
            print("%" * 50)
            print("*" * 50)

    elif select == "5":
        balance = 1000
        transfer = int(input("Please enter amount you wish to transfer:"))
        if transfer > balance:
            print("*" * 50)
            print("%" * 50)
            print("You have insufficient balance in your account")
            print("%" * 50)
            print("*" * 50)
        else:
            person = str(input("Enter the number:"))
            name = str(input("Enter the name of the person:"))
            upper = name.upper()
            balance = balance - transfer
            print("*" * 50)
            print("%" * 50)
            print("You have successfully transferred Ghc" + str(transfer) + ".00 to Mr/Mrs " + str(upper))
            print("Your current balance is Ghc" + str(balance) + ".00")
            print("Thank you for using Stedap ATM")
            print("%" * 50)
            print("*" * 50)
    elif select == "6":
        exit()


welcome()
welcome = input("Enter one(1) to sign in\nEnter two(2) to sign up\n>>")
account = ["stephen", "ama", "kofi", "yaa", "sunshine", "amina", "gertrude", "cobby", "danny", "sunshine"]
passwords = ["1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "1234"]
#print(type(account.index("stephen")))
#print(type(passwords.index("2222")))

one = "1"
two = "2"


while welcome != one and welcome != two:
    welcome = input("Enter one(1) to sign in:\nEnter two(2) to sign up:")

if welcome == one:
    username = input("Please enter your username:")
    user_counter = 3

    while username not in account and user_counter > 0:
        print("Username is invalid")
        print("You have ", user_counter, "attempt remaining.")
        username = input("Please enter your username:")
        user_counter -= 1
    if username in account:
        password = input("Enter your password:")
        try:
            if account.index(username) == passwords.index(password):
                print("*" * 50)
                print("%" * 50)
                select = input("1. Deposit\n2. Withdraw\n3. Check balance\n4. Change pin\n5. Transfer money\n6. Exit")
                menu()
            else:
                print("invalid password try")
                pass1 = 3
                while account.index(username) != passwords.index(password) and pass1 > 0:
                    print("*" * 50)
                    print("%" * 50)
                    print("Incorrect password")
                    print("You have", pass1, "attempt(s) left")
                    password = input("Enter your password:")
                    print("%" * 50)
                    print("*" * 50)
                    pass1 -= 1
                else:
                    print("*" * 50)
                    print("%" * 50)
                    select = input(
                        "1. Deposit\n2. Withdraw\n3. Check balance\n4. Change pin\n5. Transfer money\n6. Exit")
                    menu()
        except Exception as err:
            print("invalid password")

    else:
        print("*" * 50)
        print("%" * 50)
        print("ALERT!!!\nInvalid Account\nPlease Sign Up")
        print("%" * 50)
        print("*" * 50)

if welcome == two:
    user_up = input("Please enter your username:")
    user_count = 0
    while user_up in account and user_count < 3:
        print("*" * 50)
        print("%" * 50)
        print("ALERT!!!\nusername already exist\nPlease enter a different username")
        print("*" * 50)
        print("%" * 50)
        user_up = input("Please enter your username:")
        user_count += 1
    else:
        if user_up not in account:
            password_up = input("Enter a four(4) digit pin\nEnter your pin:")
            digit = password_up.isdigit()
            if len(password_up) == 4 and digit:
                print("*" * 80)
                print("%" * 80)
                print("Congratulations! you have successfully created an account with Stedap ATM")
                print("%" * 80)
                print("*" * 80)
                select = input("1. Deposit\n2. Withdraw\n3. Check balance\n4. Change pin\n5. Transfer money\n6. Exit")
                menu()
            else:
                print("*" * 50)
                print("%" * 50)
                print("ALERT!!!\nInvalid password")
                print("%" * 50)
                print("*" * 50)





