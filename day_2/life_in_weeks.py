# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#First we convert the string into an int and subtract it from 90.

age_as_int = int(age)
years_remaining = 90 - age_as_int

#We do the calculation of the remaining days, weeks and months.

days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")