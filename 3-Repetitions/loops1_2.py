# Get the value of x from the user
x = int(input("Enter the value of x: "))

# Initialize a variable to store the sum of the numbers
sum_of_numbers = 0

# Use a loop to get x numbers from the user
for i in range(x):
    number = float(input("Enter a number: "))
    sum_of_numbers += number

# Calculate the average by dividing the sum by x
average = sum_of_numbers / x

# Print the average
print("The average is:", average)