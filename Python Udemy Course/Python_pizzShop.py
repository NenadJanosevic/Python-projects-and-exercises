print("Welcom to python pizza shop")
bill = 0
size = input("May i take your order,would you like a S(small)(15$),M(medium)(20$),L(large)(25$) pizza: ").lower()
if size == "s":
    bill += 15 
elif size == "m": 
    bill += 20
else:
    bill += 25  
    
pepperoni = input("Would you like to add pepperoni (2$) (Y or N): ").lower()
if pepperoni == "y":
    bill += 2

extra_cheese = input("Would you like to add extra cheese(1$)(Y or N): ").lower()
if extra_cheese == "y":
    bill += 1

print(f"Your finale bill is: {bill}")
