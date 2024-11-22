# The data we need the user to enter is the temperature in Fahrenheit
fahr = float(input("Enter the temperature:"))

# We get the equivalent in Celsius by using the appropriate formula
celsius = (fahr - 32) *5/9

# Finally, we display the computed value
print(f"It is equal to {celsius} celsius")