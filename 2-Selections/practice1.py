# Exercise 1.1: Write a program that asks the user to enter a password and will greet the user only if the password is equal to "csc1300"

# Prompt the user to enter a password
password = input("Enter a password: ")

# Check if the entered password is equal to "csc1300"
if password == "csc1300":
    # If the password is correct, greet the user
    print("Hello, user!")


# Exercise 1.2: Write a program that asks the user to enter a number and will display its absolute value (positive equivalent) only if the number was negative.

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is negative
if number < 0:
    # If the number is negative, calculate its absolute value
    absolute_value = abs(number)
    # Display the absolute value
    print("The absolute value is:", absolute_value)


# Exercise 1.3: Write a program that asks the user to enter the side of a square and that will display the area only if the side is greater than zero.

# Prompt the user to enter the side of a square
side = float(input("Enter the side of a square: "))

# Check if the side is greater than zero
if side > 0:
    # If the side is greater than zero, calculate the area of the square
    area = side ** 2
    # Display the area of the square
    print("The area of the square is:", area)