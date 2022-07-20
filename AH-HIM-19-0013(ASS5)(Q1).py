def wages(x, y):
    # calculate gross pay
    gross_pay = x * y
    return gross_pay


hours = ""
rate_per_hour = ""


try:
    # Input number of hours worked and rate per hour
    hours = float(input("How many hours do you work?\n>>"))
    rate_per_hour = float(input("At what rate are you paid?\n>>"))

except Exception as e:
    # Catching exceptions
    print("please enter a number")

if hours > 50:
    # if number of hour is greater than 50 double the rate per hour and calculate gross pay
    rate_per_hour *= 2
    grossPay = wages(rate_per_hour, hours)
else:
    # calculate gross pay
    grossPay = wages(rate_per_hour, hours)

# print out gross pay
print("Your gross pay is {}".format(grossPay))