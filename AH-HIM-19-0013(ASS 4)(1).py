try:
    num = int(input("Enter a number:"))
    if (num >= 1) and (num <= 100):
        print("OK")
    else:
        pass
except Exception as e:
    print(e)