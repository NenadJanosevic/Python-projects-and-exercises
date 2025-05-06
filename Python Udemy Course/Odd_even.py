while True:
    user = input("Type a number to see if its odd or even(Type e to  exit): ").lower()
    if user == 'e':
        break
    try:
        number = float(user)
        if number % 2 == 0:
            print(f"You'r number {number} is even.")
        else:
            print(f"You'r number {number} is odd.")
    except ValueError:
        print("Wrong input pleas try agen with a number.")
