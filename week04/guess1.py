#Program prompts user to guess a number
#Keeps prompting user to guess number until user guesses correct number
#Author: Clare Tubridy
#Date: 17/02/2023

numberToGuess = 30

guess = int(input("Please guess a number: "))

while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was ", numberToGuess)