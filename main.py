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

def are_resources_sufficient(order_ingredients):
    """RETURNS TRUE WHEN ORDER CAN BE MADE"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough

def calculate_cost():
    """Returns the total of coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.10
    total += int(input("how many nickels?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is successful, or False with insufficient funds"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global money
        money += money_received - change
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy☕️!")


#TODO: 1. Prompt user by asking what would you like?.

# choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
# print(choice)

#TODO: 2. Turn off the coffee machine by entering off into the prompt.

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${round(money,2)}")
    elif choice in MENU:
        drink = MENU[choice]
        if are_resources_sufficient(drink["ingredients"]):
            payment = calculate_cost()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

    else:
        print("ERROR: NOT A VALID SELECTION. TRY AGAIN.")

#TODO 3: Print report.