items = {"milo": 2, "milk": 3, "coke": 4}


def display_items():
    print("Items")
    for index, product in enumerate(items.items()):
        print("{}. {}".format(index+1, product[0]))


display_items()


item = int(input("Which item do you wish to buy?\n>>"))

total_amount = []


def purchase(products):
    for t, i in enumerate(items.items()):
        if t+1 == products:
            print("{} is Ghc{}".format(i[0], i[1]))
            total_amount.append(i[1])


    next_item = int(input("Do you wish to buy another item?\n1. Yes\n2. No\n>>"))
    if next_item == 1:
        display_items()
        new_item = int(input("Which item do you wish to buy?\n>>"))
        purchase(new_item)

    else:

        print("Thank you for using our system. See you soon :)")



purchase(item)
amount = 0
for i in total_amount:
    amount = amount + i

print("The total amount of items purchased is Ghc{}.".format(amount))




