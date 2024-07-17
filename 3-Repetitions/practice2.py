# 2.1: Calculate class average, number of passing grades, and number of failing grades
grades = []
passing_grades = 0
failing_grades = 0
total_grades = 0

while True:
    grade = float(input("Enter a grade (enter 1 to stop): "))
    if grade == 1:
        break
    grades.append(grade)
    total_grades += grade
    if grade >= 60:
        passing_grades += 1
    else:
        failing_grades += 1

class_average = total_grades / len(grades)

print("Class Average:", class_average)
print("Number of Passing Grades:", passing_grades)
print("Number of Failing Grades:", failing_grades)

# 2.2: Count the number of odd and even numbers
odd_numbers = 0
even_numbers = 0

for i in range(10):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print("Number of Odd Numbers:", odd_numbers)
print("Number of Even Numbers:", even_numbers)

# 2.3: Guessing game
winning_number = 42
guesses = 0

while True:
    guess = int(input("Guess a number: "))
    guesses += 1
    if guess == winning_number:
        break
    elif guess < winning_number:
        print("Too low!")
    else:
        print("Too high!")

print("Congratulations! You found the winning number in", guesses, "guesses.")

# 2.4: Population growth
population = 9870
target_population = int(input("Enter the target population: "))

while population < target_population:
    print("Population:", population)
    population += population * 0.1

print("Population reached the target:", population)