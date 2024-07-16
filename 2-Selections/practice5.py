# Exercise 6.1: Feet to Meters Conversion
choice = input("Choose conversion type (1 for feet to meters, 2 for meters to feet): ")

if choice == "1":
    feet = float(input("Enter the length in feet: "))
    meters = feet * 0.3048
    print(f"{feet} feet is equal to {meters} meters.")
elif choice == "2":
    meters = float(input("Enter the length in meters: "))
    feet = meters / 0.3048
    print(f"{meters} meters is equal to {feet} feet.")
else:
    print("Invalid choice. Please choose 1 or 2.")

# Exercise 6.2: Grade Calculation
midterm_grade = float(input("Enter your midterm grade: "))
final_grade_needed = (70 - (midterm_grade * 0.5)) / 0.5

if final_grade_needed <= 100:
    print(f"You need {final_grade_needed} in the final to pass the class.")
else:
    print("Sorry, you will have to retake the class!")

# Exercise 6.3: Profit or Loss Calculation
income = float(input("Enter the income: "))
expenses = float(input("Enter the expenses: "))
profit = income - expenses

if profit > 0:
    print(f"Profit: {profit}")
else:
    print(f"Loss: {abs(profit)}")

# Exercise 6.4: Sorting Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f"The numbers in ascending order are: {num1}, {num2}, {num3}")
    else:
        print(f"The numbers in ascending order are: {num1}, {num3}, {num2}")
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f"The numbers in ascending order are: {num2}, {num1}, {num3}")
    else:
        print(f"The numbers in ascending order are: {num2}, {num3}, {num1}")
else:
    if num1 <= num2:
        print(f"The numbers in ascending order are: {num3}, {num1}, {num2}")
    else:
        print(f"The numbers in ascending order are: {num3}, {num2}, {num1}")