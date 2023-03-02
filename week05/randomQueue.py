# Program puts 10 random numbers into a queue
# Outputs all the values of the queue and then takes the
# Numbers from the queue one at a time
# Author: Clare Tubridy

import random

queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print(f"Queue is {queue}")

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print(f"Current Number is {currentNumber} and the queue is {queue}")

print("The que is now empty")
