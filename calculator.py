import math_tools as mt

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
operation = str(input("Which operation do you want to perform? Choose from addition, subtraction, multiplication, and division:"))

def calculator(a, b, operation):
    if operation == "addition":
        return mt.add(a,b)
    elif operation == "subtraction":
        return mt.subtract(a,b)
    elif operation == "multiplication":
        return mt.multiply(a,b)   
    elif operation == "division":
        return mt.divide(a,b)

print(calculator(a,b,operation))
