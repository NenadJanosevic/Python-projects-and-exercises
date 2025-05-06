import random

low = 1
highe = 100
gues = 1
player = input("Think of a number press . y/n to play:")
 

while True:
    pc_gues = random.randint(low,highe)
    pc_try = input(f"Is your number {pc_gues}? If not is it higer or lower(l ,h or c for correct)?")
    print(pc_try)
    if pc_try == "h":
        low = pc_gues + 1
        gues += 1
    elif pc_try == "l":
        highe = pc_gues - 1
        gues += 1
    elif pc_try == "c":
        print(f"Your number is {pc_gues} the pc guessed it in {gues}.Thanks for playing ")
        break
    else:
        print("Invalied input")



  
            
        
    




