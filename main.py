import time

from machine import MENU
from machine import resources


def coffee_menu(order):
    coffee_menu = {"a" : "espresso", "b" : "latte", "c" : "cappuccino"}
    return coffee_menu[order]

def fill_up():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def check_ingredients(coffee_name):
    coffee_water = MENU[coffee_name]["ingredients"]["water"]
    coffee_milk = MENU[coffee_name]["ingredients"]["milk"]
    coffee_coffee = MENU[coffee_name]["ingredients"]["coffee"]
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]
    if machine_water - coffee_water < 0:
        print("Sorry water is unenought")
        return False
    elif machine_milk - coffee_milk < 0:
        print("Sorry milk is unenought")
        return False

    elif machine_coffee - coffee_coffee < 0:
        print("Sorry coffee is unenought")
        return False
    else:
        return True


def calculate(quarters, dimes, nickles, pennies, price):
    quarter_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    get_money = quarter_total + dimes_total + nickles_total + pennies_total
    if get_money == price:
        print("Thank you. Please wait a second")
        return True
    elif get_money > price:
        change = get_money - price
        print(f"Thank you. Please wait a second, Here is your change : $ {change}")
        return True
    else:
        print("Sorry Money is unenought")
        return False


def make_coffee(coffee_name):
    coffee_water = MENU[coffee_name]["ingredients"]["water"]
    coffee_milk = MENU[coffee_name]["ingredients"]["milk"]
    coffee_coffee = MENU[coffee_name]["ingredients"]["coffee"]
    resources["water"] = resources["water"] - coffee_water
    resources["milk"] = resources["milk"] - coffee_milk
    resources["coffee"] = resources["coffee"] - coffee_coffee



total_money = 0
while True:
    order = input(""" Check machine type 'c', Order type 'o',
    Fill ingredients type 'f', Out type 'q', Check Money type 'cm'
    : """).lower()
    if order == 'c':
        print(resources)
        continue
    elif order == "f":
        fill_up()
        continue
    elif order == "cm":
        print(total_money)
        continue
    elif order == 'o':
        coffee = input("""Which coffee do you want ? Please type 'A', 'B' or 'C'
        'A' espresso
        'B' latte
        'C' cappuccino
        : """).lower()
        coffee_name = coffee_menu(coffee)
        check = check_ingredients(coffee_name)
        if check != True:
            print("Sorry, Please select other coffee.")
            continue
    print("Please inser coin")
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes : "))
    nickles = int(input("How many nickles : "))
    pennies = int(input("How many pennies : "))
    price = MENU[coffee_name]["cost"]
    calculation = calculate(quarters, dimes, nickles, pennies, price)
    if calculation != True:
        continue
    print("Prepare for you now. Please wait a second")
    make_coffee(coffee_name)
    print(f'Your {coffee_name} is OK. Thank you. Have a good day')
    total_money += price


#TODO check ingredients


#TODO inser coin



