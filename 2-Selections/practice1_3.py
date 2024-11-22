# Exercise 1.3: Write a program that asks the user to enter the side of a square and that will display the area only if the side is greater than zero.
# Prompt the user to enter the side of a square
side = float(input("Enter the side of a square: "))
# Check if the side is greater than zero
if side > 0:
    # If the side is greater than zero, calculate the area of the square
    area = side ** 2
    # Display the area of the square
    print("The area of the square is:", area)