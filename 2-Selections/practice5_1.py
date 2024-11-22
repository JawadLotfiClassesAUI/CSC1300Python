# Exercise 5.1: Feet to Meters Conversion
choice = input("Choose conversion type (1 for feet to meters, 2 for meters to feet): ")
if choice == "1":
    feet = float(input("Enter the length in feet: "))
    meters = feet * 0.3048
    print(f"{feet} feet is equal to {meters} meters.")
elif choice == "2":
    meters = float(input("Enter the length in meters: "))
    feet = meters / 0.3048
    print(f"{meters} meters is equal to {feet} feet.")
else:
    print("Invalid choice. Please choose 1 or 2.")