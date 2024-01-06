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

go_on = True
profit = 0

while go_on:

    def check_resources(drink):
        """To check avail. are enough resources for drink."""
        for thing in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][thing] > resources[thing]:
                print(f"sorry there's not enough {thing}.")
                return False
            else:
                return True


    def process_coins():
        """Total received amount."""
        print("Please insert coins.")
        amount = 0.25 * float(input("How many quarters?"))
        amount += 0.10 * float(input("How many dimes?"))
        amount += 0.05 * float(input("How many nickles?"))
        amount += 0.01 * float(input("How many pennies?"))
        return round(amount)


    def check_transaction(drink, amount):
        """To check received amount enough for drink payment."""
        if MENU[drink]["cost"] > amount:
            print("Sorry, That's not enough money. MONEY REFUNDED.")
        elif MENU[drink]["cost"] <= amount:
            global profit
            profit += MENU[drink]["cost"]
            for ing in MENU[drink]["ingredients"]:
                resources[ing] -= MENU[drink]["ingredients"][ing]
            change = amount - MENU[drink]["cost"]
            print(f"Your total bill is ${amount}. Here's your change ${change}")
            print(f"Here's your {drink}. ENJOY!!")


    choice = input("What would you like? ('espresso'/'latte'/'cappuccino'): ").lower()
    if choice == "report":
        # for item in resources:
        #     print(f"{item} : {resources[item]}")
        print(f"Water = {resources['water']} ml.")
        print(f"Milk = {resources['milk']} ml.")
        print(f"Coffee = {resources['coffee']} g.")
        print(f"Total profit is {profit}")
    elif choice == "off":
        go_on = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            r_amount = process_coins()
            check_transaction(choice, r_amount)
    else:
        go_on = False
        print("INVALID INPUT.")
