# Here, the user needs to enter 2 inputs: the midterm and final exam grades
midterm = eval(input("Enter your midterm grade:"))
final = eval(input("Enter your final exam grade:"))

# The midterm is worth 40% and the final 60%, so this is a weighted average
total = midterm*0.4 + final*0.6

# The total grade of the student is now ready to be displayed.
print(f"Your total grade is {total}")