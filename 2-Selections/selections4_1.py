# Ask the user to enter their weight in kilograms and height in meters
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI using the formula: BMI = weight / (height ** 2)
bmi = weight / (height ** 2)

# Check the BMI category and display the result
if bmi < 18.5:
    print("Your BMI is low.")
elif bmi > 25:
    print("Your BMI is high.")
else:
    print("Your BMI is normal.")