# Progrma prints 10 random numbers, prints them out
# Then prints out the top 3

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))
print(f"{howMany} random numbers \t {numbers}")

topOnes = numbers.copy()

topOnes.sort(reverse = True)
print(f"The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")

