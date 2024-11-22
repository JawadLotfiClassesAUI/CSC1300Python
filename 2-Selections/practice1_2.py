# Exercise 1.2: Write a program that asks the user to enter a number and will display its absolute value (positive equivalent) only if the number was negative.
# Prompt the user to enter a number and convert to float(real number)
number = float(input("Enter a number: "))
# Check if the number is negative
if number < 0:
    # If the number is negative, display its opposite
    print("The absolute value is:", -number)