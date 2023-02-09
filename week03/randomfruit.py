#this program prints out random fruit
#Author: Clare Tubridy
#Date: 09/02/2023

import random

fruits = ("Apple", "Orange", "Banana", "Pear", "Strawberry")

#we want a random number between 0 and length-1

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print(f" A random fruit: {fruit}")