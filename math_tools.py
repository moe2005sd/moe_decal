def add(a,b): #returns the sum of a and b
    return a + b
    
def substract(a,b): #returns the difference between a and b
    return a - b

def multiply(a,b): #returns the product of a and b
    return a * b

def divide(a,b): #returns the quotient of a divided by b (handles division by zero)
    if b == 0:
        return "Error: division by zero!"
    else:
        return a / b
