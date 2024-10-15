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


def current_resources(resources, money):
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: {money}$")


def check(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True

def sum_coins():
    penny = float(input("Pennies: "))
    nickle = float(input("Nickles: "))
    dime = float(input("Dimes: "))
    quarter = float(input("Quarters: "))
    return penny * 0.01 + nickle * 0.05 + dime * 0.10 + quarter * 0.25


def prepare_drink(drink, cost, resources):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy! ☕️")
    return cost


def coffe_machine():
    money = 0
    is_working = True
    while is_working:
        order = input("What would you like? (espresso/latte/cappuccino):")
        if order == 'off':
            is_working = False
        elif order == 'report':
            current_resources(resources, money)
        elif order in MENU:
            if check(order):
                price = MENU[order]['cost']
                print(f"Price is {price}$. Please, insert coins")
                sum = sum_coins()
                if sum < price:
                    print("Sorry that's not enough money. Money refunded.")
                elif sum >= price:
                    money += prepare_drink(order, price, resources)
                    if sum > price:
                        print(f"Here is ${round((sum - price), 2)} dollars in change.")
        else:
            print("Wrong order. Try again")


coffe_machine()
