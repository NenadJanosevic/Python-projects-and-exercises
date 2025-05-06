import random
from HangMan_Art import a

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | |_| | | | | |_| | | | | | | |_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

list = []
list_words = ["apple"]
word_to_gues = random.choice(list_words)
word = ""
letters_entered = ""
guess_left = 6
correct_letter = []

for i in range(len(word_to_gues)):
    word += '_'
print("Word to gues: " + word )
print(f"You have {guess_left} left, letters enterd {letters_entered} ")
while True:
    guess = input("Welcome to Hangman Enter a letter to start: ").lower() 
    display = ""
    if guess in letters_entered:
        print(f"You have alredy entered that letter.Letters entered: {letters_entered}")   
    for letter in word_to_gues:
        if letter == guess:
            display += guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    if "_" not in display:
        print(f"Congratulation you win")
        break
    if guess not in word_to_gues:
        guess_left -= 1
        letters_entered += guess
    else:
        letters_entered += guess  
    print(f"You have {guess_left} left, letters enterd: {letters_entered} ")
    print(display)
    if guess_left == 0:
        print(f"You lose the word was {word_to_gues}")
        break
    
    print(a[guess_left])