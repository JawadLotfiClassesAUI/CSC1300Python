# Exercise 5.3: Profit or Loss Calculation
income = float(input("Enter the income: "))
expenses = float(input("Enter the expenses: "))
profit = income - expenses
if profit > 0:
    print(f"Profit: {profit}")
else:
    print(f"Loss: {abs(profit)}")