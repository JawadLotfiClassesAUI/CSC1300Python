# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Use a loop to get the mid grade and final grade for each student
for i in range(num_students):
    mid_grade = float(input("Enter the midterm exam grade for student", i+1, ": "))
    final_grade = float(input("Enter the final grade for student", i+1, ": "))

    # Calculate the average by multiplying the mid grade by 0.4 and the final grade by 0.6, then adding them together
    average = (mid_grade * 0.4) + (final_grade * 0.6)

    # Print the average for each student
    print("Average for student", i+1, "is", average)