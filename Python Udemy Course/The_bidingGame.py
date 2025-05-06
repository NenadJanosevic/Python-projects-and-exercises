from os import system

Name_bid = {}
def game():
    while True:
        Name = input("What is your name?:").lower()
        bid = int(input("What is your bid?:$ "))
        Name_bid.update({Name:bid})
        question = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
        if question == "yes":
            system('cls')
            continue
        elif question == "no":
            winner = max(Name_bid,key=Name_bid.get)
            print(f"The winner is:{winner} whit a bid of {Name_bid[winner]}")
            break
        else:
            print("Wrong input!")    

game()       
