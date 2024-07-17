# Ask the student to enter their course grade and the total points
grade = float(input("Enter your course grade: "))
total_points = float(input("Enter the total points: "))

# Check if the grade or total points are negative
if grade < 0 or total_points < 0:
    print("Invalid input. Grade and total points cannot be negative.")
else:
    # Calculate the percentage
    percentage = (grade / total_points) * 100

    # Determine the result based on the percentage
    if percentage >= 80:
        result = "good"
    elif 70 <= percentage < 80:
        result = "satisfactory"
    else:
        result = "unsatisfactory"

    # Print the result
    print("Your result is", result)