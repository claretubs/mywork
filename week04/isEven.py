#Program reads an input and outputs whether the number is even or odd
#Author: Clare Tubridy
#Date: 16/02/2023

number = int(input("enter a number: "))

#Extra quetion number 4 asks to modify the origrnal prgoramme to a
#while loop so that it keeps prompting the user for a number
#until the user enters -1

while number != int('-1'):

    if (number % 2) == 0:
        print (f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

    number = int(input("-1 to quit: "))

print(f"End of Session")
    


