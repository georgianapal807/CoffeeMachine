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

money = 0


def print_report(resources_input, money_input):
    print(f"Water: {resources_input["water"]}ml")
    print(f"Milk: {resources_input["milk"]}ml")
    print(f"Coffee: {resources_input["coffee"]}g")
    print(f"Money: ${money_input}")


def check_resources(resources_input, coffe_type):
    check = True
    if resources_input["water"] < MENU[coffe_type]["ingredients"]["water"]:
        check = False
    if not coffe_type == "espresso":
        if resources_input["milk"] < MENU[coffe_type]["ingredients"]["milk"]:
            check = False
    if resources_input["coffee"] < MENU[coffe_type]["ingredients"]["coffee"]:
        check = False
    return check


def user_total(quarters, dimes, nickles, pennies):
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01


def check_transaction(user_input, coffee_type):
    return user_input >= MENU[coffee_type]["cost"]


on = True
while on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        on = False
    elif user_choice == "report":
        print_report(resources, money)
    else:
        if check_resources(resources, user_choice):
            print("Please insert coins.")
            quarters = int(input("How many quarters? :"))
            dimes = int(input("How many dimes? :"))
            nickles = int(input("How many nickles? :"))
            pennies = int(input("How many pennies? :"))
            if check_transaction(user_total(quarters, dimes, nickles, pennies), user_choice):
                if user_total(quarters, dimes, nickles, pennies) > MENU[user_choice]["cost"]:
                    change = user_total(quarters, dimes, nickles, pennies) - MENU[user_choice]["cost"]
                    print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice}. Enjoy!")
                money += user_total(quarters, dimes, nickles, pennies)
                resources["water"] -= MENU[user_choice]["ingredients"]["water"]
                resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
                if not user_choice == "espresso":
                    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]

            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there are not enough resources")
