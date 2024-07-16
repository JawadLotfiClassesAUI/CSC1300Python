# Exercise 2.1: Eligibility for Exchange Program
credits = int(input("Enter your credits: "))  # Ask the student to enter their credits
if credits >= 45:  # Check if the credits are greater than or equal to 45
    print("You are eligible for the exchange program")  # Display the eligibility message
else:
    print("You are not eligible for the exchange program")  # Display the ineligibility message

# Exercise 2.2: Absolute Value
number = int(input("Enter a number: "))  # Ask the user to enter a number
if number < 0:  # Check if the number is negative
    number = -number  # Convert the negative number into positive
print("The absolute value of the number is:", number)  # Display the absolute value of the number

# Exercise 2.3: Even or Odd
number = int(input("Enter a number: "))  # Ask the user to enter a number
if number % 2 == 0:  # Check if the number is divisible by 2
    print("The number is even")  # Display that the number is even
else:
    print("The number is odd")  # Display that the number is odd