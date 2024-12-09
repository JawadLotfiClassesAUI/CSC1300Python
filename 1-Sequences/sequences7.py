# We ask the user for the number of sheep and clients
sheep = int(input("Enter the number of sheep:"))
clients = int(input("Enter the number of clients:"))

# what we want is the remaining number of sheep after the maximum has been sold to the clients equally
sheep_per_client = sheep // clients
remaining_sheep = sheep % clients

print(f"After selling {sheep_per_client} to each client, {remaining_sheep} stayed with the farmer")