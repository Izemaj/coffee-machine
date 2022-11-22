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


def sufficient_resources(order_ingredient):
    """ Checks if the resources are sufficient to make the order"""
    for item in order_ingredient:
        if resources[item] < order_ingredient[item]:
            print(f"Sorry we don't have enough {item}")
            return False
        else:
            return True


def coffee_machine():
    order = input("What would you like to order?(espresso/latte/cappuccino):").lower()

    if order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        coffee_machine()
    elif order == "off":
        print("Machine has been turned off for maintenance")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if sufficient_resources(MENU[order]['ingredients']):
            quarters = float(input("How many quarters? "))
            dimes = float(input("How many dimes? "))
            nickels = float(input("How many nickels? "))
            pennies = float(input("How many pennies? "))

            price = MENU[order]["cost"]
            amount = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)

            if amount < price:
                print("Sorry that's not enough money. Money refunded.")
                coffee_machine()
            elif amount == price:
                for item in MENU[order]["ingredients"]:
                    resources[item] -= item
                print("Here is $0.0 in change")
                print(f"Here is your {order} ☕️. Enjoy!")
                coffee_machine()
            else:
                for item in MENU[order]["ingredients"]:
                    resources[item] -= MENU[order]["ingredients"][item]
                change = amount - price
                print(f"Here is ${change} in change")
                print(f"Here is your {order} ☕️. Enjoy!")
                coffee_machine()

    else:
        print("Invalid Input. Try again!")
        coffee_machine()


coffee_machine()
