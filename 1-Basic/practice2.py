# First, we need to get the data from the user, which is the length in inches
inches = eval(input("Enter the number of inches:"))

# Then we use the formula required to convert to centimeters: 1 inch equals 2.54 centimeters
cms = inches * 2.54

# Finally, we display the result we just got.
print(f"It is equal to {cms} centimeters")