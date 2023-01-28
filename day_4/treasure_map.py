# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#We first get the 2 characters from our input and convert the column (first digit) into an int. We leave the row (second digit) unchanged as str.
column = int(position[0:1])
row = position[1:2]

#Just some testing, ignore. Wanted to check if the outputs are correct and so are the data types.
# print(f"Column is {column}, Row is {row}")
# print(type(column))
# print(type(row))

#Checking where our varibles fit into and changing the correct box into an 'X'.

if row in "row1":
    row1[column - 1] = 'X'    
elif row in "row2":
    row2[column - 1] = 'X'
elif row in "row3":
    row3[column - 1] = 'X'
else:
    print("Incorrect input. Please input a 2 digit number using the numbers: 1, 2 or 3 only!")


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")