from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
Resurces = CoffeeMaker()
Payment = MoneyMachine()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("Turning off.")
        break
    elif choice == "report":
        Resurces.report()
        Payment.report()
    else:
        drink = menu.find_drink(choice)
        if Resurces.is_resource_sufficient(drink) and Payment.make_payment(drink.cost):
            Resurces.make_coffee(drink)

