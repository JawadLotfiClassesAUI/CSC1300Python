# We will use the random library to generate a random number
from random import randint

winning_number = randint(1,100)

# Initialize our counter of guesses to 0
number_of_guesses = 0

guess = int(input("Guess a number: "))
while guess != winning_number:
    number_of_guesses += 1
    if guess < winning_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess a number: "))

print("Congratulations! You found the winning number in", number_of_guesses, "guesses.")