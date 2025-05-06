import random
import os

players_cards = []
pc_cards = []
cards = [11,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("Welcome to BlackJack/21")

def curent_Result(number):
    return sum(number)

def player():
    players_cards.clear()
    pc_cards.clear()
    loop = True
    start = input("Pres 'y' to get your cards or 'n' to exit: ").lower()
    Npc()
    print("\n"*3)
    if start == 'y':
        players_cards.append(random.choice(cards))
        players_cards.append(random.choice(cards))
        if curent_Result(players_cards)  == 21:
            print("BlackJack baby!!!😎😎😎 You win!!!")
        print(f"Your cards: {players_cards}, current score: {curent_Result(players_cards)} ")
    else:
        print("Thanks for playing BlackJack with us.")
        exit()
    while loop:
            player = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if player == "y":
                players_cards.append(random.choice(cards))
                print(f"Your cards: {players_cards}, current score: {curent_Result(players_cards)}")
            elif player == 'n':
                loop = False
    while True:
        if 11 in players_cards and sum(players_cards) > 21:
            players_cards.remove(11)
            players_cards.append(1)
        else:
            break
    print(f"Your cards: {players_cards},final score: {curent_Result(players_cards)}")
    print("\n"*3)
    print(f"Computer's final hand: {pc_cards}, final score: {curent_Result(pc_cards)}")

def Npc():
    pc_cards.append(random.choice(cards))
    print(f"Computer's first card:{pc_cards} ")
    while True:
        if sum(pc_cards) < 18:
            pc_cards.append(random.choice(cards))
        else:
            break
    while True:
        if 11 in pc_cards and sum(pc_cards) > 21:
            pc_cards.remove(11)
            pc_cards.append(1)
        else:
            break

def winner():
    #curent_Result(players_cards) curent_Result(pc_cards) 😁, 😤, 🙃
    if curent_Result(players_cards)  == 21:
        print("BlackJack baby!!!😎😎😎You win!!!")
    elif curent_Result(players_cards) == curent_Result(pc_cards):
        print("Its a draw 🙃")
    elif curent_Result(players_cards) > 21 and curent_Result(pc_cards) > 21:
        print("Its a draw 🙃")
    elif curent_Result(pc_cards) > 21:
        print("You win 😁")
    elif curent_Result(players_cards) > 21:
        print("You lose 😤")
    elif curent_Result(players_cards) > curent_Result(pc_cards):
        print("You win 😁")
    else:
        print("You Lose 😤")

def rules():
    while True:
        user = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
        os.system('cls')
        if user == 'y':
            player()
            print("\n"*3)
            winner()
        elif user == 'n':
            print("Thank you for playing BlackJack with us.")
            break
        else:
            print("Invalid input pleas type 'y' or 'n' ")
            continue
rules()