# The only input we need is the amount of money the user has
amount = int(input("Enter the amount of money: "))

b200 = amount // 200 # With the integer division, we get the number of 200 dhs bills
print(f"{b200} bills of 200 dhs")
amount = amount % 200 # With the modulo operator, we get the remaining amount

# Repeat the process for the other bills and coins
b100 = amount // 100
print(f"{b100} bills of 100 dhs")
amount = amount % 100

b50 = amount // 50
print(f"{b50} bills of 50 dhs")
amount = amount % 50

b20 = amount // 20
print(f"{b20} bills of 20 dhs")
amount = amount % 20

c10 = amount // 10
print(f"{c10} coins of 10 dhs")
amount = amount % 10

c5 = amount // 5
print(f"{c5} coins of 5 dhs")
amount = amount % 5

c2 = amount // 2
print(f"{c2} coins of 2 dhs")
amount = amount % 2

print(f"{amount} coins of 1 dh")