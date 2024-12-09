# Getting all three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# First we check one number against the other two, making sure it is the smallest
if num1 <= num2 and num1 <= num3:
    # Then we check the smallest against the third
    if num2 <= num3:
        print("The numbers in ascending order are:", num1, num2, num3)
    else:
        print("The numbers in ascending order are:", num1, num3, num2)
# Same process here for num2
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print("The numbers in ascending order are:", num2, num1, num3)
    else:
        print("The numbers in ascending order are:", num2, num3, num1)
# Same process here for num3
else:
    if num1 <= num2:
        print("The numbers in ascending order are:", num3, num1, num2)
    else:
        print("The numbers in ascending order are:", num3, num2, num1)