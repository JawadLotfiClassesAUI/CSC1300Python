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

# Sort the list
numbers.sort()

# Display the sorted list
print("Sorted list:", numbers)

# Ask the user for a new number to insert into the sorted list
new_number = float(input("Enter a new number to insert into the sorted list: "))

# Insert the new number at the right position
for index in range(len(numbers)):
    if new_number < numbers[index]:
        numbers.insert(index, new_number)
        break
else:
    numbers.append(new_number)

# Display the updated list
print("Updated list:", numbers)
