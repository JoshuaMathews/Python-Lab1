# initialize an empty array
classesTaken = []

# Grab class count from user input, string -> int -> range so we can iterate over that.
for classTaken in range(int(input("How many classes are you taking this semester? "))):
    # grab class name
    localClass = input("Enter the name of your class: ")
    # add class name to array
    classesTaken.append(localClass)

print("The classes you are taking are:")

# print out the class name by iterating over the array
for className in classesTaken:
    print(className)
    
