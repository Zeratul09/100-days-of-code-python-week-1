#Write your code below this row 👇

#We will first create a varible to use as a placeholder to add our numbers together.
total = 0
#We will define the range in the way that only the even numbers are added together by adding an incremental step of 2.
#Also, we will have to start our range from 0, as 1 is an odd number, but if we want to the above to work it will be 0 + 2 + 4... + 96 + 98 + 100
for number in range(0, 101, 2):
    total += number

print(total)

#Another solution would be to use the modulo operator so:

# total = 0
# for numbers in range (1, 101):
#     if number % 2 == 0:
#         total += number

#Always make sure that the indentations are correct