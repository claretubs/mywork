# Program plots a histogram of salaries

import numpy as np
import matplotlib.pyplot as plt  

min_salary = 20000
max_salary = 80000
number_of_entries = 100

# Ensures random numbers are the same each time its run
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

plt.hist(salaries)
plt.show()