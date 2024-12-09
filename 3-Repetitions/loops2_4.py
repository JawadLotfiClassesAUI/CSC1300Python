# Setting our initial population and asking the user for the target population
population = 9870
target_population = int(input("Enter the target population: "))

# We will keep increasing the population by 10% until we reach the target population
while population < target_population:
    print("Population:", population)
    population += population * 0.1 # increase the population by 10%

print("Population reached the target:", population)