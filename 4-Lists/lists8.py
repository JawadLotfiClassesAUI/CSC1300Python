# Initialize an empty list to store the words
words = []

# Loop to get words from the user until they decide to quit
while True:
    # Ask the user to enter a word or 'q' to quit
    user_input = input("Enter a word (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    # Add the entered word to the list
    words.append(user_input)

# Sort the list based on the length of the words using a traditional method
for i in range(len(words)):
    for j in range(0, len(words) - i - 1):
        if len(words[j]) > len(words[j + 1]):
            # Swap the words if the current word is longer than the next word
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp

# Print the sorted list
print("Sorted list based on length:", words)
