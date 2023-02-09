#Program reads in a string and strips any leading or trailing spaces
#It also converts all letters to lower case
#It then outputs the lengths of th original string and the normalised one
#Author: Clare Tubridy
#Date: 09/02/2023

raw_string = input("Enter a string: ")
normalised_string = raw_string.strip().lower()

lenght_of_raw_string = len(raw_string)
length_of_normalised_string= len(normalised_string)

print(f"That string normalised is: {normalised_string}")
print(f"We reduced the input string from {lenght_of_raw_string} to {length_of_normalised_string} characters")
