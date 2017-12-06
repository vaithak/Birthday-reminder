import datecheck
import shelve
import os


def addinlist():
    adddate = shelve.open("birthdaysfile", writeback=True)
    print("Please enter the name of person: ", end='')
    name = input()
    print("Please give his birthday date (in format dd/mm): ", end='')
    Date = input()
    Date = datecheck.validate(Date)
    if Date != 'FALSE':
        adddate['birthdays'][name.title()] = Date
        print(name.title() + ": " + adddate['birthdays'][name.title()])
        print("Added\n")
    else:
        print("Error!!! \nInvalid Date")
    adddate.close()


def deleteinlist():
    deldate = shelve.open("birthdaysfile", writeback=True)
    print("Enter the name of the person you want to delete: ", end='')
    name = input()
    try:
        print(name.title() + ": " + deldate['birthdays'][name.title()] + 'deleted from database\n')
        del(deldate['birthdays'][name.title()])
    except KeyError:
        print("Sorry! The person is not in the list\n")
    deldate.close()


def checkbyname():
    checkbirthday = shelve.open("birthdaysfile")
    print("Please Enter the Name of the person:", end='')
    name = input()
    if name.title() in checkbirthday['birthdays'].keys():
        print(name.title() + ": " + checkbirthday['birthdays'][name.title()] + "\n")
    else:
        print("Sorry! Person is Not in the list\n")
    checkbirthday.close()


def checkbydate():
    retbydate = shelve.open("birthdaysfile")
    print("Please enter the birthday date to check (in format dd/mm): ", end='')
    Date = input()
    Date = datecheck.validate(Date)
    flag = 0
    if Date != 'FALSE':
        for name, chkDate in retbydate['birthdays'].items():
            if Date == chkDate:
                print(name.title() + ": " + chkDate)
                flag = 1
        if flag == 0:
            print("Sorry ! No one with given birth date present in the database")
    else:
        print("ERROR!!! \nInvalid Date")
    retbydate.close()

def printlist():
    printdays = shelve.open("birthdaysfile")
    count = 0
    for name, date in printdays['birthdays'].items():
        print(name.title() + ": " + date)
        count = count + 1
    if count == 0:
        print("No person in the list")
    print("\n")
    printdays.close()

if os.name == 'posix':
    os.system('clear')
elif os.name == 'nt':
    os.system('cls')

print("Welcome to Birthday Reminder\n")

start = shelve.open("birthdaysfile")
start['birthdays'] = {}
start.close()

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
