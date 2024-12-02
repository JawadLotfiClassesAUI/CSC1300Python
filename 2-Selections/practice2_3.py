# Exercise 2.3: Even or Odd
number = int(input("Enter a number: "))  # Ask the user to enter a number

if number % 2 == 0:  # Check if the remainder of the division by 2 is 0 (after dividing by 2, there is no remainder)
    print("The number is even")
else:
    print("The number is odd")