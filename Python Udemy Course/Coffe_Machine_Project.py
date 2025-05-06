menu = {
    "espresso":{
        "ingridiants":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingridiants":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingridiants":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
       }
}

resurces = {
    "water":300,
    "milk":200,
    "coffee":100,
}
money = 0
#print(menu["espresso"]["ingridiants"]["water"])
def Maintenc(user):
    if user == "report":
        for k,v in resurces.items():
            print(f"{k}: {v}")
            print(f"Money: {money}")
    elif user == "off":
        print("coffe Machine turning off")
        exit()
def customer_order(user):

    if user == "espresso":
        if resurces["water"] < 50:
            print("Sorry there is not enough water.")
            exit()
        if resurces["coffee"] < 18:
            print("Sorry there is not enough coffee.")
            exit()
        resurces["water"] -= 50
        resurces["coffee"] -= 18
    if user == "latte":
        if resurces["water"] < 200:
            print("Sorry there is not enough water.")
            exit()
        if resurces["coffee"] < 24:
            print("Sorry there is not enough coffee.")
            exit()
        if resurces["milk"] < 150:
            print("Sorry there is not enough Milk.")
            exit()
        resurces["water"] -= 200
        resurces["coffee"] -= 24
        resurces["milk"] -= 150
    if user == "cappuccino":
        if resurces["water"] < 250:
            print("Sorry there is not enough water.")
            exit()
        if resurces["coffee"] < 24:
            print("Sorry there is not enough coffee.")
            exit()
        if resurces["milk"] < 100:
            print("Sorry there is not enough Milk.")
            exit()
        resurces["water"] -= 250
        resurces["coffee"] -= 24
        resurces["milk"] -= 100

def customer_pay(user):
    global money
    quarters, dimes, nickles, pennies = 0.25, 0.10, 0.05, 0.01
    # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Pleas insert coins.")
    quarters_input = float(input("How many quarters:")) * quarters
    dimes_input = float(input("How many dimes:")) * dimes
    nickles_input = float(input("How many nickles:")) * nickles
    pennies_input = float(input("How many pennies:")) * pennies
    customer_mony = quarters_input + dimes_input + nickles_input + pennies_input
    #espresso/latte/cappuccino
    if user == "espresso":
        if customer_mony > menu["espresso"]["cost"]:
            x = customer_mony - menu["espresso"]["cost"]
            print(f"Here is {x} in change ")
            print("Here is your espresso ☕ enjoy")
            money += menu["espresso"]["cost"]
        else:
            print("Poor basterd")
    if user == "latte":
        if customer_mony > menu["latte"]["cost"]:
            x = customer_mony - menu["latte"]["cost"]
            print(f"Here is {x} in change ")
            print("Here is your latte ☕ enjoy")
            money += menu["latte"]["cost"]
        else:
            print("Poor basterd")
    if user == "cappuccino":
        if customer_mony > menu["cappuccino"]["cost"]:
            x = customer_mony - menu["cappuccino"]["cost"]
            print(f"Here is {x} in change ")
            print("Here is your cappuccino ☕ enjoy")
            money += menu["cappuccino"]["cost"]
        else:
            print("Poor basterd")

def coffe_machine():
    while True:
        customer = input("What would you like? (espresso/latte/cappuccino):").lower()
        Maintenc(customer)
        if customer == "espresso" or customer == "latte" or customer == "cappuccino":
            customer_order(customer)
            customer_pay(customer)
            
coffe_machine()



   

    
