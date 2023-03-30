# Demonstrate making a pie plot of the unique occurence of values in an array

import numpy as np
import matplotlib.pyplot as plt

# Make array of occurences
possible_counties = ['Mayo', 'Clare', 'Galway', 'Roscommon', 'Limerick', 'Cork']

# Pick 100 randomly from possible counties with the frequence set in p
counties = np.random.choice(
    possible_counties,
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

# Right now we need the numbere of occurances of each county
# This returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts = True)

# We can now put this into a pie plot
plt.pie(counts, labels=unique)

plt.show()