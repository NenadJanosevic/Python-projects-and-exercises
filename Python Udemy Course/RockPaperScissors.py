import random


print('Welcome to rock,paper,scissors')
comands = ['rock','paper','scissors']
player_count = 0
computer_count = 0

while True:
    player_1 = input("Press (R)for rock,(P)for paper (S)for  scissors:\n").strip().upper()
    computer = random.choice(comands)
    if player_1 == 'R' and computer == 'paper':
        print(f"Computer chose:\n {computer}")
        print("You lose")
        computer_count += 1    
    elif player_1 == "P" and computer == 'rock':
        print(f"Computer chose:\n {computer}")
        print("You win")
        player_count += 1
    elif player_1 == 'S' and computer == "rock":
        print(f"Computer chose:\n {computer}")
        print("You lose")
        computer_count += 1
    elif player_1 == "R" and computer == 'scissors':
        print(f"Computer chose:\n {computer}")
        print("You win")
        player_count += 1 
    elif player_1 == "P" and computer == 'scissors':
        print(f"Computer chose:\n {computer}")
        print("You lose")
        computer_count += 1 
    elif player_1 == "S" and computer == 'paper':
        print(f"Computer chose:\n {computer}")
        print("You win")
        player_count += 1
    elif player_1 == computer:
        print(f"Computer chose:\n {computer}")
        print("Its a draw!")   
    elif player_1 == "E":
        print(f"Your scoer is: {player_count}\nComputer score is: {computer_count} ")
        break
    else:
        print("Wrong input")