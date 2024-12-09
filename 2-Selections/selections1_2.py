# Prompt the user to enter a number and convert to float(real number)
number = float(input("Enter a number: "))

# Check if the number is negative
if number < 0:
    # If the number is negative, display its opposite
    print("The absolute value is:", -number)