# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h = float(height)
w = float(weight)

BMI = w / h**2
BMI_int = int(BMI)
print(BMI_int)

#EXTRA NOTES NOT PART OF THE SOLUTION

#Note: Using the // (Floor Division) you can turn the result into an integer right away.
#No need to convert it manually.

#You can use the "shorthand" /= or += to quickly do a mathematical operation without specifying variables.

#Let's say you want to add something to the result that "your BMI is:"
#For this you can use f strings so something like:
print(f"Your BMI is {BMI_int}, because your height is {height} ms and your weight is {weight} kgs")
#As you can see you simply add f (not F) at the beginning of the string 
# then you can freely add any varibles to the string regardless of their respective datatype.