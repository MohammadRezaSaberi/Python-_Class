from datetime import datetime

def display_date():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    date = datetime(year, month, day)
    print(date.strftime("%B %d, %Y"))

display_date()
