# Exercise 5.2: Grade Calculation
midterm_grade = float(input("Enter your midterm grade: "))
final_grade_needed = (70 - (midterm_grade * 0.5)) / 0.5
if final_grade_needed <= 100:
    print(f"You need {final_grade_needed} in the final to pass the class.")
else:
    print("Sorry, you will have to retake the class!")