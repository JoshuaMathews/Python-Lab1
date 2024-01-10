from calendar import c
from datetime import datetime

classesTaken = []

for classTaken in range(int(input("How many classes are you taking this semester? "))):
    localClass = input("Enter the name of your class: ")
    classesTaken.append(localClass)

print("The classes you are taking are:")

for className in classesTaken:
    print(className)
    
