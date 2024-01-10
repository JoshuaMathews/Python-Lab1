# import datetime library for getting month
from datetime import datetime

# ask for name and birthday month
name = input("What is your name? ")
month = input("What month were you born in? ")

print("Hello, " + name + "!")

# grab current date
currentDate = datetime.now()

# if the user inputs the month as a number that is the first condition
# 2nd condition checks if they input the month name equals the current month name when program is ran
if currentDate.month == month or currentDate.strftime("%B").lower() == month.strip().lower():
    print("Happy Birthday month!")

# Get length of user's name and output length.
print(f"There are {len(name)} letters in your name")