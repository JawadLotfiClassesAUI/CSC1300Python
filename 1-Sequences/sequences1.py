# First, we need to let the user provide the length and width of the room
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

# Then, we compute the result which is the surface area and perimeter
surface = length * width
perimeter = (length + width) * 2

# Finally, we display the result in a helpful sentence
print(f"The area is {surface} square meters")
print(f"The perimeter is {perimeter} meters")