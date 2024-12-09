# We ask the user for 2 numbers
number1 = float(input("Enter a number:"))
number2 = float(input("Enter another number:"))

# Using the integer division // we can get the quotient
quotient = number1 // number2

# using the modulo % we can get the remainder
remainder = number1 % number2

print(f"The divison of {number1} by {number2} is equal to {quotient} with a remainder of {remainder}")