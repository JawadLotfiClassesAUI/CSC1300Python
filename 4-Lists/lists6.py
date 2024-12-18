# Initialize an empty list to store the numbers
numbers = []

# Indefinite loop to get numbers from the user until they decide to quit
while True:
    # Prompt the user to enter a number or 'q' to quit
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    # Add the entered number to the list using the append method
    number = float(user_input)
    numbers.append(number)

# Ask the user for a value to check its position in the list
value_to_check = float(input("Enter a value to check its position in the list: "))

# Check if the value is in the list, print its position, and remove it
if value_to_check in numbers:
    position = numbers.index(value_to_check)
    print(f"The value {value_to_check} is found at position: {position} and will be removed from the list.")
    numbers.pop(position)
else:
    print(f"The value {value_to_check} is not in the list.")
