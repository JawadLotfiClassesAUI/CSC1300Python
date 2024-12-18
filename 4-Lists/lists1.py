# Initialize an empty list to store the numbers
numbers = []

# Loop 5 times to get 5 numbers from the user
for i in range(5):
    # Prompt the user to enter a number
    number = float(input("Enter a number: "))
    # Add the entered number to the list using the append method
    numbers.append(number)

# Display the list of numbers
print("The list of numbers is:", numbers)