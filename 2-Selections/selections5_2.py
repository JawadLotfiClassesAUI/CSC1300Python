# Getting the midterm grade from the user
midterm_grade = float(input("Enter your midterm grade: "))

# Using a formula to calculate the minimum final grade needed to pass the class
final_grade_needed = (70 - (midterm_grade * 0.5)) / 0.5

if final_grade_needed <= 100: # It means that it is possible
    print(f"You need {final_grade_needed} in the final to pass the class.")
else:
    print("Sorry, you will have to retake the class!")