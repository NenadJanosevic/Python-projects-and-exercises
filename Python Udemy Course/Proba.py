    # travel = {
    #     "Franc":["Paris", "Lille","Dijon" ],
    #     "Germany":["Stutgard","berlin"]}

    # print(travel["Franc"][1])

    # nested_list = ["A","B",["C","D"]]

    # print(nested_list[2][0])

# travel = {
#         "Franc":{
#             'cities_visited':["Paris", "Lille","Dijon" ],
#             "total visited":12
#         },
#         "Germany":{
#             'cities_visited':["Stutgard","berlin","Hamburg"],
#             "total visited":15
#         },
# }

# print(travel["Franc"]["total visited"])

# name_bid = {}

# while True:
#     name = input("Safari:")
#     num = int(input("number:"))
#     name_bid.update({name:num})
#     print(name_bid)

# from os import system
# def acution_winner(bidding_dictonary):
#     highest = 0
#     winner = ""
#     for bider in bidding_dictonary:
#         bid_amaount = bidding_dictonary[bider]
#         if bid_amaount > highest:
#             highest = bid_amaount
#             winner = bider
#     print(f"The winner is:{winner} whit a bid of {highest}")

# Name_bid = {}
# def game():
#     while True:
#         Name = input("What is your name?:").lower()
#         bid = int(input("What is your bid?:$ "))
#         Name_bid.update({Name:bid})
#         question = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
#         if question == "yes":
#             system('cls')
#             continue
#         elif question == "no":
#             acution_winner(Name_bid)
            
#             break
#         else:
#             print("Wrong input!")    

# game()       

# x = (input("num: "))
# if  x.isdigit():
#     print("Gj")
# else:
#     x = "Wrong"
# def format_name(F_name,L_name):
#     if F_name == "" or L_name == "":
#         return "Not vlaid input."
    
#     formated_1 = F_name.title()
#     formated_2 = L_name.title()
#     return f"{formated_1} {formated_2}"

# print(format_name(input("What is your first name? "),input("What is your last name? ")

# def is_leap_year(year):
#     if year % 4 == 0 and year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     else:
#         return "Wrong input"

# print(is_leap_year(int(input("Enter a year:"))))
# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))

# def additiont(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiplay(x,y):
#     return x*y
# def divide(x,y):
#     return x/y

# operators = {"+":additiont,
#              "-":subtract,
#              "*":multiplay,
#              "/":divide
#              }

# for i in operators:
#     print(operators[i])

# print("😤")

# import random
# players_cards = []

# while True:
#     players_score = 0
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     numbers = 0
#     player = input("Press y to play:")
#     if player == "y":
#         players_cards.append(random.choice(cards))
#         for i in players_cards:
#                 players_score += i
#         print(f"Your cards: {players_cards}, current score: {players_score} ")
#     else:
#         break

# print(f"Your cards: {players_cards}, current score: {players_score}")

# list = [1,2,3,4]

# for num in range(len(list)):
#     num +=num
# print(num)
# import random

# cards = [11,5,7]
# pc_cards = []
# pc_cards.append(random.choice(cards))

# while True:
#     if sum(pc_cards) < 17:
#         pc_cards.append(random.choice(cards))
#     else:
#         print(pc_cards,sum(pc_cards))
#         break

# def is_prime(num):
#     conditions = [2,3,5,1]
#     if num in conditions:
#         return False
#     elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
#         return False
#     else:
#         return True
# x = 1   
# print(is_prime(x))


# def is_prime(num):
#     if num == 2:
#         return True
#     if num == 1:
#         return False
 
#     # Loop through all the numbers between 2 and the number
#     for i in range(2, num):
#         # Check if the number (num) can be divided by the potential prime number
#         if num % i == 0:
#             return False
 
#     # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
#     return True

# print(is_prime(124))

# def bar():
#     my_variable = 9
 
#     if 16 > 9:
#       my_variable = 16
 
#     print(my_variable)
 
# bar()

# def numf():
#   for i in range(1,21):
#     if i == 20:
#       print("Good job")
# numf()

# from random import randint

# dice_image = ['1', '2', '3', '4', '5', '6']
# dic_num = randint(0,5)

# print(dice_image[dic_num])

# year = int(input("What year were you born: "))

# if year > 1980 and year < 1994:
#   print("You are a millennial.")
# elif year >= 1994:
#   print("You are a Gen Z")

# try:
#     age = int(input("How old are you:"))
# except ValueError:
#     print("Wrong input.Need a number")
#     age = int(input("How old are you:"))
# if age > 18:
#     print(f'You can drive at age {age}.')

# wordPerPage = 0
# pages = int(input("Number of pages:"))
# s = int(input("Number of words per page:"))
# total = print(f"{pages} * {s} = {pages * s}")
# print(total)

# def is_leap(year):
#     if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
#         return True
#     else:
#         return False
    
# x = 2025   
# print(is_leap(x))

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)

# t = 20
# print(fizz_buzz(t))
# import random

# a = random.randint(0,10)

# def exlcusive():
#     b = random.randint(0,10)
#     if b == a:
#         b = random.randint(0,10)
#         return f"{b}"
#     else:
#         return f"{b}"

# b = exlcusive()
# print(a)

# pennies = 0.25 + 0.1 * 2 + 0.05 + 0.01 * 2

# print(pennies)

# resurces = {
#     "water":300,
#     "milk":200,
#     "coffee":100,
# }
# user = input("What would you like? (espresso/latte/cappuccino):").lower()
# def customer():
#     if user == "espresso":
#         resurces["water"]-= 50
#         print(resurces["water"])

# customer()

#quarters, dimes, nickles, pennies = 0.25, 0.10, 0.05, 0.01
# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#print("Pleas insert coins.")
# quarters_input = float(input("How many quarters:")) * quarters
# dimes_input = float(input("How many dimes:")) * dimes
# nickles_input = float(input("How many nickles:")) * nickles
# pennies_input = float(input("How many pennies:")) * pennies

# mony = quarters_input + dimes_input + nickles_input + pennies_input
# print(mony)

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

# print(menu["espresso"]["cost"],menu["latte"]["cost"],menu["cappuccino"]["cost"])

for items in menu:
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

# print(menu["espresso"]["cost"],menu["latte"]["cost"],menu["cappuccino"]["cost"])
resurces = {
    "water":300,
    "milk":200,
    "coffee":100,
    "cost": 2
}

def x(dic):
    for item in dic:
        if dic[item] >= resurces[item]:
            return False
    
    return False

x(menu["latte"])