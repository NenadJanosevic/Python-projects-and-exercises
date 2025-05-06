print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
Welcome to Treasure Island.''')

while True:
    player = input("You're at a crossroad. Where do you want to go?\nType 'left' or 'right':\n").lower()
    if player == "left":
        while True:
            player = input("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across:\n").lower()
            if player == "swim":
                print("You get attacked by an angry trout. Game Over.")
                exit()
            elif player == "wait":
                while True:
                    player = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow, and one blue. Which color do you choose?\n").lower()
                    if player == "red":
                        print("It's a room full of fire. Game Over.")
                        exit()
                    elif player == "yellow":
                        print("You found the treasure! You Win!")
                        exit()                   
                    elif player == "blue":
                        print("You enter a room of beasts. Game Over.")
                        exit()
                    else:
                        print("Invalid choice. Please choose 'red', 'yellow', or 'blue'.")
            else:
                print("Invalid choice. Please type 'wait' or 'swim'")

    elif player == "right":
        print("You fell into a hole. Game Over.")
        break
    else:
        print("Try agen")
    