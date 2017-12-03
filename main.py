import accessData
import datecheck


def addinlist():
    print("h")


def deleteinlist():
    print("j")


def checkbyname():
    print("Please Enter the Name of the person:", end=' ')
    name = input()
    if name in accessData.birthdays:
        print(accessData.birthdays[name] + "\n")
    else:
        print("Sorry! Person is Not in the list\n")


def checkbydate():
    datecheck.validate()


def printlist():
    for name, date in accessData.birthdays.items():
        print(name + ": " + date)
    print("\n")


print("Welcome to Birthday Reminder\n")

choices = 5
cont = 'c'

while cont == 'c':
    choice = 0
    print("\nWhat do you want to do ? (press the corresponding choice no.) \n")
    print("1. Add a new person's birthday in the list.")
    print("2. Delete a person's birthday from your list.")
    print("3. Check a person's birthday from his name.")
    print("4. Check if anyone has birthday on a particular date.")
    print("5. Print the whole list")
    while choice <= 0 or choice > choices:
        print(f"Please enter a valid input of choice between 1 and {choices}")
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
    print("OK \n")
    if choice == 1:
        addinlist()
    elif choice == 2:
        deleteinlist()
    elif choice == 3:
        checkbyname()
    elif choice == 4:
        checkbydate()
    else:
        printlist()

    print("Do you want to continue or exit ? (press c to continue)")
    cont = input()
