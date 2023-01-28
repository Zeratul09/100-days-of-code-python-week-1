#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Before we start out don't forget, if you want 5 iterations of a loop you can either do it with range(0, 5) or range(1, 5 + 1).
#You can also either create a varible as a string, no need to add lists together, it just makes it a bit more challanging.


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#First, I've solved the harder challange, so we will use it's elements and we will remove the randomizer part:

#First we will create three varibles for three lists. This is where we are going to store our selected characters from the for loops.
selected_letters = []
selected_symbols = []
selected_numbers = []

#We will run a loop through our "letters" list to select the required amount of letters.
for letter in range(0, nr_letters):
    selected_letters.append(random.choice(letters))
    
#We will run a loop through our "symbols" list to select the required amount of symbols.
for symbol in range(0, nr_symbols):
    selected_symbols.append(random.choice(symbols))
    
#We will run a loop through our "numbers" list to select the required amount of numbers.
for number in range(0, nr_numbers):
    selected_numbers.append(random.choice(numbers))
    
#We will merge our three lists together:
merged_lists = selected_letters + selected_symbols + selected_numbers

#We will randomize our new merged list:
#random.shuffle(merged_lists)

#Finally, first, we will create a new varible for our final string and we will print out the password into it as one string using a for loop:

password = ""

for i in merged_lists:
    password += str(i)+""

print(f"Your password should be: {password}")


#Hard Level - Order of characters randomised: - We will create this one too:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#First we will create three varibles for three lists. This is where we are going to store our selected characters from the for loops.
selected_letters = []
selected_symbols = []
selected_numbers = []

#We will run a loop through our "letters" list to select the required amount of letters.
for letter in range(0, nr_letters):
    selected_letters.append(random.choice(letters))
    
#We will run a loop through our "symbols" list to select the required amount of symbols.
for symbol in range(0, nr_symbols):
    selected_symbols.append(random.choice(symbols))
    
#We will run a loop through our "numbers" list to select the required amount of numbers.
for number in range(0, nr_numbers):
    selected_numbers.append(random.choice(numbers))
    

#We will merge our three lists together:
merged_lists = selected_letters + selected_symbols + selected_numbers

#We will randomize our new merged list:
random.shuffle(merged_lists)

#Finally, first, we will create a new varible for our final string and we will print out the password into it as one string using a for loop:

password = ""

for i in merged_lists:
    password += str(i)+""

print(f"Your password should be: {password}")
