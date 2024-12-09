# We need 2 pieces of information from the user, how much is 1 kilo of apples and how many kilos we want
kilo_of_apples = float(input("How many kilograms of apples are you buying? "))
cost_per_kilo = float(input("What is the cost of 1 kilo? "))

# The price before tax is simply a multiplication of both inputs
price_before_tax = kilo_of_apples * cost_per_kilo

# The price after tax is 15% more (price_after_tax = price_before_tax + 15*price_before_tax/100)
price_after_tax = price_before_tax * 1.15

# We output the price after tax
print(f"You need to pay {price_after_tax} to make this purchase")