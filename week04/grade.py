#Reads a students percentage mark and prints out corresponding grade
#Author: Clare Tubridy
#Date: 16/02/2023

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage >100:
    print ("Please enter a number between 0 to 100")
elif percentage < 40:           #we know it is greater than 0
    print("Fail")
elif percentage < 50:           #between 40 and 49
    print("Pass")
elif percentage < 60:           #between 50 and 59
    print("Merit1")
elif percentage < 70:           #bewteen 60 and 69
    print("Merit2")
else:                           #only option left between 70 and 100
    print("Distinction")