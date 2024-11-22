# 3.2: Program to check if a year is leap or not
# Get the year from the user
year = int(input("Enter a year: "))
# Check if the year is leap or not
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")