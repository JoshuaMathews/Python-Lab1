from datetime import datetime

name = input("What is your name? ")
month = input("What month were you born in? ")

print("Hello, " + name + "!")

currentDate = datetime.now()

if currentDate.month == month or currentDate.strftime("%B").lower() == month.strip().lower():
    print("Happy Birthday month!")
    
print(f"There are {len(name)} letters in your name")