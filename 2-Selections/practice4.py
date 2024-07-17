# Exercise 4.1: Body Mass Index (BMI) Calculator
# Ask the user to enter their weight in kilograms and height in meters
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
# Calculate the BMI using the formula: BMI = weight / (height ** 2)
bmi = weight / (height ** 2)
# Check the BMI category and display the result
if bmi < 18.5:
    print("Your BMI is low.")
elif bmi > 25:
    print("Your BMI is high.")
else:
    print("Your BMI is normal.")

# Exercise 4.2: Total Grade Calculator
# Ask the user to enter their quiz average, midterm grade, and final exam grade
quiz = float(input("Enter your quiz average (out of 100): "))
midterm = float(input("Enter your midterm grade (out of 100): "))
final = float(input("Enter your final exam grade (out of 100): "))
# Calculate the total grade using the formula: Total = Quiz * 0.25 + Midterm * 0.35 + Final * 0.4
total = quiz * 0.25 + midterm * 0.35 + final * 0.4
# Check the total grade category and display the result
if total > 80:
    print("Your total grade is Good.")
elif 70 <= total <= 80:
    print("Your total grade is Satisfactory.")
else:
    print("Your total grade is Unsatisfactory.")