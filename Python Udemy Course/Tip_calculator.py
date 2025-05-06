print('Welcom to the tip calculator')
user_1 = float(input("What was the total bill: "))
tip = int(input("How much tip would you like to give(5,10,15): "))
user_2 = float(input("How many people have to split the bill: "))

tip_calculator = (user_1 * tip / 100)
calculator = (user_1 + tip_calculator) / user_2
x = round(calculator,2)

print(f"Each person sould pay {x}")

