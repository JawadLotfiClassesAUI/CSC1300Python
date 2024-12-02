# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is leap or not using either the first condition "or" the second
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")