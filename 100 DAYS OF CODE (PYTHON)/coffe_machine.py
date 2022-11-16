import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def enough_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """return true if payment is accepted and false if insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is the change ${change}")
        # this is to get the profit that is outside the scope of the function
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money.")
        return False


def process_coins():
    """returns the total calculated from coins inserted,False if ingredients are not enough"""
    print("please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, ingredients):
    """deduct required ingredients"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}☕")


is_on = True

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino)\n")
    if choice == "off":
        print("shutting down")
        time.sleep(1)
        is_on = False

    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
