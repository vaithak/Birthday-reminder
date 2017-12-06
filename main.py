import datecheck
import shelve


def addinlist():
    adddate = shelve.open("birthdaysfile",writeback=True)
    print("Please enter the name of person: ", end='')
    name = input()
    print("Please give his birthday date (in format dd/mm): ", end='')
    Date = input()
    Date = datecheck.validate(Date)
    if Date != 'FALSE':
        adddate['birthdays'][name] = Date
        print(name + ": " + adddate['birthdays'][name])
        print("Added\n")
    else:
        print("Error!!! \nInvalid Date")
    adddate.close()


def deleteinlist():
    deldate = shelve.open("birthdaysfile",writeback=True)
    print("Enter the name of the person you want to delete: ", end='')
    name = input()
    try:
        del(deldate['birthdays'][name])
        print(name + ": " + deldate['birthday'][name] + 'deleted from database\n')
    except KeyError:
        print("Sorry! The person is not in the list")
    deldate.close()


def checkbyname():
    checkbirthday = shelve.open("birthdaysfile")
    print("Please Enter the Name of the person:", end='')
    name = input()
    if name in checkbirthday['birthdays'].keys():
        print(name + ": " + checkbirthday['birthdays'][name] + "\n")
    else:
        print("Sorry! Person is Not in the list\n")
    checkbirthday.close()


def checkbydate():
    retbydate = shelve.open("birthdaysfile")
    print("Please enter the birthday date to check (in format dd/mm): ", end='')
    Date = input()
    Date = datecheck.validate(Date)
    if Date != 'FALSE':
        for name, chkDate in retbydate['birthdays'].items():
            if Date == chkDate:
                print(name + ": " + chkDate)
            else:
                print("Sorry ! No one with given birth date present in the database")
    else:
        print("ERROR!!! \nInvalid Date")
    retbydate.close()

def printlist():
    printdays = shelve.open("birthdaysfile")
    count = 0
    print(printdays['birthdays'])
    for name, date in printdays['birthdays'].items():
        print(name + ": " + date)
        count = count + 1
    if count == 0:
        print("No person in the list")
    print("\n")
    printdays.close()


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
