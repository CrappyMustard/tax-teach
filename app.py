# These are the libraries that help this program run.
import time
from datetime import date



# This is essentially the main menu for the application. You'll be able to calculate or exit here.
def mainMenu():
    print("Select an option below by typing the corresponding number:")
    print("1. Calculate")
    print("2. Exit")
    while True:
        selection = input()
        if selection not in ("1", "2"):
            print("You entered an invalid option. Try again.")
        else:
            break
    # This is where the calculations happen.
    if selection == "1":
        print("----------------")
        print("Enter the cost of the item in the following format: 00.00")
        while True:
            try:
                price = float(input())
                price = round(price, 2)
                break
            except:
                print("You entered an invalid price. Try again.")
        print("Enter the sales tax being applied in your area in the following format: 0.00")
        while True:
            try:
                tax = float(input())
                tax = round(tax, 2)
                break
            except:
                print("You entered an invalid price. Try again.")
        finalCost = (price * (tax / 100)) + price
        finalCost = format(finalCost, '.2f')
        print(f'The final cost of your purchase should be around ${finalCost}.')
        time.sleep(1)
        print("----------------")
        mainMenu()
    else:
        print("Thanks for using Tax Teach! Goodbye!")
        time.sleep(1)

# This is where all of the code above is ran in full.
print("Welcome to Tax Teach!")
time.sleep(1)
print("----------------")
print(f'Today is {date.today().strftime("%B %d, %Y")}...')
print("----------------")
mainMenu()
