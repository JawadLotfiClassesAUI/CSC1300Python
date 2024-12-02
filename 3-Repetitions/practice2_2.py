# Setting our counters of even and odd numbers to 0
odd_numbers = 0
even_numbers = 0

# We will ask the user for 10 numbers
for i in range(10):
    number = int(input("Enter a number: "))
    if number % 2 == 0: # if there is no remainder when dividing by 2, we count the number as even
        even_numbers += 1
    else: # otherwise, we count it as odd
        odd_numbers += 1

print("Number of Odd Numbers:", odd_numbers)
print("Number of Even Numbers:", even_numbers)