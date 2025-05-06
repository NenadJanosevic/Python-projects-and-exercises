from wordplay import Logo

print(Logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text,shif_amount):
    cipher = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher += letter
        else:
            shift_number = alphabet.index(letter) + shif_amount
            shift_number %= len(alphabet)
            cipher += alphabet[shift_number]
    print(f"Here is the encode word: {cipher}")

def decode(original_text,shift_amount):
    cipher = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher += letter
        else:
            shift_number2 = alphabet.index(letter) - shift_amount
            cipher += alphabet[shift_number2]

    print(f"Here is the decode word: {cipher}")

def caser():
    while True:
        directions = input('''Type 'encode' to encode ,type 'decode' to decrypt:\n''' ).lower()
        text = input("Type your message:\n").lower()
        shift = int(input("type the shif number:\n"))
        if directions == "encode":
            encrypt(original_text= text,shif_amount=shift)
        elif directions == "decode":
            decode(original_text= text,shift_amount=shift)
        user = input("Would you like to try agen:")
        if user == 'yes':
                continue
        elif user == 'no':
                break

       

caser()
    
