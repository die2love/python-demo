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
    "money": 0
}
def get_resoucer(favor):
    if favor == "espresso":
        if resources["water"] <= MENU[favor]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        else:
            if resources["coffee"] <= MENU[favor]["ingredients"]["coffee"]:
                print("Sorry there is not enough Coffee.")
            else:
                coins()
    else:
        if resources["water"] <= MENU[favor]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        else:
            if resources["coffee"] <=MENU[favor]["ingredients"]["coffee"]:
                print("Sorry there is not enough Coffee.")
            else:
                if resources["milk"] <= MENU[favor]["ingredients"]["milk"]:
                    print("Sorry there is not enough Milk.")
                else:
                    coins()

def coins():
    print("Please insert coins.")
    no_of_quarters = int(input("how many quarters?: "))
    no_of_dimes = int(input("how many dimes?: "))
    no_of_nickles =int(input("how many dimes?: "))
    no_of_pennies = int(input("how many pennies?: "))
    process_coin(no_of_quarters, no_of_dimes, no_of_nickles, no_of_pennies,order)

def process_coin(no_of_quarters, no_of_dimes, no_of_nickles, no_of_pennies,order):
    total_quartes = 0.25*no_of_quarters
    total_dimes = 0.10*no_of_dimes
    total_nickles = 0.05*no_of_nickles
    total_pennies = 0.01*no_of_pennies
    total = total_quartes + total_dimes + total_nickles + total_pennies
    if total >= MENU[order]["cost"]:
        if total - MENU[order]["cost"] !=0:
            bal = round(total - MENU[order]["cost"],2)
            print(f'Here is ${bal} in change.')
            print(f'Here is your {order} ☕️. Enjoy!')
            make_coffee_update(order)
        else:
            print(f'Here is your {order} ☕️. Enjoy!')
            make_coffee_update(order)
    else:
        print("Sorry that's not enough money. Money refunded")

def make_coffee_update(order):
    if order == "espresso":
        resources.update({"water": (300 -MENU[order]["ingredients"]["water"]),"milk": 200,"coffee": (100 - MENU[order]["ingredients"]["coffee"])})
        money(order)
    elif order == "latte":
        resources.update({"water": (300 - MENU[order]["ingredients"]["water"]), "milk": (200-MENU[order]["ingredients"]["milk"]),
                          "coffee": (100 - MENU[order]["ingredients"]["coffee"])})
        money(order)
    elif order == "cappuccino":
        resources.update({"water": (300 - MENU[order]["ingredients"]["water"]), "milk": (200-MENU[order]["ingredients"]["milk"]),
                          "coffee": (100 - MENU[order]["ingredients"]["coffee"])})
        money(order)

def money(order):
    get_current_amount = resources["money"]
    get_current_amount = get_current_amount + MENU[order]["cost"]
    resources.update({"money": get_current_amount})

# TODO 1 : Prompt user by asking “ What would you like
# TODO 2: Turn off the Coffee Machine by entering “ off ” to the promptes
# TODO 3: Print report
# TODO 4: Check resources sufficient
# TODO 5: Process coins
# TODO 6: Check transaction successful
# TODO 7: Make Coffee

coffee_machine_on = True
while coffee_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    resources_bal = [resources["water"], resources["coffee"], resources["milk"]]
    if order == "off":
        exit()
    elif order == "report":
        print(f'Water: {resources["water"]} ml \nmilk: {resources["milk"]} ml \ncoffee: {resources["coffee"]} ml \nmoney: {resources["money"]}')
    elif order == "espresso":
        get_resoucer(order)
    elif order == "latte":
        get_resoucer(order)
    elif order == "cappuccino":
        get_resoucer(order)





