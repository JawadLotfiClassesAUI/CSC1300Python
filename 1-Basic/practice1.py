# Here we are entering the length and width of the room
length = eval(input("Enter the length:"))
width = eval(input("Enter the width:"))

# Here we compute the result which is the surface area
surface = length * width
perimeter = (length + width) * 2

# Finally, we display the result in a helpful sentence
print(f"The area is {surface} square meters")
print(f"The perimeter is {perimeter} meters")