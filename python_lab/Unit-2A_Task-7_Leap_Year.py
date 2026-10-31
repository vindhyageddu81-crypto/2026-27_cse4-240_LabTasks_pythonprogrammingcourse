# check a given year is a leap year or not
year = int(input("Enter a year: "))
if year % 400 == 0:  # outer leap-year check
    print(f"{year} is a leap year")
else:
    if year % 100 == 0:  # nested check
        print(f"{year} is not a leap year")
    else:
        if year % 4 == 0:  # innermost check
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")