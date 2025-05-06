import Number_Guessing_Game_assci_Art
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100 try to gues.")

score = 0 
x = random.randint(1,100)
print(f"Psst the number is {x} don't tell anyone.")

def difficulty():
    global score
    level_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level_difficulty == 'easy':
        score += 10
    else:
        score += 5

def player():
    global score
    while score > 0:
        player = int(input("Enter a number:"))
        score -= 1
        if player == x:
            print(f"You got it! The answer was {x}.")
            score -= 1
            break
        if player > x:
            print(f"You have {score} attempts remaining to guess the number.")
            score -= 1
            print("Too high")
        elif player < x:
            print(f"You have {score} attempts remaining to guess the number.")
            score -= 1
            print("Too low")
    print("You Fail")
difficulty()
player()

    




