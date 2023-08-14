
import datetime

date_of_birth = input("Enter your date of birth in YYYY-MM-DD format: ")
try:
    date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
except ValueError:
    print("Invalid input. Please try again.")
    exit()

now = datetime.datetime.now()

difference = now - date_of_birth

weeks = difference.days // 7
days = difference.days % 7
seconds = difference.seconds

print(f"You have lived for {weeks} weeks, {days} days and {seconds} seconds.")