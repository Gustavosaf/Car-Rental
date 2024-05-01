from functions import *
import os

os.system("cls") 

input("Welcome to the car rental company!\n==================================\n\nPress any buttom to enter.")

while True:
    os.system("cls")

    menu()

    option = int(input())
    
    if option == 0:
        os.system("cls")
        print("All cars currently available:")
        show_portfolio(car_portfolio, show_values=True)
        while True:
            sub_option = int(input("\n0 - CONTINUE | 1 - EXIT: ")) 
            if sub_option == 0:
                break
            elif sub_option == 1:
                exit()
            else:
                print("Invalid option. Please enter 0 to continue or 1 to exit.")
    elif option == 1:
        os.system("cls")
        print("Rent a car:")
        show_portfolio(car_portfolio, show_values=True)
        car_code = int(input("\nEnter the car code: "))
        days = int(input("\nHow many days do you want to rent the car? "))
        final_value = calculate(car_code, days)
        print(final_value)
        while True:
            sub_option = int(input("\n0 - CONTINUE | 1 - EXIT: ")) 
            if sub_option == 0:
                remove_car(car_code)
                break
            elif sub_option == 1:
                exit()
            else:
                print("Invalid option. Please enter 0 to continue or 1 to exit.")
    elif option == 2:
        os.system("cls")
        print("Cars to return:")
        show_portfolio(rented_car, show_values=False)
        car_code = int(input("\nChoose the car code that you want do return: "))
        return_car(car_code, final_value[5:])
        while True:
            sub_option = int(input("0 - CONTINUE | 1 - EXIT: ")) 
            if sub_option == 0:
                break
            elif sub_option == 1:
                exit()
            else:
                print("Invalid option. Please enter 0 to continue or 1 to exit.")
    elif option == 3:
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")