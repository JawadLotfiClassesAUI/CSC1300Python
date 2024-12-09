# Initialize a variable, called an accumulator, to store the sum of the numbers.
sum_of_numbers = 0

# Use a loop to get 10 numbers from the user
for i in range(10):
    number = float(input("Enter a number: "))
    sum_of_numbers += number

# Calculate the average by dividing the sum by 10
average = sum_of_numbers / 10

# Print the average
print("The average is:", average)