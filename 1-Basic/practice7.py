# We ask the user for the number of sheep and clients
sheep = eval(input("Enter the number of sheep:"))
clients = eval(input("Enter the number of clients:"))

# what we want is the remaining number of sheep after the maximum has been sold to the clients equally
remaining_sheep = sheep % clients

print(f"After selling the sheep equally to the clients, {remaining_sheep} stayed with the farmer")