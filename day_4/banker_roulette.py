# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

#We need the length of the list 
max_number = len(names)

#We need a random number from 0 to the amount of names in the list - 1 (as list's are indexed starting from 0)
random_number = random.randint(0, max_number - 1)

#Printing out the lucky winner.
print(f"{names[random_number]} is going to buy the meal today!")