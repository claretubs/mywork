#Program that reads in two numbers and outputs the integer
#answer and remainder
#Author: Clare Tubridy
#Date: 09/02/2023

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x//y)      #//gives the int division
remainder = x%y         # % gives the remainder

print(f"{x} divided by {y} is {answer} with remainder {remainder}")