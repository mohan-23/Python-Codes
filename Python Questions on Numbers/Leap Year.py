# method 1 (Using If, Else)
year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
        else:
            print(year, "is not a Leap Year")
    else:
        print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
print("------------")

# method 2 (Using Ternary Operator)
year = 2004
leap_year = "Leap Year" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Not a Leap Year"
print(leap_year)
print('------------')

# method 3 (Using Calendar Module)

import calendar
year = 2010
leap_year = "Leap Year" if calendar.isleap(year) else "Not a Leap Year"
print(leap_year)