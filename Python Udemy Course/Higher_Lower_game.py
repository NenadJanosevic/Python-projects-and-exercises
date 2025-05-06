import random
from Game_data import data
from art import art_pic



def randmom_exclusive_num(exclude):
    index = random.randint(0,10)
    while index ==  exclude:
        index = random.randint(0,10)
    return index
    
a = random.randint(0,10)
b = randmom_exclusive_num(a)
curent_score = 0
# print(f"{data[0]['name']}, {data[0]['description']}, {data[0]['country']} ")
while True:
    print(f"Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}")
    print(f"Compare B: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}")
    print("\n")
    player = (input("Who has more followers? Type 'A' or 'B':")).lower()
    if data[a]['follower count'] > data[b]['follower count'] and player == 'a':
        curent_score += 1
        print(f"You're right! Current score: {curent_score}")
        b = randmom_exclusive_num(a)
    elif data[a]['follower count'] < data[b]['follower count'] and player == 'b':
        a = b
        b = randmom_exclusive_num(a)
        curent_score += 1
        print(f"You're right! Current score: {curent_score}") 
    else:
        print(f"Sorry, that's wrong. {curent_score}")
        break
