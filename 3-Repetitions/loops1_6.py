# We ask the user to enter the number of products sold.
num_products = int(input("Enter the number of products sold: "))
total_sales = 0

# For each product, we get the unit price and quantity
for product in range(num_products):
    price = float(input("Enter the price of product", product+1, ": "))
    quantity = int(input("Enter the quantity of product", product+1, ": "))
    sales = price * quantity
    total_sales += sales # Increment the total sales with the sales of the current product

# The final output is outside of the loop, therefore, it happens only once
print("Total sales: ", total_sales)