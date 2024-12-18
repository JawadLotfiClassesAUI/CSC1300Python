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

# Display the highest, lowest values, and sum of the numbers
if len(numbers) > 0:
    print("The highest number is:", max(numbers))
    print("The lowest number is:", min(numbers))
    print("The sum of the numbers is:", sum(numbers))
else:
    print("No numbers were entered.")