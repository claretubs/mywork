#Program rounds a number 
#Rounds to the nearest even number e.g. 4.5 rounds to 4 but 5.5 rounds to 6
#do not use it accuracy is essential
#Author: Clare Tubridy
#Date: 09/02/2023

number_to_round = float(input("Enter a float number: "))
rounded_number = round(number_to_round)

print(f"{number_to_round} rounded is {rounded_number}")