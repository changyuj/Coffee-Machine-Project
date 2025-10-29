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

#Turn the machine on (start the while loop)
is_on = True 

#Check if there are enough ingredients to make the drink
def check_resource_available(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item} to make the drink.")
            return False
    return True

#Returns the total of money received
def process_money():
    print("Please insert your coins.")
    coin_check = True
    while coin_check:
        try:
            user_input = int(input("how many quarters? ")) * 0.25
            total = user_input
            coin_check = False
        except ValueError:
            print("Pleae enter numbers only.")
    coin_check = True
    while coin_check:
        try:
            user_input = int(input("how many dimes? ")) * 0.1
            total += user_input
            coin_check = False
        except ValueError:
            print("Pleae enter numbers only.")

    coin_check = True
    while coin_check:
        try:
            user_input = int(input("how many nickles? ")) * 0.05
            total += user_input
            coin_check = False
        except ValueError:
            print("Pleae enter numbers only.")
    coin_check = True
    while coin_check:
        try:
            user_input = int(input("how many pennies? ")) * 0.01
            total += user_input
            coin_check = False
        except ValueError:
            print("Pleae enter numbers only.")

    '''total = int(input("how many quarters? ")) * 0.25'''
    '''total += int(input("how many dimes? ")) * 0.1'''
    '''total += int(input("how many nickles? ")) * 0.05'''
    '''total += int(input("how many pennies? ")) * 0.01'''
    return total

#check if money received is enough to make the drink, if enough then calculate the change and add the profit
def check_transaction(payment_received, drink_cost):
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"You paid ${payment_received}, but the drink cost ${drink_cost}.")
        return False

def make_coffee(drink_ordered, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_ordered} ☕. Enjoy!")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    choice = choice.lower() # lowercase all letter
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Cofee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in ("espresso", "latte", "cappuccino"):
        drink = MENU[choice]
        if check_resource_available(drink["ingredients"]):
            payment = process_money()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Please check your spelling, thank you!")