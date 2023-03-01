# This program reads in numbers until the user enters 0
# Program will then print out each of the numbers entered
# Prints out average of all numbers entered.

#empty array to store list of input numbers
numbers = []

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    #read next number and check if 0
    number = int(input("Enter another number (0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)/len(numbers))
print(f"The average is {average}")