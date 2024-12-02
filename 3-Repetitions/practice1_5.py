# Same exercise as practice1_4.py but with an input to let the user determine the start
# Also, uses the sleep function to pause the program for a second

# Here we import the sleep function from the time module in the Python standard library
from time import sleep

x = int(input("Enter the value of x: "))
for count in range(x, -1, -1):
    print(count)
    sleep(1) # This pauses the program for 1 second