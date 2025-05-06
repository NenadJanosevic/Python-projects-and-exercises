import random
import string

keyboard_symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+','[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?',' ']
numbers = ['1','2','3','4','5','6','7','8','9']
lowercase_letters = string.ascii_lowercase
pasword1 = []


 
user = int(input("Welcome to the PyPassword Generator!\nHow many letters would you like in your password?\n"))
for i in range(user):
    pasword1 += random.choice(lowercase_letters)
user1 = int(input("How many symbols would you like?\n"))
for i in range(user1):
    pasword1 += random.choice(keyboard_symbols)
user2 = int(input("How many numbers would you like?\n"))
for i in range(user2):
    pasword1 += random.choice(numbers)

print(pasword1)
random.shuffle(pasword1)
print(pasword1)
print(f"Your password is:\n{pasword1}") 
    

