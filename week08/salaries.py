# Program makes list that has 10 random numbers
# Between 20000 and 80000

import numpy as np 

min_salary = 20000
max_salary = 80000
number_of_entries = 10

# Ensures random numbers are the same each time its run
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

# Adds 5000 to each salary
salaries_plus = salaries + 5000

# 5% added to each salary 
salaries_mult = salaries * 1.05

# Float array, this is to convert it to an int array
new_salaries = salaries_mult.astype(int)

print ('original',salaries)
print('addition', salaries_plus)
print('multiply', salaries_mult)
print('integer', new_salaries)