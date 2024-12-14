from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine=MoneyMachine()
coffemaker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffemaker.report()
        machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffemaker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                coffemaker.make_coffee(drink)
