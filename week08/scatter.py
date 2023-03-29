# Program makes scatter plot of ages and salaries 
# From 21 to 65

import numpy as np
import matplotlib.pyplot as plt  

min_salary = 20000
max_salary = 80000
number_of_entries = 100

# Ensures random numbers are the same each time its run
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint(low=21, high=65, size=number_of_entries)

plt.scatter(ages,salaries, label='salaries')

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color='r', label='x sqaured')

plt.title('Random Plot')
plt.xlabel('Salaries')
plt.ylabel('Age')
plt.legend()
#plt.show()

plt.savefig('prettier_plot.png')
