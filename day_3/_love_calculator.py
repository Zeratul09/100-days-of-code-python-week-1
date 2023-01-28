# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Converting names into a lowercase one:
lower_name1 = name1.lower()
lower_name2 = name2.lower()

#Let's concatanate them and remove any spaces in the names:
both_names = (lower_name1 + lower_name2).replace(" ", "")

#Calculating how many times the letters in "TRUE LOVE" occurs:
#As we haven't learned about Regex or importing different functions we will stick to using only a very basic solution:
#We will count the letters for "true" and "love" separately:

letters_true = 0

if "t" in both_names:
    letters_true += both_names.count("t")
if "r" in both_names:
    letters_true += both_names.count("r")
if "u" in both_names:
    letters_true += both_names.count("u")
if "e" in both_names:
    letters_true += both_names.count("e")

letters_love = 0

if "l" in both_names:
    letters_love += both_names.count("l")
if "o" in both_names:
    letters_love += both_names.count("o")
if "v" in both_names:
    letters_love += both_names.count("v")
if "e" in both_names:
    letters_love += both_names.count("e")

#Now, we will concatanate the 2 numbers to get our "love score"

love_score = int(str(letters_true) + str(letters_love))

#Finally, we will evaulate the results and return it:

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")