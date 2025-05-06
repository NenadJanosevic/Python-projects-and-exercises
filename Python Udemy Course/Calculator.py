print("Calculator")

def additiont(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplay(x,y):
    return x*y
def divide(x,y):
    return x/y

def calculator():
    previus_num = 0
    while True:
        if previus_num == 0:
            Number_1 = input("Enter your first number:")
            if Number_1.isdigit():
                Number_1 = float(Number_1)
            elif Number_1 is not Number_1.isdigit():
                Number_1 = 0
        else:
            Number_1 == previus_num
        Number_2 = input("What is your second number: ")
        if Number_2.isdigit():
            Number_2 = float(Number_2)
        elif Number_2 is not Number_2.isdigit():
            Number_2 = 0
        operator = input("Operators:\n+\n-\n*\n/\n")
        if operator == '+':
            print(Number_1, "+" , Number_2 ,"=", additiont(x = Number_1, y = Number_2) )
            previus_num = additiont(x = Number_1, y = Number_2)
        elif operator == '-':
            print(Number_1, "-" , Number_2 ,"=", subtract(x = Number_1, y = Number_2) )
            previus_num = subtract(x = Number_1, y = Number_2)
        elif operator == '*':
            print(Number_1, "*" , Number_2 ,"=", multiplay(x = Number_1, y = Number_2) )
            previus_num = multiplay(x = Number_1, y = Number_2)
        elif operator == '/':
            print(Number_1, "/" , Number_2 ,"=", divide(x = Number_1, y = Number_2) )
            previus_num = divide(x = Number_1, y = Number_2)
        else:
            print(Number_1 ,"undefined ", Number_2 ,'=', 0.0 )
            previus_num = 0
        agen = input(f"Type 'y' to continue calculating with {previus_num},or type 'n' to start a new calculation or type'e' to exit:" ).lower()

        if agen == 'y':
            Number_1 = previus_num
        elif agen == 'n':
            previus_num = 0
        elif agen == 'e':
            print("Thank you for using our calculator.")
            break

calculator()
