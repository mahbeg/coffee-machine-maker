from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"what would you like? {option}? ")
    if choice == "report":
        print(coffee_maker.report())
        print(money.report())
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)






