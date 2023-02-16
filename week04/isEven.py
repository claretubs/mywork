#Program reads an input and outputs whether the number is even or odd
#Author: Clare Tubridy
#Date: 16/02/2023

number = int(input("enter a number: "))

if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")