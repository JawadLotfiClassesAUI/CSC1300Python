# Exercise 1.1: Write a program that asks the user to enter a password and will greet the user only if the password is equal to "csc1300"
# Prompt the user to enter a password
password = input("Enter a password: ")
# Check if the entered password is equal to "csc1300"
if password == "csc1300":
    # If the password is correct, greet the user
    print("Hello, user!")