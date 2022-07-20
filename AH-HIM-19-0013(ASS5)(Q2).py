
# defining a dictionary with month as key and number of days a value
days_in_month_dict = {"January": 31, "February": 28,
                      "March": 31, "April": 30,
                      "May": 31, "June": 30,
                      "July": 31, "August": 31,
                      "September": 30, "October": 31,
                      "November": 30, "December": 31}


# function to check if the year is a leap year
def is_leap_year(leap_year):
    return (leap_year % 4 == 0) and (leap_year % 100 != 0) or (leap_year % 400 == 0)

# function to print out the number of days a month has
def days_in_month(year, month):
    # check if the year is a leap year and the month is february
    if is_leap_year(year) and month == "February":
        return print(month, "has 29 days in a leap year")

    try:
        # attempt to get value from dictionary
        return print(month, "has", days_in_month_dict[month], "days")

    except KeyError:
        # key does not exist, so we caught the error
        return None

# Take in input for the year and month
the_year = int(input("Enter year\n>>"))
the_month = input("Enter month\n>>")

# calling the days_in_year function
days_in_month(the_year, the_month.capitalize())