# Initialize an empty list to store the numbers
numbers = []
positive_count = 0
negative_count = 0

# Indefinite loop to get numbers from the user until they decide to quit
while True:
    # Prompt the user to enter a number or 'q' to quit
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    # Add the entered number to the list using the append method
    number = float(user_input)
    numbers.append(number)
    # Increment the positive or negative counter
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

# Display the average, and counts of positive and negative numbers
if len(numbers) > 0:
    print("The average of the numbers is:", sum(numbers) / len(numbers))
    print("The count of positive numbers is:", positive_count)
    print("The count of negative numbers is:", negative_count)
else:
    print("No numbers were entered.")
