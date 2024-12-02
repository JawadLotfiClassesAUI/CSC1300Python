# Get the student's age and CGPA from the user
credits = int(input("Enter your credits: "))
cgpa = float(input("Enter your CGPA: "))

# Check both conditions at the same time using the "and" operator
if credits >= 45 and cgpa >= 3.0:
    print("You are eligible for exchange!")
else:
    print("You are not eligible for exchange.")