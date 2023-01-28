# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# This is how you work out whether if a particular year is a leap year.

    # on every year that is evenly divisible by 4 

    # **except** every year that is evenly divisible by 100 

    # **unless** the year is also evenly divisible by 400


#Let's write up a different variable for each requirement we will use for the checking and we will use the number in the naming to distinguish it.

year_4 = year % 4
year_100 = year % 100
year_400 = year % 400

if year_4 == 0:
    if year_100 == 0:
        if year_400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#It might be best to use drar.io when you first would need to draw up a logic and then get to coding after that.