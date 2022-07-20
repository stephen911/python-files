def divisor():
    try:
        n = int(input("Enter an integer:"))
    except Exception as e:
        print(e)
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    print("The factors of {} are {}".format(n, factors))


def greatest_common_divisor():
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    try:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
    except Exception as e:
        print(e)

    g = gcd(a, b)
    print("The greatest common divisor of {} and {} is {}".format(a, b, g))


divisor()
greatest_common_divisor()











