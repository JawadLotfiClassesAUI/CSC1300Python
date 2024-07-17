# 1.1: Write a program that computes the average of 10 numbers.
# Hint: The average is the sum of these 10 numbers divided by 10.

# Initialize a variable to store the sum of the numbers
sum_of_numbers = 0

# Use a loop to get 10 numbers from the user
for i in range(10):
    number = int(input("Enter a number: "))
    sum_of_numbers += number

# Calculate the average by dividing the sum by 10
average = sum_of_numbers / 10

# Print the average
print("The average is:", average)


# 1.2: Write a program that computes the average of x numbers. The value of x is entered by the user at the beginning.

# Get the value of x from the user
x = int(input("Enter the value of x: "))

# Initialize a variable to store the sum of the numbers
sum_of_numbers = 0

# Use a loop to get x numbers from the user
for i in range(x):
    number = int(input("Enter a number: "))
    sum_of_numbers += number

# Calculate the average by dividing the sum by x
average = sum_of_numbers / x

# Print the average
print("The average is:", average)


# 1.3: Write a program that asks the user about the number of students in a class and then for each one of them ask for the mid grade and final grade (both out of 100 points). Your program outputs each student average. (40% for mid and 60% for final)

# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Use a loop to get the mid grade and final grade for each student
for i in range(num_students):
    mid_grade = int(input("Enter the mid grade for student {}: ".format(i+1)))
    final_grade = int(input("Enter the final grade for student {}: ".format(i+1)))

    # Calculate the average by multiplying the mid grade by 0.4 and the final grade by 0.6, then adding them together
    average = (mid_grade * 0.4) + (final_grade * 0.6)

    # Print the average for each student
    print("Average for student {} is: {}".format(i+1, average))

# 1.4: Write a program that counts down from 5 to 0.
count = 5
while count >= 0:
    print(count)
    count -= 1


# 1.5: Write a program that counts down from x to 0. The value of x needs to be specified by the user at the beginning.
x = int(input("Enter the value of x: "))
while x >= 0:
    print(x)
    x -= 1


# 1.6: Write a program that asks a shop owner to enter the number of products that he sold. After that, for each product the user needs to enter the price and the quantity. The program must compute the total sales and display it at the very end.
num_products = int(input("Enter the number of products sold: "))
total_sales = 0

for i in range(num_products):
    price = float(input("Enter the price of product {}: ".format(i+1)))
    quantity = int(input("Enter the quantity of product {}: ".format(i+1)))
    sales = price * quantity
    total_sales += sales

print("Total sales: ", total_sales)