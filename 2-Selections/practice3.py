# 4.1: Program to check eligibility for exchange
# Get the student's age and CGPA from the user
credits = int(input("Enter your credits: "))
cgpa = float(input("Enter your CGPA: "))

# Check if the student is eligible for exchange
if credits >= 45 and cgpa >= 3.0:
    print("You are eligible for exchange!")
else:
    print("You are not eligible for exchange.")

# 4.2: Program to check if a year is leap or not
# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is leap or not
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")