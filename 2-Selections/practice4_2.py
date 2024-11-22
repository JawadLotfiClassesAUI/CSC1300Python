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