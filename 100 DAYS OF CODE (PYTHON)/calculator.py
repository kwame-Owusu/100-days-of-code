import os
from calculator_art import logo

print(logo)


restart = False


# Putting the whole process in a while loop to make it run over and over again, depeding on user input.

while not restart:
    operation = input("Pick and operation:\n +\n -\n * \n / \n")
    # addition
    if operation == "+":
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        result = num1 + num2
        print(result)
        # subtraction
    elif operation == "-":
    
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        result = num1 - num2
        print(result)
        # multiplication
    elif operation == "*":
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        result = num1 * num2
        print(result)
        # division
    elif operation == "/":
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        result = num1 / num2
        print(result)
    else:
        print("INVALID INPUT")
    
    # asking the user if he/she wants make another opearation, then the screen clears for additional operations.
    restart_calc = input("Would like to make another calculation? Type 'y' or 'n \n").lower()
    if restart_calc == "n":
        restart = True
    elif restart_calc == "y":
        os.system('cls')

    print()
        




