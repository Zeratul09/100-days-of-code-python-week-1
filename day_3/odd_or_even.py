# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Modulo in this case leaves either a 0 or 1 after the operation.
modulo = number % 2

if modulo >= 1:
    print("This is an odd number.")
else:
    print("This is an even number.")