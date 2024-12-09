# First, we need a few counters and accumulators
# counters are used to keep count of values that meet certain conditions
passing_grades = 0
failing_grades = 0
num_grades = 0

# accumulators are used to keep track of the sum of values
sum_of_grades = 0

grade = float(input("Enter a grade (enter -1 to stop): "))
while grade != -1:
    sum_of_grades += grade
    num_grades += 1
    if grade >= 60:
        passing_grades += 1
    else:
        failing_grades += 1
    grade = float(input("Enter a grade (enter -1 to stop): "))

# After the loop ends, we can calculate the class average and display the results
if num_grades != 0:
    class_average = sum_of_grades / num_grades
    print("Class Average:", class_average)
    print("Number of Passing Grades:", passing_grades)
    print("Number of Failing Grades:", failing_grades)
else:
    print("No grades entered.") # if no grades were entered, we display a message to inform the user