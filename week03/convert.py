#Program that takes in a float number and returns the absolute in cents 
#Author: Clare Tubridy
#Date: 09/02/2023

amount_in_dollars = float(input("Enter a number: "))
absolute_value = abs(amount_in_dollars)

amount_in_cents = absolute_value*100            #converts dollars to cents

print(f"Amount entered in dollars was {amount_in_dollars} and the amount in cents is {amount_in_cents}")