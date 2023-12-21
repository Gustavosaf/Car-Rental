from functions import *
import os
os.system("cls") 
#_________________________________________________

print("\n========\nWelcome to the car rental company!\n=======")

while True:
    os.system("cls")

    menu()

    option = int(input())
    
    if option == 0:
        showPortfolio(carPortfolio)
        subOption = int(input("0 - CONTINUE | 1 - EXIT")) 
        if subOption == 0:
            continue
        else:
            break
    elif option == 1:
        os.system("cls")
        showPortfolio(carPortfolio)
        carCode = int(input("Enter the car code."))
        days = int(input("How many days do you want to rent the car?."))
        finalValue = calculate(carCode, days)
        print(finalValue)
        subOption = int(input("0 - CONTINUE | 1 - EXIT")) 
        if subOption == 0:
            removeCar(carCode)
            continue
        else:
            break
    elif option == 2:
        print("Cars to return")
        showPortfolio(rentedCar)
        carCode = int(input("Choose the car code that you want do return:"))
        returnCar(carCode)
        subOption = int(input("0 - CONTINUE | 1 - EXIT")) 
        if subOption == 0:
            removeCar(carCode)
            continue
        else:
            break