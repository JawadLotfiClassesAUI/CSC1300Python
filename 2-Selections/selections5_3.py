# Getting income and expenses from the user
income = float(input("Enter the income: "))
expenses = float(input("Enter the expenses: "))

# Calculating the difference between income and expenses
difference = income - expenses

# Displaying if it is a profit or a loss
if difference > 0:
    print(f"Profit: {difference}")
else:
    print(f"Loss: {abs(difference)}")